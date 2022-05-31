from django.urls import path

from apps.product.views import ListCreateProductView, GetProductView

urlpatterns = [
    path('list_or_create/', ListCreateProductView.as_view()),
    path('<int:pk>/', GetProductView.as_view()),

]