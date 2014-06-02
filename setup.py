#!/usr/bin/env python

from os import path
from codecs import open
from setuptools import setup

# Get the long description
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
	long_description = f.read()

setup(name='pygments-xslfo-formatter',
	version='1.1',
	description='A pygments formatter that outputs <fo:inline> tags',
	long_description=long_description,
	keywords='syntax highlighting xsl-fo',
	author='Steve Ratcliffe',
	author_email='sr@parabola.me.uk',
	url='https://bitbucket.org/sratcliffe/pygments-xslfo-formatter',
	license='MIT',
	platforms='any',

	classifiers=[
		'Development Status :: 4 - Beta',
		#'Development Status :: 5 - Production/Stable',

		'Intended Audience :: Developers',
		'Intended Audience :: End Users/Desktop',

		# Pick your license as you wish (should match "license" above)
		'License :: OSI Approved :: MIT License',

		# Specify the Python versions you support here. In particular, ensure
		# that you indicate whether you support Python 2, Python 3 or both.
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 2.7',

		'Topic :: Text Processing :: Filters',
	],

	packages=['pygments_xslfo_formatter'],

	entry_points={
		'pygments.formatters': ['xslfo = pygments_xslfo_formatter.xslfo:XslfoFormatter']
	},

	install_requires=['Pygments'],
)
