#!/usr/bin/python
# coding: utf8
from setuptools import setup
import os
import codecs
import re


def find_version(*file_paths):
    # Open in Latin-1 so that we avoid encoding errors.
    # Use codecs.open for Python 2 compatibility
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, *file_paths), 'r', 'latin1') as f:
        version_file = f.read()

    # The version line must have the form
    # __version__ = 'ver'
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

requirements_file = "requirements.txt"
requirements = [pkg.strip() for pkg in open(requirements_file).readlines()]

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst') + "\n"
except(IOError, ImportError):
    with codecs.open('README.md', encoding='utf-8') as f:
        long_description = f.read() + "\n"

setup(
    name='geocoder',
    version=find_version('geocoder', '__init__.py'),
    description="Geocoder is a geocoding library, written in python,"
                " simple and consistent.",
    long_description=long_description,
    author='Denis Carriere',
    author_email='carriere.denis@gmail.com',
    url='https://github.com/DenisCarriere/geocoder',
    download_url='https://github.com/DenisCarriere/geocoder/tarball/master',
    license=open('LICENSE').read(),
    entry_points='''
        [console_scripts]
        geocode=geocoder.cli:cli
    ''',
    packages=['geocoder'],
    package_data={'': ['LICENSE', 'README.md']},
    package_dir={'geocoder': 'geocoder'},
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='geocoder arcgis tomtom opencage google bing here',
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Scientific/Engineering :: GIS',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ),
)
