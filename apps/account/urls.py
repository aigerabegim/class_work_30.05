from django.urls import path
from .views import LoginView, RegisterView, ActivateView, LogoutAPIView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('logout/', LogoutAPIView.as_view()),
    path('register/', RegisterView.as_view()),
    path('activate/<str:activate_code>/', ActivateView.as_view()),
]