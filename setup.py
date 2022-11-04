#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="Anderson",
    author_email='chaup001@umn.edu',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Project to simulate stock trading",
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='stocks_project',
    name='stocks_project',
    packages=find_packages(include=['stocks_project', 'stocks_project.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/achauphan/stocks_project',
    version='0.1.0',
    zip_safe=False,
)
