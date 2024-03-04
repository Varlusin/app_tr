from location.models import locationAvailable
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.geos import Polygon, MultiPolygon
from pprint import pprint
import re
import requests
import urllib.request
from urllib.request import urlopen
import ast


def run():
    myheader={}
    myheader['User-Agent']='Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Mobile Safari/537.36'
    urll='https://yandex.ru/maps/geo/1508541974/?ll=43.828915%2C40.722227&z=14.19'
    r=urllib.request.Request(urll,headers=myheader)
    esp=urllib.request.urlopen(r)
    html=esp.read().decode('utf-8')
    data=re.findall('"type":"Polygon","coordinates":(.*?)}]},"', html)
    df = data[0][3:-3]
    df = df.replace(',', ' ')
    df = df.replace('] [',', ')
    col = re.findall('(.*?),', df)[0]
    df = 'MULTIPOLYGON((('+df+', ' + col + ')))'
    pnt = GEOSGeometry(df, srid=4326)
    sity = locationAvailable.objects.get(pk = 8)
    sity.location = pnt
    sity.sity = 'azatan'
    sity.save()
