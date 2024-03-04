
# from unidecode import unidecode
# import unicodedata
# from django.contrib.postgres.search import (SearchVector, 
#                                             SearchQuery, 
#                                             SearchRank, 
#                                             TrigramSimilarity,
#                                             TrigramDistance)
# from location.models import (Building,
#                              locationAvailable,
#                              Street)

# from django.db.models import F



# def _get_len_code(txt):
#     unicodeNane = unicodedata.name(txt[0])
#     if "ARMENIAN" in unicodeNane:
#         return "_hy"
#     elif "CYRILLIC" in unicodeNane:
#         return "_ru"
#     elif "LATIN" in unicodeNane:
#         return "_en"
#     else:
#         return f""" = '{unidecode(txt)}' """


# class SearchResult:
#     def __init__(self, *args) -> None:

#         self.query_adres = args
#         self.old_rez = {}

#     def src(self):
#         # search_leng = _get_len_code(txt=self.query_adres)
#         print(self.old_rez, self.query_adres)
#         self.old_rez = 'aaaaaaa'
#         print(self.__dict__)



# def search_results(query_adres):

#     search_leng = _get_len_code(txt=query_adres)

#     if len(query_adres.split()) == 1:
#         res_sity = (
#             locationAvailable.objects
#             .annotate(similarity=TrigramSimilarity(f"sity{search_leng}", query_adres),)
#             # .filter(similarity__gt=0.3)
#             .order_by('-similarity')
#             .values('id', f'sity{search_leng}', 'similarity')[:2]
#             )
#         res_stret = (
#             Street.objects
#             .annotate(similarity =  TrigramSimilarity(f'name{search_leng}', query_adres ),)
#             # .filter(similarity__gte = 0.5)
#             .order_by('-similarity')
#             .values('id', f'name{search_leng}', 'similarity')[:3]
#             )
#         print(res_sity)
#         data: None = list(res_sity)
        
#         print( list(res_stret))
#         return (data)


#     vector = (
#         SearchVector(f"sity__sity{search_leng}" ) #, weight="B")
#         + SearchVector(f"stret__name{search_leng}") #, weight="A")
#         + SearchVector('adres') #, weight="A")
#     )
#     query = SearchQuery(query_adres, search_type="websearch")
#     result = (
#         Building.objects.annotate(
#             stret_sim = TrigramSimilarity(f'stret__name{search_leng}', query_adres),
#             sity_sim = TrigramSimilarity(f'sity__sity{search_leng}', query_adres),
#             simil = F("sity_sim") + F("stret_sim")
#         )
#         .order_by("-simil")
#         .select_related("sity")
#         .select_related("stret")
#         .values("id", f'sity__sity{search_leng}', f'stret__name{search_leng}','simil', "sity_sim", "stret_sim")[:10]
#     )

#     return list(result)





# def search_results(query_adres):
#     search_leng = _get_len_code(txt=query_adres)

#     if len(query_adres.split()) == 1:
#         print('ffffffffff')



#     vector = (
#         SearchVector(f"sity__sity{search_leng}" ) #, weight="B")
#         + SearchVector(f"stret__name{search_leng}") #, weight="A")
#         + SearchVector('adres') #, weight="A")
#     )
#     query = SearchQuery(query_adres, search_type="websearch")
#     result = (
#         Building.objects.annotate(
#             rank=SearchRank(vector=vector, query=query, cover_density=True)
#         )
#         .order_by("-rank")
#         .select_related("sity")
#         .select_related("stret")
#         .values("id", f'sity__sity{search_leng}', f'stret__name{search_leng}', "adres")[:10]
#     )

#     return result
