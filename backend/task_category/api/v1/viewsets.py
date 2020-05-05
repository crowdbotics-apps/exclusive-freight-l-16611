from rest_framework import authentication
from task_category.models import Subcategory, Category
from .serializers import SubcategorySerializer, CategorySerializer
from rest_framework import viewsets


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Category.objects.all()


class SubcategoryViewSet(viewsets.ModelViewSet):
    serializer_class = SubcategorySerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Subcategory.objects.all()
