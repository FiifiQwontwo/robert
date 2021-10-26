from rest_framework import serializers
from .models import *


class IdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ids
        fields = ['id', 'id_type', 'id_image']


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'name', 'description', 'product_category_image', 'slug']


class VendorSignSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorSign
        fields = ['id', 'name_of_vendor', 'name_of_shop',
                  'phone_number', 'phone_number1', 'biz_registration',
                  'shop_place_image', 'id_type', 'id_number', 'id_image',
                  'current_image', 'email_add', 'location', 'ghana_post_address', 'category'
                  ]
