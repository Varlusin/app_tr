from django.shortcuts import render
from django.utils.translation import gettext as _ 
from grups.models import ServisCategory, Company



def index(request):
    grup = Company.objects.all()

    context = {
        "title": _('Home'),
        'grup' : grup,
    }    
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



