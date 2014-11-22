#!/usr/bin/python
# coding: utf8

import geocoder
import pytest
import unittest
from geocoder.location import location

address = '453 Booth Street, Ottawa'
location = 'Ottawa, Ontario'
ip = '74.125.226.99'
repeat = 3
ottawa = (45.4215296, -75.6971930)
toronto = (43.653226, -79.3831843)

def test_entry_points():
    geocoder.ip
    geocoder.osm
    geocoder.bing
    geocoder.nokia
    geocoder.yahoo
    geocoder.google
    geocoder.tomtom
    geocoder.arcgis
    geocoder.geonames
    geocoder.mapquest
    geocoder.timezone
    geocoder.elevation
    geocoder.geolytica
    geocoder.canadapost
    geocoder.timezone
    geocoder.opencage
    geocoder.elevation

def test_google():
    g = geocoder.google(location)
    assert g.ok

def test_google_reverse():
    g = geocoder.google(ottawa, method='reverse')
    assert g.ok

def test_google_timezone():
    g = geocoder.google(ottawa, method='timezone')
    assert g.ok

def test_google_elevation():
    g = geocoder.google(ottawa, method='elevation')
    assert g.ok

def test_bing():
    g = geocoder.bing(location)
    assert g.ok

def test_bing_reverse():
    g = geocoder.bing(ottawa, method='reverse')
    assert g.ok
    
def test_opencage():
    g = geocoder.opencage(location)
    assert g.ok

def test_yahoo():
    g = geocoder.yahoo(location)
    assert g.ok

def test_arcgis():
    g = geocoder.arcgis(location)
    assert g.ok

def test_geolytica():
    g = geocoder.geolytica(address)
    assert g.ok

def test_canadapost():
    g = geocoder.canadapost(address)
    assert g.ok

def test_nokia():
    g = geocoder.nokia(location)
    assert g.ok

def test_osm():
    g = geocoder.osm(location)
    assert g.ok

def test_tomtom():
    g = geocoder.tomtom(location)
    assert g.ok

def test_mapquest():
    g = geocoder.mapquest(location)
    assert g.ok

def test_geonames():
    g = geocoder.geonames(location)
    assert g.ok

def test_ip():
    g = geocoder.ip(ip)
    assert g.ok

def test_location_text():
    l = Location('45.123, -76.123')
    assert l.ok

def test_location_list():
    l = Location([45.123, -76.123])
    assert l.ok
    