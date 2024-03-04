from mayin.models import Typefutur, TypeFuturNavigation
from grups.models import ServisCategory, Company
from django.db import connection 
from pprint import pprint 
def run():
    typ_comp = (
        ServisCategory.objects
        .prefetch_related('cat_comp')
        # .values('slug', 'names_hy', 'cat_comp__names_hy', "cat_comp__specialcolumn_hy")
    )


    for fut in typ_comp:
        print( fut )
        # print(f" {fut.name} ")
        # for fu in fut.cat_fut.all():
        #     print(fu.name , fu.slug)

    pprint(connection.queries)