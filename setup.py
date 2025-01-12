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
    version="1.0.6",
    long_description=long_description, 
    long_description_content_type="text/markdown",
    author="Peter Bohus",
    author_email="v2020.bohus.peter@gmail.com",
    license="Apache-2.0",
    ext_modules=[module],
)
