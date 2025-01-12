from setuptools import setup, Extension

module = Extension(
    "dokkey",
    sources=["main.c"],
    libraries=["user32", "kernel32"],  # Windows libraries
)

setup(
    name="dokkey",
    version="1.0",
    description="A Python module for detecting keyboard events",
    ext_modules=[module],
)
