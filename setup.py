# -*- coding: utf-8 -*-
from setuptools import setup

def readme():
	with open('README.rst') as f:
		return f.read()

setup(name='cyanide-bot',
	  version='0.1',
	  description='Imgur user bot that posts current cyanide and happiness comics',
	  long_description=readme(),
	  classifiers=[
	  	'Development Status :: 2 - Pre-Alpha',
	  	'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python :: 3'
      ],
	  url='',
	  author='Cody Rocker',
	  author_email='cody.rocker.83@gmail.com',
	  license='GNU/GPL',
	  packages=['cyanide_bot'],
	  install_requires=[
	  	'imgurpython'
	  ],
	  scripts=['bin/cyanide_bot'],
	  include_package_data=True,
	  zip_safe=False)