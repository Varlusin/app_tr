from django.urls import path
from location.views import getlocation, search_location , src_loc

urlpatterns = [
    path("cordinats/", getlocation),
    path('src/', search_location, name='src_loc'), 
    path('adres/', src_loc ),
]

