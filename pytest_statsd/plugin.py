"""pytest_statsd.plugin

.. codeauthor:: John Lane <jlane@fanthreesixty.com>

"""

from __future__ import absolute_import
import time
import statsd


def pytest_addoption(parser):
    """

    :param parser:
    :return:
    """

    group = parser.getgroup('terminal reporting')
    group.addoption('--stats-d', action='store_true',
                    help='send test results to graphite')
    group.addoption('--stats-host', action='store', dest='stats_host',
                    metavar='host', default='localhost',
                    help='statsd host. default is \'localhost\'')
    group.addoption('--stats-port', action='store', dest='stats_port',
                    metavar='port', default=8125,
                    help='statsd port. default is 8125')
    group.addoption('--stats-prefix', action='store', dest='stats_prefix',
                    metavar='prefix', default=None,
                    help='prefix to give all stats')


def pytest_configure(config):
    """

    :param config:
    :return:
    """

    stats_d = config.getoption('stats_d')

    # prevent opening statsd on slave nodes (xdist)
    if stats_d and not hasattr(config, 'slaveinput'):
        config._graphite = GraphiteReport(config)
        config.pluginmanager.register(config._graphite)


def pytest_unconfigure(config):
    """

    :param config:
    :return:
    """

    graphite = getattr(config, '_graphite', None)

    if graphite:

        del config._graphite
        config.pluginmanager.unregister(graphite)


class GraphiteReport(object):
    """Graphite report implementation
    """

    def __init__(self, config):

        self.errors = self.failed = 0
        self.passed = self.skipped = 0
        self.xfailed = self.xpassed = 0
        self.total = 0

        self.config = config
        self.host = config.getoption('stats_host')
        self.port = config.getoption('stats_port')
        self.prefix = config.getoption('stats_prefix')
        self.suite_start_time = 0

    def pytest_runtest_logreport(self, report):
        """Add report metrics

        :param pytest.Report report: Test case report
        :return:
        """

        if report.passed:
            self.append_passed(report)

        elif report.failed:
            self.append_failed(report)

        elif report.skipped:
            self.append_skipped(report)

    def append_passed(self, report):
        """Add passed test metric

        :param pytest.Report report: Test case report
        :return:
        """

        if report.when == 'call':

            if hasattr(report, "wasxfail"):
                self.xpassed += 1

            else:
                self.passed += 1

    def append_failed(self, report):
        """Add failed test metric

        :param pytest.Report report: Test case report
        :return:
        """

        if report.when == "call":

            if hasattr(report, "wasxfail"):
                self.xpassed += 1

            else:
                self.failed += 1

        else:
            self.errors += 1

    def append_skipped(self, report):
        """Add skipped test metric

        :param pytest.Report report: Test case report
        :return:
        """

        if hasattr(report, "wasxfail"):
            self.xfailed += 1

        else:
            self.skipped += 1

    def pytest_sessionstart(self, session):
        """before test run begins

        :param pytest.Session session:
        :return:
        """

        self.suite_start_time = time.time()

    def pytest_sessionfinish(self, session):
        """whole test run finishes

        :param pytest.Session session:
        :return:
        """

        stats = statsd.StatsClient(self.host, self.port, prefix=self.prefix)
        stats.gauge('passed', self.passed)
        stats.gauge('skipped', self.skipped)
        stats.gauge('failed', self.failed)
        stats.gauge('errors', self.errors)
        stats.gauge('xfailed', self.xfailed)
        stats.gauge('xpassed', self.xpassed)
        stats.gauge('total', sum([self.passed, self.skipped, self.failed,
                                  self.errors, self.xfailed, self.xpassed]))
        stats.gauge('aggregate_runs', 1, delta=True)

        if sum([self.errors, self.failed]) == 0:
            stats.gauge('aggregate_passing', 1, delta=True)

        else:
            stats.gauge('aggregate_failing', 1, delta=True)

        duration = int((time.time() - self.suite_start_time) * 1000)
        stats.timing('duration', duration)

    def pytest_terminal_summary(self, terminalreporter):
        """add additional section in terminal summary reporting

        :param terminalreporter:
        :return:
        """

        terminalreporter.write_sep('-', 'sent results to http://{}:{}'.format(self.host, self.port))
