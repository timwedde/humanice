#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Setup script for humanize."""

import os
import re
import sys
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    with open(os.path.join(here, *parts), "r") as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name="humanice",
    version=find_version("humanice", "__init__.py"),
    description="Python humanization utilities.",
    long_description=open("README.md", "r", encoding="UTF-8").read(),
    # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
    ],
    keywords="humanize time size",
    author="Tim Wedde",
    author_email="timwedde@icloud.com",
    url="http://github.com/timwedde/humanice",
    license="MIT",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    zip_safe=False,
    test_suite="tests",
    tests_require=[],
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points="""
        # -*- Entry points: -*-
    """,
)
