#!/usr/bin/python
# coding: utf8

"""
Geocoder
~~~~~~~~

Geocoder is a geocoding library, written in python, simple and consistent.

Many online providers such as Google & Bing have geocoding services,
these providers do not include Python libraries and have different
JSON responses between each other.

Consistant JSON responses from various providers.

    >>> g = geocoder.google('New York City')
    >>> g.latlng
    [40.7127837, -74.0059413]
    >>> g.state
    'New York'
    >>> g.json
    ...

"""

__title__ = 'geocoder'
__author__ = 'Denis Carriere'
__author_email__ = 'carriere.denis@gmail.com'
__version__ = '1.3.1'
__license__ = 'MIT'
__copyright__ = 'Copyright (c) 2013-2015 Denis Carriere'

# CORE
from .api import get, yahoo, bing, geonames, mapquest, google  # noqa
from .api import nokia, osm, tomtom, geolytica, arcgis, opencage  # noqa
from .api import maxmind, freegeoip, ottawa, here, baidu, w3w, yandex  # noqa

# EXTRAS
from .api import timezone, elevation, ip, canadapost, reverse, distance, location  # noqa

# CLI
from .cli import cli  # noqa
