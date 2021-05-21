#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""PIP setup script for the SKA SDP Operator Interface package."""

import setuptools

with open("README.md", "r") as file:
    LONG_DESCRIPTION = file.read()

setuptools.setup(
    name="ska-sdp-opinterface",
    description="SKA SDP Operator Interface",
    author="SKA Sim Team",
    license="License :: OSI Approved :: BSD License",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/ska-telescope/sdp/ska-sdp-opinterface",
    package_dir={"": "src"},
    packages=setuptools.find_packages("src"),
    package_data={"ska_sdp_opinterface": ["static/*", "templates/*"]},
    install_requires=[
        "flask",
        "ska-sdp-config>=0.2.1",
    ],
    setup_requires=["pytest-runner"],
    tests_require=[
        "pylint2junit",
        "pytest",
        "pytest-cov",
        "pytest-pylint",
    ],
    dependency_links=[
        "https://nexus.engageska-portugal.pt/repository/pypi/simple/",
    ],
    zip_safe=False,
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Astronomy",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: BSD License",
    ],
)
