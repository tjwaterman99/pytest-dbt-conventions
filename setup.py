#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-dbt-conventions',
    version='0.1.0',
    author='Tom Waterman',
    author_email='tjwaterman99@gmail.com',
    maintainer='Tom Waterman',
    maintainer_email='tjwaterman99@gmail.com',
    license='Apache Software License 2.0',
    url='https://github.com/tjwaterman99/pytest-dbt-conventions',
    description='A plugin for validating dbt project conventions',
    long_description=read('README.rst'),
    py_modules=['pytest_plugin'],
    python_requires='>=3.5',
    install_requires=['pytest>=6.2.5'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache Software License',
    ],
    entry_points={
        'pytest11': [
            'dbt-conventions = pytest_plugin',
        ],
    },
)
