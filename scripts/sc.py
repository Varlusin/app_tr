from django.contrib.auth.models import User 
from grups.models import PopularityCompany, Company
from django.utils import timezone 
from django.db import connection 
from pprint import pprint 

def run():
    posts = Company.objects.all()

    posts.update(popularity = 2.5)

    print(connection.queries)