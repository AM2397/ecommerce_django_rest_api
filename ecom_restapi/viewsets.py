from rest_framework import viewsets
from . import models
from . import serializers
from django.db.models import Avg, Sum

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = models.Categories.objects.all()
    serializer_class = serializers.CategoriesSerializer

    def get_queryset(self):
        queryset = models.Categories.objects.all()
        product_category = self.request.query_params.get('product_category', None)
        if product_category is not None:
            queryset = queryset.filter(product_category=product_category)
        return queryset

class SubCategoriesViewSet(viewsets.ModelViewSet):
    queryset = models.SubCategories.objects.all()
    serializer_class = serializers.SubCategoriesSerializer

    def get_queryset(self):
        queryset = models.SubCategories.objects.all()
        product_category = self.request.query_params.get('product_category', None)
        product_subcategory = self.request.query_params.get('product_subcategory', None)
        if product_subcategory is not None:
            queryset = queryset.filter(product_category=product_category,product_subcategory=product_subcategory)
        
        return queryset

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = models.Products.objects.all()
    serializer_class = serializers.ProductsSerializer

    def get_queryset(self):
        queryset = models.Products.objects.all()
        product_category = self.request.query_params.get('product_category', None)
        product_subcategory = self.request.query_params.get('product_subcategory', None)
        if product_subcategory is not None:
            queryset = queryset.filter(product_category=product_category,product_subcategory=product_subcategory)
        
        return queryset

class CountDataViewSet(viewsets.ModelViewSet):
    queryset = models.Products.objects.all()
    serializer_class = serializers.DataCountSerializer

    def get_queryset(self):
        product_category = self.request.query_params.get('product_category', None)
        product_subcategory = self.request.query_params.get('product_subcategory', None)
        if product_category is not None and product_subcategory is not None:
            queryset = models.Products.objects.values('product_category', 'product_subcategory').filter(product_category=product_category, product_subcategory=product_subcategory).order_by('product_category').annotate(total_quantity=Sum('quantity'),total_price=Sum('totalprice'),avg_price=Avg('totalprice'))
        else:
            queryset = models.Products.objects.values('product_category', 'product_subcategory').order_by('product_category').annotate(total_quantity=Sum('quantity'),total_price=Sum('totalprice'),avg_price=Avg('totalprice'))

        return queryset