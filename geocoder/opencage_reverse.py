#!/usr/bin/python
# coding: utf8

from .base import Base
from .keys import opencage_key
from .opencage import OpenCage
from .location import Location


class OpenCageReverse(OpenCage, Base):
    """
    OpenCage Geocoding Services
    ===========================
    OpenCage Geocoder simple, easy, and open geocoding for the entire world
    Our API combines multiple geocoding systems in the background.
    Each is optimized for different parts of the world and types of requests.
    We aggregate the best results from open data sources and algorithms so you don't have to.
    Each is optimized for different parts of the world and types of requests.

    API Reference
    -------------
    http://geocoder.opencagedata.com/api.html

    OSM Quality (5/6)
    -----------------
    [x] addr:housenumber
    [x] addr:street
    [x] addr:city
    [x] addr:state
    [x] addr:country
    [ ] addr:postal
    """
    provider = 'opencage'
    method = 'reverse'

    def __init__(self, location, **kwargs):
        self.url = 'http://api.opencagedata.com/geocode/v1/json'
        self.location = Location(location).latlng
        self.json = dict()
        self.parse = dict()
        self.content = None
        self.params = {
            'q': self.location,
            'key': kwargs.get('app_id', opencage_key),
        }
        self._initialize(**kwargs)
        self._opencage_catch_errors()

    @property
    def ok(self):
        return bool(self.address)

if __name__ == '__main__':
    latlng = [45.4049053, -75.7077965]
    g = OpenCageReverse(latlng)
    g.debug()