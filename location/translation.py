from modeltranslation.translator import translator, TranslationOptions
from location.models import (
    locationAvailable,
    Street,
)


class locationAvailableTranslationOptions(TranslationOptions):
    fields= ('sity',)
translator.register(locationAvailable, locationAvailableTranslationOptions)


class StreetTranslationOptions(TranslationOptions):
    fields= ('name',)
translator.register(Street, StreetTranslationOptions)

