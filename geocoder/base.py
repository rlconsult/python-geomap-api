#!/usr/bin/python
# coding: utf8

import requests
import sys
import json
from collections import defaultdict
from haversine import haversine


class Base(object):
    _exclude = ['parse', 'json', 'url', 'attributes', 'help', 'debug', 'short_name',
                'api', 'content', 'params', 'status_code', 'street_number', 'method',
                'api_key', 'key', 'id', 'x', 'y', 'latlng', 'headers', 'timeout',
                'geometry', 'wkt','locality', 'province','rate_limited_get', 'osm',
                'route', 'properties','geojson','tree','error']
    _attributes = []
    error = None
    status_code = None
    headers = {}
    params = {}
    housenumber = ''
    address = ''
    lat = ''
    lng = ''
    street = ''
    city = ''
    state = ''
    postal = ''
    country = ''
    population = ''

    def __repr__(self):
        return "<[{0}] {1} - {2} [{3}]>".format(
            self.status, 
            self.provider.title(), 
            self.method.title(), 
            self.address.encode('utf-8')
        )

    @staticmethod
    def rate_limited_get(url, **kwargs):
        return requests.get(url, **kwargs)

    def _connect(self, **kwargs):
        self.status_code = 'Unknown'
        self.timeout = kwargs.get('timeout', 5.0)
        self.proxies = kwargs.get('proxies', '')
        try:
            r = self.rate_limited_get(
                self.url, 
                params=self.params, 
                headers=self.headers, 
                timeout=self.timeout,
                proxies=self.proxies
            )
            self.status_code = r.status_code
            self.url = r.url
            self.content = r.json()
        except KeyboardInterrupt:
            sys.exit()
        except:
            self.status_code = 404
            self.error = 'ERROR - URL Connection'

        # Open JSON content from Request connection
        if self.status_code == 200:
            try:
                self.content = r.json()
            except:
                self.status_code = 400
                self.error = 'ERROR - JSON Corrupted'
                self.content = r.content

    def _initialize(self, **kwargs):
        self.json = dict()
        self.parse = self.tree()
        self.content = None
        self._connect(url=self.url, params=self.params, **kwargs)
        self._build_tree(self.content)
        self._exceptions()
        self._json()

    def _json(self):
        for key in dir(self):
            if bool(not key.startswith('_') and key not in self._exclude):
                self._attributes.append(key)
                value = getattr(self, key)
                if value:
                    self.json[key] = value

        # Add OK attribute even if value is "False"
        self.json['ok'] = self.ok

    def debug(self):
        print(json.dumps(self.parse, indent=4))
        print(json.dumps(self.json, indent=4))

    def tree(self): return defaultdict(self.tree)

    def _build_tree(self, content):
        if content:
            for key, value in content.items():
                self.parse[key] = value

    @property
    def status(self):
        if self.ok:
            return 'OK'
        elif self.error:
            return self.error
        elif self.status_code == 404:
            return 'ERROR - URL Connection'
        elif not self.address:
            return 'ERROR - No results found'
        elif not bool(self.lng and self.lat):
            return 'ERROR - No Geometry'

    def _get_bbox(self, south, west, north, east):
        # South Latitude, West Longitude, North Latitude, East Longitude
        self.south = south
        self.west = west
        self.north = north
        self.east = east

        # Bounding Box Corners
        self.northeast = [north, east]
        self.northwest = [north, west]
        self.southwest = [south, west]
        self.southeast = [south, east]

        # GeoJSON bbox
        self.westsouth = [west, south]
        self.eastnorth = [east, north]
        
        if bool(south and east and north and west):
            bbox = {
                'northeast': [north, east],
                'southwest': [south, west],
            }
            return bbox
        return {}

    @property
    def confidence(self):
        if self.bbox:
            # Units are measured in Kilometers
            distance = haversine(self.northeast, self.southwest)
            for score, maximum in [
                (10, 0.25),
                (9, 0.5),
                (8, 1),
                (7, 5),
                (6, 7.5),
                (5, 10),
                (4, 15),
                (3, 20),
                (2, 25)]:
                if distance < maximum:
                    return score
                if distance >= 25:
                    return 1
        # Cannot determine score
        return 0

    @property
    def bbox(self):
        return {}

    @property
    def ok(self):
        if bool(self.lng and self.lat):
            return True
        else:
            return False

    @property
    def geometry(self):
        if self.ok:
            geometry = {
                'type': 'Point',
                'coordinates': [self.lng, self.lat],
            }
            return geometry
        return {}

    @property
    def osm(self):
        osm = dict()
        if self.ok:
            osm['x'] = self.x
            osm['y'] = self.y
            if self.housenumber:
                osm['addr:housenumber'] = self.housenumber
            if self.street:
                osm['addr:street'] = self.street
            if self.city:
                osm['addr:city'] = self.city
            if self.state:
                osm['addr:state'] = self.state
            if self.country:
                osm['addr:country'] = self.country
            if self.postal:
                osm['addr:postal'] = self.postal
            if self.population:
                osm['population'] = self.population
        return osm

    @property
    def properties(self):
        properties = self.json
        if self.bbox:
            del properties['bbox']
        return properties

    @property
    def geojson(self):
        feature = {
            'type': 'Feature',
            'properties': self.properties,
        }
        if self.geometry:
            feature['geometry'] = self.geometry
        if self.bbox:
            feature['bbox'] = self.westsouth + self.eastnorth
        return feature

    @property
    def wkt(self):
        if self.ok:
            return 'POINT({x} {y})'.format(x=self.x, y=self.y)
        return '' 

    @property
    def latlng(self):
        if self.ok:
            return [self.lat, self.lng]
        return []

    @property
    def y(self):
        return self.lat

    @property
    def x(self):
        return self.lng

    @property
    def locality(self):
        return self.city

    @property
    def province(self):
        return self.state

    @property
    def street_number(self):
        return self.housenumber

    @property
    def route(self):
        return self.street

