
from django.http import JsonResponse
# from location.utils import search_results, SearchResult

from django.shortcuts import render
from django.db.models import  When, Case

from location.forms import  LocationSearchForm
from location.models import Street, locationAvailable, Building, search_model
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
from nltk.metrics import edit_distance

def _get_len_code(txt) -> str:
    unicodeNane = unicodedata.name(txt[0])
    if "ARMENIAN" in unicodeNane: return "_hy"
    elif "CYRILLIC" in unicodeNane: return "_ru"
    elif "LATIN" in unicodeNane: return "_en"
    else: return f""" = '{unidecode(txt)}' """

def _word_similarity(word1, word2) -> float:
    return 1 - (edit_distance(word1, word2) / max(len(word1), len(word2)))

def _get_len_code_unicode(txt) -> dict:
    unicodeNane = unicodedata.name(txt[0])
    if "ARMENIAN" in unicodeNane: return {'len_code':"_hy", 'query': unidecode(txt)}
    elif "CYRILLIC" in unicodeNane: return {'len_code':"_ru", 'query': unidecode(txt)}
    elif "LATIN" in unicodeNane: return {'len_code':"_en", 'query': txt}
    else: return {'len_code':"_en", 'query': unidecode(txt)}


def src_loc(request) -> JsonResponse:
    if 'q' in request.GET:
        q = request.GET.get('q')
        query_unicode = _get_len_code_unicode(q)
        sity_len_code = f"""sity__sity{query_unicode['len_code']}"""
        stret_len_code = f"""stret__name{query_unicode['len_code']}"""
        find = (
            search_model.objects
            .annotate(similarity=TrigramSimilarity('txt', query_unicode['query']),)
        # .filter(similarity__gt=0.3)
            .order_by('-similarity')[:10]
            .select_related('sity', 'stret')
            .values(sity_len_code, stret_len_code, 'similarity')[:10]  #, 'txt', 'sity_id', 'stret_id')[:10]
        )
        find = list(find)
        pprint(connection.queries)
    return JsonResponse({"data":find})





# def src_loc(request) -> JsonResponse:
#     if 'q' in request.GET:
#         q = request.GET.get('q')
#         len_code = _get_len_code(q)
#         siyt_ln_code = f'sity{len_code}'
#         find_sity = (
#             locationAvailable.objects
#             .annotate(similarity=TrigramSimilarity(siyt_ln_code, q),)
#         # .filter(similarity__gt=0.3)
#             .order_by('-similarity')
#             .values('id', siyt_ln_code )[:1]
#         )
#         find_sity = list(find_sity)
#         sity_name_of_find = find_sity[0][siyt_ln_code]
#         list_word_query = q.split()
#         similarity_list = []
#         for word in list_word_query:
#             similarity_list.append(_word_similarity(word.capitalize(), sity_name_of_find))
#         list_word_query.pop(similarity_list.index(max(similarity_list)))
#         list_word_query = ' '.join(list_word_query)

#         street_len_code = f'name{len_code}'
#         find_streets = (
#             Street.objects
#             .filter(sity__id =find_sity[0]['id'])
#             .annotate(similarity=TrigramSimilarity(street_len_code, list_word_query),)
#             .filter(similarity__gt=0.3)
#             .order_by('-similarity')
#             .values( street_len_code , 'similarity', 'buildings__adres')
#         )
#     find_streets = list(find_streets)

#     # que =(
#     # Building.objects
#     # .select_related('sity', 'stret')
#     # .values('id', 'adres', 'sity__sity_en',  'sity__sity_hy', 'sity__sity_ru', 'stret__name_en', 'stret__name_hy', 'stret__name_ru' )

#     # )
#     # for i in que:
#     #     print(i) 
#     pprint(connection.queries)
#     resp = {
#         'sity': find_sity,
#         'sreet':find_streets}


    
#     return JsonResponse(resp)






def search_location(request):
    form = LocationSearchForm
    context = {'form':form}

    if 'q' in request.GET:
        form = LocationSearchForm(request.GET)
        if form.is_valid():
            q=form.cleaned_data['q']
            len_code = _get_len_code(q)
            siyt_ln_code = f'sity{len_code}'
            find_sity = (
                locationAvailable.objects
                .annotate(similarity=TrigramSimilarity(siyt_ln_code, q),)
            # .filter(similarity__gt=0.3)
                .order_by('-similarity')
                .values('id', siyt_ln_code, 'similarity')[:1]
            )
            find_sity = list(find_sity)
            sity_name_of_find = find_sity[0][siyt_ln_code]
            list_word_query = q.split()
            similarity_list = []
            for word in list_word_query:
                similarity_list.append(_word_similarity(word.capitalize(), sity_name_of_find))
            list_word_query.pop(similarity_list.index(max(similarity_list)))
            stret_query = ' '.join(list_word_query)
            print(stret_query)
            res_str = (
                Street.objects
                .filter(sity__id =find_sity[0]['id'])
                .annotate(similarity=TrigramSimilarity(f"name{len_code}", stret_query),)
                .filter(similarity__gt=0.1)
                .order_by('-similarity')[:10]
                # .values('building_id', 'name', 'similarity', 'buildings__adres' )
                .prefetch_related('buildings')
            )
        context = {
            'form':form,
            'result':res_str,
            # 'result': result
        }

        pprint(connection.queries)
        return render(request, 'location/index.html', context=context )

    return render(request, 'location/index.html', context=context )




# def search_location(request):

#     form = LocationSearchForm
    
#     context = {
#         'form':form
#     }

#     if 'q' in request.GET:
#         form = LocationSearchForm(request.GET)
#         if form.is_valid():
#             q=form.cleaned_data['q']
#             search_leng = _get_len_code(txt=q)
#             # print(SearchQuery(q))
#             res_sity = (
#                 locationAvailable.objects
#                 .annotate(similarity=TrigramSimilarity(f"sity{search_leng}", q),)
#             # .filter(similarity__gt=0.3)
#                 .order_by('-similarity')
#                 .values('id', f"sity{search_leng}", 'similarity')[:1]
#             )
#             ressity = list(res_sity)
#             if ressity[0]['similarity'] >=0.1:
#                 # pprint(ressity)
#                 # pprint(q)
#                 res_str = (
#                     Street.objects
#                     .filter(sity__id =ressity[0]['id'])
#                     .annotate(similarity=TrigramSimilarity(f"name{search_leng}", q),)
#                     .filter(similarity__gt=0.1)
#                     .order_by('-similarity')[:10]
#                     # .values('building_id', 'name', 'similarity', 'buildings__adres' )
#                     .prefetch_related('buildings')

#                 )

#             # for i in res_str:
#             #     for j in i.buildings.all():
#             #         print(j)

            
#             context = {
#                 'form':form,
#                 'result':res_str,
#                 # 'result': result
#             }

#             # pprint(connection.queries)
#             return render(request, 'location/index.html', context=context )


#     return render(request, 'location/index.html', context=context )
















# def src_loc(request) -> JsonResponse:
#     # if 'q' in request.GET:
#     #     query = request.GET.get('q')
#     #     resp = {
#     #         'adr':search_results(query_adres=query)
#     #     }
#     resp = {}
#     return JsonResponse(resp)













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
    longitude = request.GET.get('longitude')
    latitude = request.GET.get('latitude')
    if(latitude and longitude):
        print( f'POINT({longitude} {latitude})')

        pnt = f'POINT({longitude} {latitude})'
        obj = (Building.objects.get(geometry__contains = pnt))

        data ={
            'sity':obj.sity.sity_hy,
            'street':obj.stret.name_hy,
            'adres':obj.adres,
        }
        pprint(connection.queries) 
        print(data)
        # return JsonResponse({})
    # data = get_building_polygons(longitude=longitude,latitude=latitude)
        # save_new_data(data=data)
    return JsonResponse({})
