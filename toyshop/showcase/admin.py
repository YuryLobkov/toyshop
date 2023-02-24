from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

# Register your models here.

@admin.register(Toy)
class ToyAdmin(TranslationAdmin):
    class Meta:
        model = Toy
        fields = ('name', 'description', 'material', 
                  'size', 'price', 'in_stock', 'quantity', 
                  'category', 'image')


@admin.register(Materials)
class MaterialsAdmin(TranslationAdmin):
    class Meta:
        model = Materials
        fields = '__all__'


@admin.register(Sizes)
class SizesAdmin(TranslationAdmin):
    class Meta:
        model = Sizes
        fields = '__all__'


@admin.register(Categories)
class CategoriesAdmin(TranslationAdmin):
    class Meta:
        model = Categories
        fields = '__all__'


admin.site.register(Order)