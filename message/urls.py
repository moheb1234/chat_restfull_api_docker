from django.urls import path

from . import views

urlpatterns = [
    path('send/', views.SentMessagesListCreateView.as_view(), name='send_list_message'),
    path('received/', views.ReceivedMessagesListView.as_view(), name='received_message'),
    path('<int:pk>/', views.RetrieveUpdateDestroyMessageView.as_view(), name='retrieve_update_delete_message'),
]
