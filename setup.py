# SPDX-License-Identifier: Apache-2.0

from setuptools import setup, Extension

with open("README.md", "r") as fh:
    long_description = fh.read()

module = Extension(
    "dokkey",
    sources=["main.c"],
    libraries=["user32", "kernel32"],  # Windows libraries
)

setup(
    name="dokkey",
    version="1.1.0",
    description="Dokkey is a Python package designed to detect keypresses on Windows",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Qiyaya",
    author_email="v2020.bohus.peter@gmail.com",
    url = 'https://github.com/Sekiraw/Dokkey',
    keywords=["KEY", "TRACK"],
    license="Apache-2.0",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    ext_modules=[module],
)
