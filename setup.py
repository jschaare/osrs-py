#!/usr/bin/env python3

import os
from setuptools import setup

directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="osrs_py",
    version="0.0.1",
    description="OSRS python interface",
    author="jschaare",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["osrs"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=["requests", "yarl", "tinydb"],
    python_requires=">=3.8",
    extras_require={
        "testing": ["pytest"],
    },
    include_package_data=True,
)
