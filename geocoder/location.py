#!/usr/bin/python
# coding: utf8
import re
from collections import namedtuple


class Location(object):
    """ Location container """
    lat = None
    lng = None

    def __init__(self, location):
        self._check_input(location)

    @property
    def ok(self):
        if self.latlng:
            return True
        else:
            return False

    def _convert_float(self, number):
        try:
            return float(number)
        except ValueError:
            return None

    def _check_input(self, location):
        # Checking for a String
        if isinstance(location, str):
            expression = r"[-]?\d+[.]?[-]?[\d]+"
            pattern = re.compile(expression)
            match = pattern.findall(location)
            if len(match) == 2:
                lat, lng = match
                self._check_for_list([lat, lng])

        # Checking for List of Tuple
        if isinstance(location, (list, tuple)):
            self._check_for_list(location)

        # Checking for Dictionary
        elif isinstance(location, dict):
            self._check_for_dict(location)

        # Checking for a Geocoder Class
        elif hasattr(location, 'latlng'):
            self.lat, self.lng = location.latlng

    def _check_for_list(self, location):
        # Standard LatLng list or tuple with 2 number values
        if len(location) == 2:
            lat = self._convert_float(location[0])
            lng = self._convert_float(location[1])
            condition_1 = isinstance(lat, float)
            condition_2 = isinstance(lng, float)

            # Check if input are Floats
            if bool(condition_1 and condition_2):
                condition_3 = lat <= 90 and lat >= -90
                condition_4 = lng <= 180 and lng >= -180

                # Check if inputs are within the World Geographical
                # boundary (90,180,-90,-180)
                if bool(condition_3 and condition_4):
                    self.lat = lat
                    self.lng = lng
                    return self.lat, self.lng
                else:
                    self.error = 'ERROR - Lat & Lng are not '\
                                 'within the world\'s geographical boundary.'
            else:
                self.error = 'ERROR - Lat & Lng are not floats.'

    def _check_for_dict(self, location):
        # Standard LatLng list or tuple with 2 number values
        if bool('lat' in location and 'lng' in location):
            lat = location.get('lat')
            lng = location.get('lng')
            self._check_for_list([lat, lng])

        if bool('y' in location and 'x' in location):
            lat = location.get('y')
            lng = location.get('x')
            self._check_for_list([lat, lng])

    @property
    def latlng(self):
        condition1 = isinstance(self.lat, float)
        condition2 = isinstance(self.lng, float)
        if bool(condition1 and condition2):
            latlng = namedtuple('LatLng', ['lat', 'lng'])
            return latlng(self.lat, self.lng)

    @property
    def xy(self):
        condition1 = isinstance(self.lat, float)
        condition2 = isinstance(self.lng, float)
        if bool(condition1 and condition2):
            xy = namedtuple('XY', ['x', 'y'])
            return xy(self.lng, self.lat)

    def __str__(self):
        if self.ok:
            return '{0}, {1}'.format(self.lat, self.lng)
        else:
            return ''

if __name__ == '__main__':
    l = Location([])
