
from django.http import JsonResponse
# from location.utils import search_results, SearchResult

from django.shortcuts import render
from location.forms import  LocationSearchForm
from location.models import Street, locationAvailable, Building
from django.contrib.postgres.search import  TrigramSimilarity, TrigramDistance
from django.contrib.postgres.search import (SearchVector, 
                                            SearchQuery, 
                                            SearchRank, 
                                            TrigramSimilarity,
                                            TrigramDistance)

from django.contrib.postgres.search import SearchHeadline, SearchQuery



from django.db import connection 
from pprint import pprint

from unidecode import unidecode
import unicodedata

def _get_len_code(txt):
    unicodeNane = unicodedata.name(txt[0])
    if "ARMENIAN" in unicodeNane:
        return "_hy"
    elif "CYRILLIC" in unicodeNane:
        return "_ru"
    elif "LATIN" in unicodeNane:
        return "_en"
    else:
        return f""" = '{unidecode(txt)}' """


def search_location(request):

    form = LocationSearchForm
    
    context = {
        'form':form
    }

    if 'q' in request.GET:
        form = LocationSearchForm(request.GET)
        if form.is_valid():
            q=form.cleaned_data['q']
            search_leng = _get_len_code(txt=q)
            res_sity = (
                locationAvailable.objects
                .annotate(similarity=TrigramSimilarity(f"sity{search_leng}", q),)
            # .filter(similarity__gt=0.3)
                .order_by('-similarity')
                .values('id', f'sity', 'similarity')[:1]
            )
            ressity = list(res_sity)
            print(q)
            print(ressity)
            if ressity[0]['similarity'] >=0.1:
                res_str = (
                    Street.objects
                    .filter(sity__id =ressity[0]['id'])
                    .annotate(similarity=TrigramSimilarity(f"name{search_leng}", q),)
                    .filter(similarity__gt=0.1)
                    .order_by('-similarity')[:10]
                    # .values('building_id', 'name', 'similarity', 'buildings__adres' )
                    .prefetch_related('buildings')

                )

            # for i in res_str:
            #     for j in i.buildings.all():
            #         print(j)

            
            context = {
                'form':form,
                'result':res_str,
                # 'result': result
            }

            pprint(connection.queries)
            return render(request, 'location/index.html', context=context )


    return render(request, 'location/index.html', context=context )
















def src_loc(request):
    # if 'q' in request.GET:
    #     query = request.GET.get('q')
    #     resp = {
    #         'adr':search_results(query_adres=query)
    #     }
    resp = {}
    return JsonResponse(resp)













# def search_location(request):

#     form = LocationSearchForm
    
#     context = {
#         'form':form
#     }

#     if 'q' in request.GET:
#         form = LocationSearchForm(request.GET)
#         if form.is_valid():
#             q=form.cleaned_data['q']

#             result = (Building.objects
#                       .annotate(distance = TrigramDistance ('stret__name_en', q),)
#                       .filter(distance__gte = 0.3)
#                       .order_by('distance')
#                       .select_related('sity')
#                       .select_related('stret')
#                       .values('id', 'sity__sity', 'stret__name', 'adres')
                      
#                              )
            
#             context = {
#                 'form':form,
#                 'result':result,
#             }
#             # cont = {
#             #     'result':list(result),
#             # }
#             pprint(connection.queries)
#             # return JsonResponse(cont)
#             return render(request, 'location/index.html', context=context )


#     return render(request, 'location/index.html', context=context )












# def search_location(request):
#     form = LocationSearchForm
    
#     context = {
#         'form':form
#     }

#     if 'q' in request.GET:
#         form = LocationSearchForm(request.GET)
#         if form.is_valid():
#             q=form.cleaned_data['q']

#             # leng_code = request.LANGUAGE_CODE
#             # print(f'sity__sity_{leng_code}')
#             vector = SearchVector('sity__sity_en', weight = 'B' ) + SearchVector('stret__name_en', weight = 'A' ) + SearchVector('adres', weight='A' )
#             query = SearchQuery(q)
#             result = (Building.objects
#                       .annotate(rank = SearchRank(vector=vector, query=query, cover_density = True))
#                       .order_by('-rank')
#                       .select_related('sity')
#                       .select_related('stret')
#                       .values('id', 'sity__sity', 'stret__name', 'adres')
                      
#                              )
            
#             context = {
#                 'form':form,
#                 'result':result,
#             }
#             # cont = {
#             #     'result':list(result),
#             # }
#             pprint(connection.queries)
#             # return JsonResponse(cont)
#             return render(request, 'location/index.html', context=context )


#     return render(request, 'location/index.html', context=context )





def getlocation(request):
    # longitude = request.GET.get('longitude')
    # latitude = request.GET.get('latitude')
    # if(latitude and longitude):

        # pnt = f'POINT({longitude} {latitude})'
        # obj = (Building.objects.get(geometry__contains = pnt))

        # data ={
        #     'sity':obj.sity.sity_hy,
        #     'street':obj.stret.name_hy,
        #     'adres':obj.adres,
        # }
        # pprint(connection.queries) 
        # return JsonResponse({})
    # data = get_building_polygons(longitude=longitude,latitude=latitude)
        # save_new_data(data=data)
    return JsonResponse({})