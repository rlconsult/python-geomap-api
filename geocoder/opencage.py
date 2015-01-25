#!/usr/bin/python
# coding: utf8

from base import Base
from keys import opencage_key


class OpenCage(Base):
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

    OSM Quality (6/6)
    -----------------
    [x] addr:housenumber
    [x] addr:street
    [x] addr:city
    [x] addr:state
    [x] addr:country
    [x] addr:postal
    
    Attributes (27/29)
    ------------------
    [x] DMS
    [x] Maidenhead
    [x] Mercator
    [ ] accuracy
    [x] address
    [x] bbox
    [x] callingcode
    [x] city
    [x] city_district
    [x] confidence
    [x] country
    [x] county
    [x] geohash
    [x] housenumber
    [x] lat
    [x] license
    [x] lng
    [x] location
    [x] mgrs
    [x] neighborhood
    [x] ok
    [x] postal
    [x] provider
    [ ] quality
    [x] state
    [x] status
    [x] street
    [x] town
    [x] w3w
    """
    provider = 'opencage'
    method = 'geocode'

    def __init__(self, location, **kwargs):
        self.url = 'http://api.opencagedata.com/geocode/v1/json'
        self.location = location
        self.params = {
            'q': location,
            'key': kwargs.get('key', opencage_key),
        }
        self._initialize(**kwargs)
        self._opencage_catch_errors()

    def _opencage_catch_errors(self):
        if self.content:
            status = self.content.get('status')
            if status:
                code = status.get('code')
                message = status.get('message')
                if code:
                    self.error = message

    def _exceptions(self):
        # Build intial Tree with results
        if self.parse['results']:
            self._build_tree(self.parse['results'][0])
        licenses = self.parse['licenses']
        if licenses:
            self.parse['licenses'] = licenses[0]
    
    @property
    def lat(self):
        return self.parse['geometry']['lat']

    @property
    def lng(self):
        return self.parse['geometry']['lng']

    @property
    def address(self):
        return self.parse['formatted']

    @property
    def housenumber(self):
        return self.parse['components']['house_number']

    @property
    def street(self):
        return self.parse['components']['road']

    @property
    def neighborhood(self):
        neighbourhood = self.parse['components']['neighbourhood']
        if neighbourhood:
            return neighbourhood
        elif self.suburb:
            return self.suburb
        elif self.city_district:
            return self.city_district

    @property
    def suburb(self):
        return self.parse['components']['suburb']

    @property
    def city_district(self):
        return self.parse['components']['city_district']

    @property
    def city(self):
        city = self.parse['components']['city']
        if city:
            return city
        elif self.town:
            return self.town
        elif self.county:
            return self.county

    @property
    def town(self):
        return self.parse['components']['town']

    @property
    def county(self):
        return self.parse['components']['county']

    @property
    def state(self):
        return self.parse['components']['state']

    @property
    def country(self):
        return self.parse['components']['country_code']

    @property
    def postal(self):
        return self.parse['components']['postcode']

    @property
    def confidence(self):
        return self.parse['confidence']

    @property
    def w3w(self):
        return self.parse['what3words']['words']

    @property
    def mgrs(self):
        return self.parse['annotations']['MGRS']

    @property
    def geohash(self):
        return self.parse['annotations']['geohash']

    @property
    def callingcode(self):
        return self.parse['annotations']['callingcode']

    @property
    def Maidenhead(self):
        return self.parse['annotations']['Maidenhead']

    @property
    def DMS(self):
        return self.parse['DMS']

    @property
    def Mercator(self):
        return self.parse['Mercator']

    @property
    def license(self):
        return self.parse['licenses']

    @property
    def status(self):
        return self.parse['status']

    @property
    def bbox(self):
        south = self.parse['southwest']['lat']
        north = self.parse['northeast']['lat']
        west = self.parse['southwest']['lng']
        east = self.parse['northeast']['lng']
        return self._get_bbox(south, west, north, east)

if __name__ == '__main__':
    g = OpenCage('1552 Payette dr., Ottawa')
    g.debug()