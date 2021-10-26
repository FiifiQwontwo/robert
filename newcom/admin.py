from django.contrib import admin
from .models import *

# Register your models here.




@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'product_category_image', 'slug']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Ids)
class IdsAdmin(admin.ModelAdmin):
    fields = ['id_type', 'id_image', 'slug']
    search_fields = ['id_type']
    prepopulated_fields = {'slug': ('id_type',)}
