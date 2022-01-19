#! /usr/bin/env python3

from setuptools import setup


setup(
    name='newslib',
    version='latest',
    use_scm_version={
        "local_scheme": "node-and-timestamp"
    },
    setup_requires=['setuptools_scm'],
    author='HOMEINFO - Digitale Informationssysteme GmbH',
    author_email='<info@homeinfo.de>',
    maintainer='Richard Neumann',
    maintainer_email='<r.neumann@homeinfo.de>',
    install_requires=[
        'ferengi',
        'filedb',
        'hinews',
        'mdb',
        'newslib',
        'peewee',
        'peeweeplus',
        'wsgilib'
    ],
    packages=['newslib'],
    description='Multi-source news API.')
