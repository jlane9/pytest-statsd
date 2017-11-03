"""setup.py

.. codeauthor:: John Lane <jlane@fanthreesixty.com>

"""

from setuptools import setup
from pytest_statsd import __author__, __email__, __license__, __version__


setup(name='pytest-statsd',
      version=__version__,
      description='pytest plugin for reporting to graphite',
      author=__author__,
      author_email=__email__,
      url=u'https://github.com/jlane9/pytest-statsd',
      packages=['pytest_statsd'],
      entry_points={'pytest11': ['statsd = pytest_statsd.plugin', ]},
      install_requires=['pytest>=2.7', 'statsd>=3.2.1'],
      keywords='py.test pytest statsd graphite grafana report',
      license=__license__,
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Framework :: Pytest',
          'Intended Audience :: Developers',
          'Operating System :: POSIX',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: MacOS :: MacOS X',
          'Topic :: Software Development :: Testing',
          'Topic :: Software Development :: Quality Assurance',
          'Topic :: Software Development :: Libraries',
          'Topic :: Utilities',
          'Programming Language :: Python :: 2.7',
      ])
