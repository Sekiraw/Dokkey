from setuptools import setup, Extension
import pypandoc

module = Extension(
    "dokkey",
    sources=["main.c"],
    libraries=["user32", "kernel32"],  # Windows libraries
)

description = ""
try:
    description=pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    description=open('README.md').read()

setup(
    name="dokkey",
    version="1.0.3",
    description=description,
    author="Peter Bohus",
    author_email="v2020.bohus.peter@gmail.com",
    ext_modules=[module],
)
