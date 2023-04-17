from setuptools import setup, find_packages

setup(
    name="kagiapi",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    author="Vladimir Prelovac",
    author_email="vlad@kagi.com",
    description="A Python package for Kagi Search API",
    url="https://github.com/kagisearch/kagiapi",
)