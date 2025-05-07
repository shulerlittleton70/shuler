from setuptools import setup, find_packages

setup(
    name="shuler_tools",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    author="Shuler Littleton",
    description="A simple library to fetch Cloudability business mappings via Frontdoor auth.",
)
