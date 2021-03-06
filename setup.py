from setuptools import setup, find_packages
import sys, os

def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()
setup(
  name = 'heywatch',
  version = '2.2.1',
  py_modules = ['heywatch.job', 'heywatch.config'],
  packages=find_packages(exclude=['tests*']),
  author='Bruno Celeste',
  author_email='bruno@heywatch.com',
  description='A python wrapper around the HeyWatch API',
  license='MIT License',
  url='http://www.heywatchencoding.com',
  keywords='heywatch api',
  install_requires=[ "httplib2" ],
	long_description="""Client Library for encoding Videos with HeyWatch

HeyWatch is a Video Encoding Web Service.

For a CLI, look at the ruby version: http://github.com/particles/heywatch-ruby

For more information:

* HeyWatch: http://www.heywatchencoding.com
* API Documentation: http://www.heywatchencoding.com/docs
* Twitter: @heywatch / @sadikzzz

Changelogs

2.2.0
Added a new method #config to generate a full configuration based on the given parameters. It's especially useful to handle dynamic settings like source or variables that can be set directly in code.

2.0.0
New version of the client library which uses the HeyWatch API v2. This library is not compatible with 1.x

1.0.0
First version

"""
)