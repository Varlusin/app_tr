from django.contrib.postgres.search import SearchVector, SearchQuery
from location.models import locationAvailable, Street
from django.db import connection
from django.db.models import Q
from pprint import pprint
from unidecode import unidecode
import unicodedata

def get_len_code(txt):
    if 'ARMENIAN' in unicodedata.name(txt[0]):
        return f"""_hy = '{txt}'"""
    elif 'CYRILLIC' in unicodedata.name(txt[0]):
        return f"""_ru = '{txt}'"""
    elif 'LATIN' in unicodedata.name(txt[0]):
        return f"""_en = '{txt}'"""
    else: return f""" = '{unidecode(txt)}' """


# def run():
#     txt = input('search:  ')
#     result = [elem.capitalize() for elem in txt.split()]
#     q_query = f""" Q(sity{get_len_code(result[0])})"""
#     print(q_query)
#     obj = (locationAvailable.objects.
#            filter(eval(q_query))
#            )

#     print(obj.count())

#     pprint(connection.queries)
    

def run():
    sity = 'Gyumri'
    stret = 'Yerevanyan Highway'
    adres = '142'

    obj = (locationAvailable.objects
           .annotate(
               search = SearchVector('sity_en', 'street__name_en', 'buildings__adres' )
           )
           .filter(search=SearchQuery(sity | stret | adres))
    )

    print(obj.count())

    pprint(connection.queries)