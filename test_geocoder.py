#!/usr/bin/python
# coding: utf8

import geocoder


address = '453 Booth Street, Ottawa'
location = 'Ottawa, Ontario'
city = 'Ottawa'
ip = '74.125.226.99'
china = '中国'
repeat = 3
ottawa = (45.4215296, -75.6971930)
toronto = (43.653226, -79.3831843)


def test_entry_points():
    geocoder.ip
    geocoder.osm
    geocoder.bing
    geocoder.here
    geocoder.baidu
    geocoder.yahoo
    geocoder.google
    geocoder.tomtom
    geocoder.arcgis
    geocoder.geonames
    geocoder.mapquest
    geocoder.timezone
    geocoder.maxmind
    geocoder.elevation
    geocoder.freegeoip
    geocoder.geolytica
    geocoder.timezone
    geocoder.opencage
    geocoder.elevation
    geocoder.canadapost

"""
Server Down

def test_freegeoip():
    g = geocoder.freegeoip(ip)
    assert g.ok
"""


def test_maxmind():
    g = geocoder.maxmind(ip)
    assert g.ok


def test_baidu():
    g = geocoder.baidu(china)
    assert g.ok


def test_google():
    g = geocoder.google(location)
    assert g.ok
    assert g.city == city


def test_google_reverse():
    g = geocoder.google(ottawa, method='reverse')
    assert g.ok


def test_google_timezone():
    g = geocoder.google(ottawa, method='timezone')
    assert g.ok


def test_google_elevation():
    g = geocoder.google(ottawa, method='elevation')
    assert g.ok

"""
Bing causing issues
First request is rarely successful

def test_bing():
    g = geocoder.bing(location)
    g = geocoder.bing(location)
    assert g.ok
    assert g.city == city


def test_bing_reverse():
    # First request rarely successful
    g = geocoder.bing(ottawa, method='reverse')
    g = geocoder.bing(ottawa, method='reverse')
    assert g.ok
"""

def test_opencage():
    g = geocoder.opencage(location)
    assert g.ok


def test_opencage_reverse():
    g = geocoder.opencage(ottawa, method='reverse')
    assert g.ok


def test_yahoo():
    g = geocoder.yahoo(location)
    assert g.ok
    assert g.city == city


def test_arcgis():
    g = geocoder.arcgis(location)
    assert g.ok


def test_geolytica():
    g = geocoder.geolytica(address)
    assert g.ok


def test_canadapost():
    g = geocoder.canadapost(address)
    assert g.ok


def test_here():
    g = geocoder.here(location)
    assert g.ok
    assert g.city == city


def test_osm():
    g = geocoder.osm(location)
    assert g.ok
    assert g.city == city


def test_tomtom():
    g = geocoder.tomtom(location)
    assert g.ok
    assert g.city == city


def test_mapquest():
    g = geocoder.mapquest(location)
    assert g.ok
    assert g.city == city


def test_geonames():
    g = geocoder.geonames(city)
    assert g.ok
