from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from account.serializer import UserRegistrationSerializer, UserChangePasswordSerializer


class RegisterApiView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()


class ChangePasswordApiView(generics.UpdateAPIView):
    serializer_class = UserChangePasswordSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
