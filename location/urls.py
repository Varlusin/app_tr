from django.urls import path
from location.views import (
    getlocation, 
    # search_location , 
    # src_loc, 
    user_order_adres
   )
urlpatterns = [
    path("orderedlocation/", user_order_adres),
    path("cordinats/", getlocation),
    # path('src/', search_location, name='src_loc'), 
    # path('adres/', src_loc ),
]



