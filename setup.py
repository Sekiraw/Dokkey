from setuptools import setup, Extension

module = Extension(
    "dokkey",
    sources=["main.c"],
    libraries=["user32", "kernel32"],  # Windows libraries
)

setup(
    name="dokkey",
    version="1.0.2",
    description="A Python module for detecting keyboard events",
    author="Peter Bohus",
    author_email="v2020.bohus.peter@gmail.com",
    ext_modules=[module],
)
