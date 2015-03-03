#!/usr/bin/env python

from distutils.core import setup

setup(
    name='PyHubble',
    version='0.1',
    author='Javier Aguirre',
    author_email='hello@javaguirre.net',
    packages=['pyhubble'],
    url='https://github.com/javaguirre/pyhubble',
    download_url='https://github.com/javaguirre/pyhubble/tarball/0.1',
    license=open('LICENSE.txt').read(),
    description='A python client for hubble',
    long_description=open('README.txt').read(),
    install_requires=['requests'],
    keywords=['hubble'],
    classifiers=[],
)
