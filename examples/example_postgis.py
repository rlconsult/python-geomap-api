#!/usr/bin/python

import psycopg2
import psycopg2.extras
import geocoder
import logging
import time

conn = psycopg2.connect("host=kingston.cbn8rngmikzu.us-west-2.rds.amazonaws.com port=5432 dbname=mydb user=addxy password=Denis44C")
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

sql_search = """
SELECT location
FROM kingston
WHERE NOT EXISTS (
    SELECT location
    FROM geocoder
    WHERE kingston.location = geocoder.location AND
    geocoder.provider = 'Google')
"""

sql_exists = """
SELECT location FROM geocoder
WHERE provider=%s AND location=%s
"""

sql_insert = """INSERT INTO geocoder (
status, street_number, locality,
country, route, provider, county,
state, location, address, neighborhood,
postal, quality, sublocality, url, geom)

VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, ST_GeomFromText('POINT({lng} {lat})', 4326))
"""

cur.execute(sql_search)

for item in cur.fetchall():
    
    location = item[0]

    for provider in ['Google', 'MapQuest', 'Bing', 'OSM', 'Nokia', 'TomTom']:
        before = time.time()
        cur.execute(sql_exists, (provider, location))
        if not cur.fetchone():
            g = geocoder.get(location, provider=provider)
            if g.ok:
                fields = (g.status, g.street_number, g.locality,
                    g.country, g.route, g.name, g.county,
                    g.state, g.location, g.address, g.neighborhood,
                    g.postal, g.quality, g.sublocality, g.url
                    )
                cur.execute(sql_insert.format(lng=g.lng, lat=g.lat), fields)
                conn.commit()
                now = str(time.time() - before)[:5] + 's'
                print now, '-', provider, '-', location

#shp2pgsql -s 4326 states > states.sql
#psql -d test -h localhost -U postgres -f states.sql
# normalize_address POSTGIS function
# soundex POSTGIS function