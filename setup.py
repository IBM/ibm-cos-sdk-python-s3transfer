#!/usr/bin/env python
import os
import re

from setuptools import find_packages, setup

ROOT = os.path.dirname(__file__)
VERSION_RE = re.compile(r'''__version__ = ['"]([a-z0-9.]+)['"]''')


requires = [
    'ibm-cos-sdk-core==2.13.5',
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
    install_requires=requires,
    license="Apache License 2.0",
    python_requires=">= 3.8",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)
