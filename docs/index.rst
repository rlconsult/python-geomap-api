.. Geocoder documentation master file, created by
   sphinx-quickstart on Fri Jul 31 14:40:36 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Geocoder: Simple, Consistent
============================

Release v\ |version|. (:ref:`Installation <install>`)

Simple and consistent geocoding library written in Python.

Many online providers such as Google & Bing have geocoding services,
these providers do not include Python libraries and have different
JSON responses between each other.

It can be very difficult sometimes to parse a particular geocoding provider 
since each one of them have their own JSON schema. 

Here is a typical example of retrieving a Lat & Lng from Google using Python, 
things shouldn't be this hard.

.. code-block:: python

    >>> import requests
    >>> url = 'https://maps.googleapis.com/maps/api/geocode/json'
    >>> params = {'sensor': 'false', 'address': 'Mountain View, CA'}
    >>> r = requests.get(url, params=params)
    >>> results = r.json()['results']
    >>> location = results[0]['geometry']['location']
    >>> location['lat'], location['lng']
    (37.3860517, -122.0838511)

Now lets use Geocoder to do the same task.

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.google('Mountain View, CA')
    >>> g.latlng
    (37.3860517, -122.0838511)

Testimonials
------------

**Tobias Siebenlist**
    Geocoder: great geocoding library by @DenisCarriere. 

**mcbetz**
    Very good companion for Geocoder. Glad to see Python getting more geo libraries for Non-GIS users.


API Documentation
-----------------

If you are looking for information on a specific function, class or method,
this part of the documentation is for you.

.. toctree::
   :maxdepth: 3

   api


Providers
~~~~~~~~~

.. csv-table::
    :header: Provider, Optimal, Access
    :widths: 20, 15, 15

    :ref:`ArcGIS <ArcGIS>`, World
    :ref:`Baidu <Baidu>`, China, API key
    :ref:`Bing <Bing>`, World, API key
    :ref:`CanadaPost <CanadaPost>`, Canada, API key
    :ref:`FreeGeoIP <FreeGeoIP>`, World
    :ref:`Geocoder.ca <Geocoder-ca>`, North America, Rate Limit
    :ref:`GeoNames <GeoNames>`, World, Username
    :ref:`GeoOttawa <GeoOttawa>`, Ottawa
    :ref:`Google <Google>`, World, Rate Limit
    :ref:`HERE <HERE>`, World, API key
    :ref:`Mapbox <Mapbox>`, World, API key
    :ref:`MapQuest <MapQuest>`, World, API key
    :ref:`MaxMind <MaxMind>`, World
    :ref:`OpenCage <OpenCage>`, World, API key
    :ref:`OpenStreetMap <OpenStreetMap>`, World
    :ref:`TomTom <TomTom>`, World, API key
    :ref:`What3Words <What3Words>`, World, API key
    :ref:`Yahoo <Yahoo>`, World
    :ref:`Yandex <Yandex>`, Russia


Contributor Guide
-----------------

If you want to contribute to the project, this part of the documentation is for
you.

.. toctree::
   :maxdepth: 1

   authors

