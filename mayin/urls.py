from django.urls import path
from  mayin.views import company , index
from grups.views import Company_vews

urlpatterns = [
    path("", index, name = 'home'),
    path('<slug:slug>',company , name = 'company'),
    path( ("<slug:company_slug>/<int:company_id>/"), Company_vews , name = 'Companyvews'),
]





