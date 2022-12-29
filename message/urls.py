from django.urls import path

from . import views

urlpatterns = [
    path('send/', views.SentMessagesListCreateView.as_view()),
    path('received/', views.ReceivedMessagesListView.as_view()),
    path('<int:pk>/', views.RetrieveUpdateDestroyMessageView.as_view()),
]
