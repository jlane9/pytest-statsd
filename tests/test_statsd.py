from numbers import Number
import os
from random import choice
import time
import requests
import pytest


class TestGenerateData(object):
    """Generate test data for statsd
    """

    pytestmark = [pytest.mark.generate]

    @pytest.fixture
    def dummy(self):
        raise Exception('oops')

    @pytest.mark.pass_only
    def test_passed(self):

        time.sleep(choice(range(0, 10)))

    @pytest.mark.fail_only
    def test_failed(self):
        pytest.fail('Failed test')

    def test_fail_without_stacktrace(self):
        pytest.fail('Failure without stacktrace', False)

    def test_skipped(self):
        pytest.skip('Skipped test')

    def test_error(self, dummy):
        assert dummy == 2

    @pytest.mark.expected_fail
    @pytest.mark.xfail(raises=ZeroDivisionError)
    def test_expected_failure(self):

        i = 1 / 0
        print(i)

    @pytest.mark.xfail()
    def test_unexpected_pass(self):
        pass


class TestStatsD(object):
    """Test Statsd plugin
    """

    BASE_URL = os.environ.get('GRAPHITE_URL', "http://localhost/render/")
    pytestmark = [pytest.mark.statsd]

    def get_data(self, target):
        """Gather data from graphite for data point

        :param str target: Graphite data point namespace
        :return:
        """

        assert isinstance(target, str)

        r = requests.get(self.BASE_URL, params={'target': target, 'format': 'json'})

        if not r.ok:
            pytest.fail("%s return status code %i" % (r.url, r.status_code))

        json = r.json()
        return [point[0] for point in json[0]['datapoints'] if isinstance(point[0], Number)] if json else []

    @pytest.mark.parametrize('data_point', (
            'stats.gauges.passed',
            'stats.gauges.skipped',
            'stats.gauges.failed',
            'stats.gauges.errors',
            'stats.gauges.xfailed',
            'stats.gauges.xpassed',
            'stats.gauges.total',
            'stats.gauges.aggregate_runs',
            'stats.gauges.aggregate_passing',
            'stats.gauges.aggregate_failing',
            'stats.timers.duration.lower'
    ))
    def test_graphite_result(self, data_point):
        """Test to make sure data points are collected by statsd

        :param str data_point: Data point to test
        :return:
        """

        data = self.get_data(data_point)

        if not data:
            pytest.fail('Nothing returned for %s' % data_point)

        if max(data) in (0, None, ''):
            pytest.fail('%s did not increment %i' % (data_point, max(data)))
