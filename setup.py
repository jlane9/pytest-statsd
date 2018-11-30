"""setup.py

.. codeauthor:: John Lane <jlane@fanthreesixty.com>

"""

import os
from setuptools import setup
from pytest_statsd import __author__, __email__, __license__, __version__


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setup(name='pytest-statsd',
      version=__version__,
      author=__author__,
      author_email=__email__,
      description='pytest plugin for reporting to graphite',
      license=__license__,
      keywords='py.test pytest statsd graphite grafana report',
      url=u'https://github.com/jlane9/pytest-statsd',
      project_urls={
          "Documentation": "https://pytest-statsd.readthedocs.io/en/latest/",
          "Tracker": "https://github.com/jlane9/pytest-statsd/issues"
      },
      packages=['pytest_statsd'],
      entry_points={'pytest11': ['statsd = pytest_statsd.plugin', ]},
      long_description=read("README.md"),
      long_description_content_type="text/markdown",
      install_requires=['pytest>=3.0.0', 'statsd>=3.2.1'],
      python_requires=">=2.7",
      tests_require=[
          "pytest>=3.0.0,<5.0.0",
          "pytest-cov>=2.6.0",
          "pytest-pep8>=1.0.0",
          "requests>=2.18.4,<3.0.0"
      ],
      extras_require={
          "release": [
              "bumpversion>=0.5.0",
              "Sphinx>=1.8.0",
              "sphinx-autobuild>=0.7.0",
              "sphinx-rtd-theme>=0.4.2",
              "twine>=1.12.0"
          ]
      },
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Framework :: Pytest',
          'Intended Audience :: Developers',
          "License :: OSI Approved :: MIT License",
          "Natural Language :: English",
          'Operating System :: POSIX',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: MacOS :: MacOS X',
          'Programming Language :: Python :: 2.7',
          'Topic :: Software Development :: Testing',
          'Topic :: Software Development :: Quality Assurance',
          'Topic :: Software Development :: Libraries',
          'Topic :: Utilities'
      ])
