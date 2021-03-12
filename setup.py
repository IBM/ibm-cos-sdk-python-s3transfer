#!/usr/bin/env python
import os
import re

from setuptools import setup, find_packages


ROOT = os.path.dirname(__file__)
VERSION_RE = re.compile(r'''__version__ = ['"]([a-z0-9.]+)['"]''')


requires = [
    'ibm-cos-sdk-core==2.10.0',
]


def get_version():
    init = open(os.path.join(ROOT, 'ibm_s3transfer', '__init__.py')).read()
    return VERSION_RE.search(init).group(1)


setup(
    name='ibm-cos-sdk-s3transfer',
    version=get_version(),
    description='IBM S3 Transfer Manager',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='IBM',
    author_email='',
    url='https://github.com/IBM/ibm-cos-sdk-python-s3transfer',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    python_requires='~=3.6',
    install_requires=requires,
    license="Apache License 2.0",
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ),
)
