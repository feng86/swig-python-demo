#!/usr/bin/env python
# -*- coding:utf-8 -*-

""" setup script """
import runpy

from setuptools import Extension, find_packages, setup


EXAMPLE_EXT = Extension(
    name='_example',
    sources=[
        'src/example/example.c',
        'src/example/example.i',
    ],
)

INFO = runpy.run_path('src/example/_meta.py')

setup(
    name='swig-example-demo',
    description='A Python demo for SWIG',
    version=INFO['__version__'],
    author=INFO['__author__'],
    license=INFO['__copyright__'],
    author_email=INFO['__email__'],
    url=INFO['__url__'],
    keywords=['SWIG', 'demo'],

    packages=find_packages('src'),
    package_dir={'': 'src'},
    ext_modules=[EXAMPLE_EXT],

    python_requires='>=3.4',
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)
