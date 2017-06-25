#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup


setup(
    name='drf_google',
    url='https://github.com/sassoo/drf_google',
    license='BSD',
    description='Google API interface for DRF',
    author='Sassoo',
    author_email='noreply@devnull.seriously',
    install_requires=[
        'geopy',
        'requests',
    ],
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
