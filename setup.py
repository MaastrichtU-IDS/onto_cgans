#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    version='0.0.1',
    name='onto-cgans',
    license='MIT License',
    description='Ontology-embedding differential privacy conditional generative adversarial network (Onto-CGANS)',
    author='Chang Sun, Léopold Cudilla',
    author_email='chang.sun@maastrichtuniversity.nl leopold.cudilla@maastrichtuniversity.nl',
    url='',
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.8.0',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=open("requirements.txt", "r").readlines(),
    tests_require=['pytest==5.2.0'],
    setup_requires=['pytest-runner'],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9"
    ]
)
