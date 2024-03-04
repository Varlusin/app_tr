from atexit import register
from django import template
from grups.models import ServisCategory

register = template.Library()

@register.simple_tag()
def tag_ctg():

    return ServisCategory.objects.all()


