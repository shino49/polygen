#!/usr/bin/env python
from codecs import open  # To use a consistent encoding
from os import path

# Always prefer setuptools over distutils
from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

setup(
    name="polygen",
    version="0.1.0",
    description="Package to access polygen modules",
    long_description="",
    url="",
    author="Anshul Ahluwalia",
    author_email="",
    license="APACHE",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: APACHE License",
        "Operating System :: POSIX",
        "Operating System :: MacOS",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    keywords="computer-vision",
    packages=find_packages(),
    python_requires=">= 3.6",
    install_requires=[],
)