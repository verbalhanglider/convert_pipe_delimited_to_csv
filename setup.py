
from setuptools import setup


def _readme():
    with open("README.md", "r") as read_file:
        return read_file.read()

setup(
    name="processingcollection",
    description="A command-line script to process collection list into something to read",
    long_description=_readme(),
    scripts = ['bin/saf-generation.py'],
)
