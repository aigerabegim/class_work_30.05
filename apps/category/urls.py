from django.urls import path
from .views import ListCreateCategoryView

urlpatterns = [
    path('list_or_create/', ListCreateCategoryView.as_view())
]
