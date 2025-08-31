#!/usr/bin/env python3
"""
Setup script for FamilyCLI
"""

from setuptools import setup, find_packages
import os

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="familycli",
    version="1.0.0",
    author="AIMLDev726",
    author_email="aistudentlearn4@gmail.com",
    description="A warm, child-safe AI family chat experience in your terminal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AIMLDev726/ai-family-cli",
    project_urls={
        "Bug Tracker": "https://github.com/AIMLDev726/ai-family-cli/issues",
        "Documentation": "https://github.com/AIMLDev726/ai-family-cli/blob/main/README.md",
        "Source Code": "https://github.com/AIMLDev726/ai-family-cli",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Families",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Communications :: Chat",
        "Topic :: Education",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.10",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "familycli=src.main:main",
        ],
    },
    keywords=["ai", "family", "chat", "cli", "children", "safe", "conversation"],
    include_package_data=True,
    zip_safe=False,
)
