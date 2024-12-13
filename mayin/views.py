from django.shortcuts import render
from django.utils.translation import gettext as _ 
from grups.models import ServisCategory, Company
from location.models import CustomerAddresses
from users.models import CustomUser

from django.db import connection
from pprint import pprint

# def get_old_locations(user_mile):
#     old_location = (
#         CustomerAddresses.objects
#         .select_related('order_adres')
#     )


def index(request):
    context = {}
    grup = Company.objects.all()
    
    context['title'] = _('Home')
    context['grup'] = grup
    # pprint(connection.queries)
    # print(context)
    return render(request, 'mayin/index.html', context)


def company(request, slug):
    grup = (
    Company.objects
    .select_related('category')
    .filter(category__slug = slug)
    .values('names', 'specialcolumn', 'popularity', 'image', 'startwork', 'stopwork', 'slug', 'id')
    )
    context = {
        "title": _('Home'),
        'grup' : grup,
    }    
    return render(request, 'mayin/index.html', context)



