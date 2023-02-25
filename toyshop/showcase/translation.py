from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Toy)
class ToyTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'size', 'material', 'price', 'category')

@register(Materials)
class MaterialsTranslationOptions(TranslationOptions):
    fields = ('material')
