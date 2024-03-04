from unicodedata import category
from django.contrib.auth.models import User 
from grups.models import PopularityCompany, Company
from django.utils import timezone 
from django.db import connection 
from pprint import pprint 

def run(slug = 'basen'):

    bas =(
    Company.objects
    .first()
    )
    for bs in bas.ratings.all():
        print(bs.pk)
        print(bs.post)


    pprint(connection.queries)