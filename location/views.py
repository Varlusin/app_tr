from django.http import JsonResponse
from django.utils.translation import get_language
from django.utils.translation import gettext as _

from location.utils import find_location
from location.models import CustomerAddresses

from django.db import connection
from pprint import pprint

def __point_serialize(*args, **kwargs):

    def __create_data(dict_geopoint):
        new_dict = dict(map(lambda kv: (kv[0], [kv[1].y, kv[1].x]) if kv[0] == 'geometry' else (kv[0], kv[1]), dict_geopoint.items()))
        return new_dict
    new_list = list(map(lambda x: __create_data(x) , args[0]))
    return new_list


def user_order_adres(request):
    if request.user.is_authenticated:
        old_location = (
                                CustomerAddresses.objects
                                .select_related('custumer')
                                .filter(custumer = request.user)
                                .order_by("-createOrUpdateDate")
                                .values( "id","building", "adres", "geometry")
                                )
        if old_location:
            data =  __point_serialize(list(old_location))
            pprint(connection.queries)
            print(data)
            return JsonResponse({'old_location':data}, status = 200)

    return JsonResponse({})



def getlocation(request):
    longitude = request.GET.get("longitude")
    latitude = request.GET.get("latitude")
    if latitude and longitude:
        page_ln_code = get_language()
        first_search = find_location(longitude, latitude, page_ln_code)
        data, status_code =  first_search.definit_adres()
        pprint(connection.queries)
        print(data)
        return JsonResponse(data, status = status_code)
    
    return JsonResponse({
        'detail': _("The query is missing coordinates.")
    }, status=404, safe=False)


