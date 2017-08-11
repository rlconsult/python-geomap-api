GeoNames
========

GeoNames is mainly using REST APIs. It offers 40 different webservices, listed with examples in its `overview <http://www.geonames.org/export/ws-overview.html>`_

Geocoder provides you with various methods for different purposes:

- (geocode) retrieve GeoNames's geocoded data from a query string, and various filters
- (details) retrieve all geonames data for a given *geonames_id*
- (children) retrieve the hierarchy of a given *geonames_id*
- (hierarchy) retrieve all children for a given *geonames_id*

Geocoding
~~~~~~~~~

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.geonames('New York', key='<USERNAME>')
    >>> g.address
    "New York City"
    >>> g.geonames_id
    5128581
    >>> g.description
    "city, village,..."
    >>> g.population
    8175133

Geonames web service support a lot of filters that you can use to refine your query. Here follows a list from the `official documentation <http://www.geonames.org/export/geonames-search.html>`_

- 'name', 'name_equals', 'name_startsWith', 
- 'maxRows', 'startRow',
- 'country', 'countryBias', 'continentCode',
- 'adminCode1', 'adminCode2', 'adminCode3',
- 'featureClass', 'featureCode',
- 'lang', 'type', 'style', 'fuzzy',
- 'isNameRequired', 'tag', 'operator', 'charset'
- 'east', 'west', 'north', 'south'

They are all supported 

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.geonames('New York', key='<USERNAME>', featureClass='A')
    >>> g.address
    "New York"
    >>> g.geonames_id
    5128638
    >>> g.description
    "first-order administrative division"
    >>> g.population
    19274244

Proximity
---------

Geomanes allows the extra parameters 'east', 'west', 'north', 'south' to restrict the query to the therefore defined box. They provide the functionnality 'proximity' that can be found on some other providers (e.g Mapbox)


.. code-block:: python

    >>> g = geocoder.geonames('Paris', key='<USERNAME>', east=-96.0, west=-95.0, north=33.5, south=33.0)
    >>> g.address
    'Kosciusko'
    >>> g.country
    'United States'


For consistency purpose, geocoder also accepts a 'bbox' parameter. Follows an example where google provider is used first, and the resulting bbox is passed to make a query to geonames:


.. code-block:: python

    >>> location = 'Ontario, Ottawa'
    >>> google_result = geocoder.google(location, key='YOUR KEY')
    >>> google_result.address
    'Ottawa, ON, Canada'
    >>> google_result.bbox
    {'northeast': [45.5375801, -75.2465979], 'southwest': [44.962733, -76.35391589999999]}
    >>> g = geocoder.geonames(location, key='YOUR USERNAME', bbox=google_result.bbox)
    >>> g.address
    'Ottawa'


Multiple values for some parameters
-----------------------------------

As pointed out in Geonames specs, the search (geocoding) service accepts multiple values for some parameters (e.g. 'country', 'featureClass' and 'featureCode')


This is also supported by Geocoder, which will expect in these cases an array instead of the normal string.


.. code-block:: python

    >>> g = geocoder.geonames('Paris', key='<USERNAME>', maxRows=5, country=['FR', 'US'])
    >>> print([(r.address, r.country) for r in g])
    [('Paris', 'France'), ('Paris', 'United States'), ('Paris', 'France'), ('Paris', 'United States'), ('Paris', 'United States')]


Details (inc. timezone, bbox)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This method requires a valid *geonames_id*, which you can get with the geocode method. It will fetchs all available information from geonames, including timezone and bbox.


.. code-block:: python

    g = geocoder.geonames(6094817, method='details', key='<USERNAME>')

    >>> g.lat
    "45.41117"
    >>> g.lng
    "-75.69812"
    >>> g.geonames_id
    6094817
    >>> g.address
    "Ottawa"
    >>> g.feature_class
    "P"
    >>> g.class_description
    "city, village,..."
    >>> g.code
    "PPLC"
    >>> g.description
    "capital of a political entity"
    >>> g.continent
    "NA"
    >>> g.country_geonames_id
    "6251999"
    >>> g.country_code
    "CA"
    >>> g.country
    "Canada"
    >>> g.state
    "Ontario"
    >>> g.state_code
    "08"
    >>> g.state_geonames_id
    "6093943"
    >>> g.admin2
    ""
    >>> g.admin3
    ""
    >>> g.admin4
    ""
    >>> g.admin5
    ""
    >>> g.population
    812129
    >>> g.srtm3
    71
    >>> g.wikipedia
    "en.wikipedia.org/wiki/Ottawa"
    >>> g.timeZoneId
    "America/Toronto"
    >>> g.timeZoneName
    "America/Toronto"
    >>> g.rawOffset
    -5
    >>> g.dstOffset
    -4
    >>> g.bbox
    {'northeast': [45.58753415000007, -75.07957784899992], 'southwest': [44.962202955000066, -76.35400795899994]}

Children and Hierarchy
~~~~~~~~~~~~~~~~~~~~~~~

These two web services expect a geonames_id, which means you first need to make geocode your location. They will return multiple results most of the time, which you can access as described in the :ref:`results page <results>`.

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.geonames('New York', key='<USERNAME>', method='children')
    >>> c = geocoder.geonames(g.geoname_id, key='<USERNAME>', method='children')
    >>> c.geojson
    ...
    >>> h = geocoder.geonames(g.geoname_id, key='<USERNAME>', method='hierarchy')
    >>> h.geojson
    ...


Command Line Interface
----------------------

.. code-block:: bash

    $ geocode 'New York City' --provider geonames

Environment Variables
---------------------

To make sure your API key is store safely on your computer, you can define that API key using your system's environment variables.

.. code-block:: bash

    $ export GEONAMES_USERNAME=<Secret Username>

Parameters
----------

- `location`: Your search location you want geocoded.
- `key`: (required) geonames *username" needs to be passed with each request.
- `method`: (default=geocode) Use the following:

  - geocode
  - details
  - timezone
  - children
  - hierarchy

References
----------

- `GeoNames REST Web Services <http://www.geonames.org/export/web-services.html>`_
