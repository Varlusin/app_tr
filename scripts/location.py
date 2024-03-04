from location.models import locationAvailable, Building
from django.db import connection 
from pprint import pprint 
from django.core.serializers import serialize
from django.contrib.gis.db.models.functions import Distance


def run():
    ln = 'hy'
    lat, log = 40.808835552742245, 43.844971060752876
    pnt = f'POINT({log} {lat})'
    poin = Building.objects.get(geometry__contains = pnt).center_point
    obj = Building.objects.annotate(distance=Distance("center_point", poin)).first()

    data ={
        'sity':obj.sity.sity,
        'street':obj.stret.name,
        'adres':obj.adres,
        'distance': obj.distance,
    }
    pprint(data)

    
    pprint(connection.queries)  