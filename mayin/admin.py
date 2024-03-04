from django.contrib import admin
from mayin.models import Typefutur, TypeFuturNavigation

from modeltranslation.admin import TranslationAdmin

@admin.register(Typefutur)
class TypefuturAdmin(TranslationAdmin):
    prepopulated_fields = {"slug":("names",)}
    # list_display= ("title",)
    group_fieldsets = True
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(TypeFuturNavigation)
class TypeFuturNavigationAdmin(TranslationAdmin):
    prepopulated_fields = {"slug":("names",)}
    # list_display= ("title",)
    group_fieldsets = True
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }