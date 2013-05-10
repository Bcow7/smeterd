#!/usr/bin/env python
from setuptools import setup

from smeterd import VERSION
from smeterd import DESC


setup(
    name = 'smeterd',
    version = VERSION,
    packages = [
        'smeterd'
    ],
    url = 'http://nrocco.github.io/',
    author = 'Nico Di Rocco',
    author_email = 'dirocco.nico@gmail.com',
    description = DESC,
    include_package_data = True,
    install_requires = [
        'pyserial>=2.6',
        'bottle>=0.11.6',
        'bottle-sqlite>=0.1.2',
        'pycli_tools'
    ],
    dependency_links = [
        'https://github.com/nrocco/pycli-tools/tarball/master#egg=pycli_tools-dev'
    ],
    entry_points = {
        'console_scripts': [
            'smeterd = smeterd.main:parse_and_run',
        ]
    },
    classifiers = [
        'Development Status :: 5 - Production/Stable',
         'Operating System :: OS Independent',
         'Programming Language :: Python :: 2.6',
         'Programming Language :: Python :: 2.7',
         'Topic :: Internet :: WWW/HTTP',
         'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
