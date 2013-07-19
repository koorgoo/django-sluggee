#!/usr/bin/env python
from setuptools import setup

setup(
    name="django-sluggee",
    version="0.1",
    description="Russian slugifier for Django",
    long_description="Django's 'slugify' wrapper to slugify russian easily.",
    keywords="django, slug",
    author="Dima Kurguzov",
    author_email="koorgoo@gmail.com",
    url="https://github.com/koorgoo/djangl-sluggee/",
    license="MIT",
    packages=["sluggee"],
    zip_safe=False,
    install_requires=[],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3"
    ],
)
