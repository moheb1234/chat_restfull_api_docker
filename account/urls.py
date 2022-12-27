from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

urlpatterns = [
    path('register/', views.RegisterApiView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('referesh/token/', TokenRefreshView.as_view()),
    path('change-password/', views.ChangePasswordApiView.as_view()),
]
