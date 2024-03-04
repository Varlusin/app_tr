from django.contrib import admin
from grups.models import ServisCategory, Company, CompanyDiscription, PopularityCompany

from modeltranslation.admin import TranslationAdmin
from leaflet.admin import LeafletGeoAdmin

@admin.register(ServisCategory)
class ServisCategoryAdmin(TranslationAdmin):
    prepopulated_fields = {"slug":("names",)}
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

@admin.register(Company)
class CompanyAdmin(TranslationAdmin):
    prepopulated_fields = {"slug":("names",)}
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


# @admin.register(CompanyDiscription)
class CompanyDiscriptionAdmin(TranslationAdmin):
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

class CompanyDiscriptionAdmin(LeafletGeoAdmin):
    pass

admin.site.register(CompanyDiscription, CompanyDiscriptionAdmin)
admin.site.register(PopularityCompany)


