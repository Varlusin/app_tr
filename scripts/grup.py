
from grups.models import ServisCategory, Company
from django.db import connection 
from pprint import pprint 


def run(slug = 'supermarket'):
    grup = (
    Company.objects
    .select_related('category')
    .filter(category__slug = slug)
    .values('names', 'specialcolumn', 'popularity', 'image', 'startwork', 'stopwork', 'slug', 'id')
    )

    for gr in grup:
        print(gr)

    pprint(connection.queries)