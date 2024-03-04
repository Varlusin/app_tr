from modeltranslation.translator import translator, TranslationOptions
from grups.models import  ServisCategory, Company, CompanyDiscription


class ServisCategoryTranslationOptions(TranslationOptions):
    fields= ('names',)
translator.register(ServisCategory, ServisCategoryTranslationOptions)


class CompanyTranslationOptions(TranslationOptions):
    fields= ('names', 'specialcolumn')
translator.register(Company, CompanyTranslationOptions)

class CompanyDiscriptionTranslationOptions(TranslationOptions):
    fields= ('discription',)
translator.register(CompanyDiscription, CompanyDiscriptionTranslationOptions)

