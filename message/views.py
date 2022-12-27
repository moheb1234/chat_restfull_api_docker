from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .filters import *
from .permissions import IsSenderOrReadOnlyReceiver
from .serializer import *


# get sent messages and send message
class SentMessagesListCreateView(generics.ListCreateAPIView):
    serializer_class = CreateMessageSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = SendMessageFiter

    def get_queryset(self):
        return Message.objects.filter(sender=self.request.user).order_by('send_date')


# get received messages
class ReceivedMessagesListView(generics.ListAPIView):
    serializer_class = CreateMessageSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = ReceiveMessageFiter

    def get_queryset(self):
        return Message.objects.filter(receiver=self.request.user).order_by('send_date')


class RetrieveUpdateDestroyMessageView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UpdateMessageSerializer
    permission_classes = [IsAuthenticated, IsSenderOrReadOnlyReceiver]
    queryset = Message.objects.all()
