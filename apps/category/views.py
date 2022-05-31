from rest_framework import generics
from apps.category.models import Category
from apps.category.serializers import CategorySerializer


class ListCreateCategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

