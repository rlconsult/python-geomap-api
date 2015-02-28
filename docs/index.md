Title:   Python Geocoder API
Summary: Home page for Geocoder
Authors: Denis Carriere
Date:    February 20, 2015
base_url: http://geocoder.readthedocs.org

# Geocoder

[![badge][badge]][badge_url] [![travis][travis]][travis_url]

Geocoder is a geocoding library, written in python, simple and consistent.

![][providers]

Many online providers such as Google & Bing have geocoding services,
these providers do not include Python libraries and have different
JSON responses between each other.

Consistant JSON responses from various providers.

```python
>>> g = geocoder.google('New York City')
>>> g.latlng
[40.7127837, -74.0059413]
>>> g.state
'New York'
>>> g.json
...
```

## Features

- Formats (JSON, GeoJSON, OSM, WKT)
- Command Line Interface
- Confidence Score

## Installation

To install Geocoder, simply:

```bash
$ pip install geocoder
```

## Providers

| Global        | Country       | Local     | IP Address    | 
|:--------------|:------------- |:----------|:--------------|
| ArcGIS        | CanadaPost    | GeoOttawa | FreeGeoIP     |
| Bing          | Geocoder.ca   |           | MaxMind       |
| Geonames      |               |           |               |
| Google        |               |           |               |
| HERE          |               |           |               |
| MapQuest      |               |           |               |
| OpenCage      |               |           |               |
| OpenStreetMap |               |           |               |
| TomTom        |               |           |               |
| Yahoo         |               |           |               |



## Twitter

Speak up on Twitter [DenisCarriere] and tell me how you use this Python Geocoder. New updates will be pushed to Twitter Hashtags [python].

## Topic not available?

If you cannot find a topic you are looking for, please feel free to ask me [DenisCarriere] or post them on the [Github Issues Page].

## Feedback

Please feel free to give any feedback on this module. If you find any bugs or any enhancements to recommend please send some of your comments/suggestions to the [Github Issues Page].

## Thanks to

A big thanks to all the people that help contribute:

- [Thanh Ha] - Cleaned up code
- [Mahdi Yusuf] - Promoted by [Pycoders Weekly]
- [Alex Pilon] - Cleaned up code
- [Philip Hubertus] - Provided HERE improvements & documentation
- [Antonio Lima] - Improved code quality and introduced Rate Limits
- [Alexander Lukanin] - Improved Python 3 compatibilty
- [flebel] - Submitted Github Issues
- [patrickyan] - Submitted Github Issues
- [esy] - Submitted Github Issues

[Thanh Ha]: https://twitter.com/zxiiro
[Alex Pilon]: http://alexpilon.ca
[Mahdi Yusuf]: https://twitter.com/myusuf3
[Pycoders Weekly]: https://twitter.com/pycoders
[Philip Hubertus]: https://twitter.com/philiphubs
[Antonio Lima]: https://twitter.com/themiurgo
[Alexander Lukanin]: https://github.com/alexanderlukanin13
[flebel]: https://github.com/flebel
[patrickyan]: https://github.com/patrickyan
[esy]: https://github.com/lambda-conspiracy

[providers]: http://i.imgur.com/vUJKCGl.png
[badge_url]: http://badge.fury.io/py/geocoder
[travis_url]: https://travis-ci.org/DenisCarriere/geocoder
[badge]: https://badge.fury.io/py/geocoder.png
[travis]: https://travis-ci.org/DenisCarriere/geocoder.png?branch=master
[DenisCarriere]: https://twitter.com/DenisCarriere
[python]: https://twitter.com/search?q=%23python
[Github Issues Page]: https://github.com/DenisCarriere/geocoder/issues
