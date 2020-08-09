from rest_framework import serializers
from .models import Categories, SubCategories, Products

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

        
class SubCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategories
        fields = '__all__'

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('product_title','product_category','product_subcategory','unitprice')

class DataCountSerializer(serializers.ModelSerializer):

    total_quantity = serializers.IntegerField()
    total_price = serializers.IntegerField()
    avg_price = serializers.IntegerField()

    class Meta:
        model = Products
        fields = ('total_quantity', 'total_price', 'avg_price')