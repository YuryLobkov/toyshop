from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Toy)
class ToyTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'price',)


@register(Materials)
class MaterialsTranslationOptions(TranslationOptions):
    fields = ('material',)


@register(Sizes)
class SizesTranslationOptions(TranslationOptions):
    fields = ('size',)


@register(Categories)
class CategoriesTranslationOptions(TranslationOptions):
    fields = ('category',)