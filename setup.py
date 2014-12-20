#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import bookmap
version = bookmap.__version__

setup(
    name='bookmap',
    version=version,
    author='',
    author_email='jstratm@yahoo.com',
    packages=[
        'bookmap',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.7.1',
    ],
    zip_safe=False,
    scripts=['bookmap/manage.py'],
)
