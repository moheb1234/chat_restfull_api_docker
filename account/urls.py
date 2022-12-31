from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from . import views

urlpatterns = [
    path('register/', views.RegisterApiView.as_view(), name='user-register'),
    path('login/', TokenObtainPairView.as_view()),
    path('referesh/token/', TokenRefreshView.as_view()),
    path('change-password/', views.ChangePasswordApiView.as_view(), name='user-change-password'),
]
