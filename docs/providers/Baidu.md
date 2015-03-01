# Baidu

Baidu Maps Geocoding API is a free open the API, the default quota
one million times / day.

## Examples

**Basic geocoding**

```python
>>> import geocoder
>>> g = geocoder.baidu('中国')
>>> g.json
...
```

## Parameters

- `location`: Your search location you want geocoded.
- `key`: Baidu API key.
- `referer`: Baidu API referer website.

## References

- [API Reference](http://developer.baidu.com/map/index.php?title=webapi/guide/webservice-geocoding)
- [Get Baidu key](http://lbsyun.baidu.com/apiconsole/key)