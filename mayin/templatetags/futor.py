from atexit import register
from django import template
from mayin.models import Typefutur, TypeFuturNavigation

register = template.Library()

@register.simple_tag()
def tag_fut():
    # type_fut = (
    #     Typefutur
    #     .objects
    #     .filter(publish = True)
    #     .prefetch_related('translations')
    # )
    return Typefutur.objects.all()

    