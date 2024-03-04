from modeltranslation.translator import translator, TranslationOptions
from .models import  Typefutur, TypeFuturNavigation


class TypefuturTranslationOptions(TranslationOptions):
    fields= ('names',)
translator.register(Typefutur, TypefuturTranslationOptions)


class TypefuturNavigationTranslationOptions(TranslationOptions):
    fields= ('names', 'discriptions')
translator.register(TypeFuturNavigation, TypefuturNavigationTranslationOptions)
