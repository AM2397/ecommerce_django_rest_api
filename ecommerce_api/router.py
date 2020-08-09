from ecom_restapi.viewsets import CategoriesViewSet, SubCategoriesViewSet, ProductsViewSet, CountDataViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('categories',CategoriesViewSet)
router.register('subcategories',SubCategoriesViewSet)
router.register('products',ProductsViewSet)
router.register('datacount',CountDataViewSet, basename='datacount')