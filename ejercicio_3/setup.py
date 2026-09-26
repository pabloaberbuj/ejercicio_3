#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
===============================
HtmlTestRunner
===============================


.. image:: https://img.shields.io/pypi/v/ejercicio_3.svg
        :target: https://pypi.python.org/pypi/ejercicio_3
.. image:: https://img.shields.io/travis/pabloaberbuj/ejercicio_3.svg
        :target: https://travis-ci.org/pabloaberbuj/ejercicio_3

Es el proyecto del ejercicio 3 de Desarrollo con python


Links:
---------
* `Github <https://github.com/pabloaberbuj/ejercicio_3>`_
"""

from setuptools import setup, find_packages

requirements = [ ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Pablo Aberbuj",
    author_email='pabloaberbuj@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Es el proyecto del ejercicio 3 de Desarrollo con python",
    install_requires=requirements,
    license="MIT license",
    long_description=__doc__,
    include_package_data=True,
    keywords='ejercicio_3',
    name='ejercicio_3',
    packages=find_packages(include=['ejercicio_3']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/pabloaberbuj/ejercicio_3',
    version='0.1.0',
    zip_safe=False,
)
