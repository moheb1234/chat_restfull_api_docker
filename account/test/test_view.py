from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken


class TestUserRegisterView(APITestCase):
    def setUp(self):
        self.data = {'username': 'bob123', 'password': 'Password12@', 'confirm_password': 'Password12@'}

    def test_valid_data(self):
        response = self.client.post(reverse('user-register'), data=self.data)
        self.assertEqual(response.status_code, 201)

    def test_confirm_password_dont_match(self):
        self.data['confirm_password'] = 'Password12!'
        response = self.client.post(reverse('user-register'), data=self.data)
        self.assertEqual(response.status_code, 400)
        self.assertTrue('non_field_errors' in response.data)

    def test_invalid_password(self):
        self.data['password'] = 'Password2'
        response = self.client.post(reverse('user-register'), data=self.data)
        self.assertEqual(response.status_code, 400)
        self.assertTrue('password' in response.data)


class TestChangePasswordView(APITestCase):
    def setUp(self):
        self.data = {'old_password': 'Password@39', 'password': 'Password#10', 'confirm_password': 'Password#10'}
        self.user = User.objects.create(username='jon15', password=make_password('Password@39'))
        self.token = AccessToken.for_user(self.user)
        self.authorization = f' Bearer {str(self.token)}'

    def test_valid_data(self):
        response = self.client.put(path=reverse('user-change-password'), data=self.data,
                                   HTTP_AUTHORIZATION=self.authorization)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(User.objects.first().check_password('Password#10'))

    def test_wrong_password(self):
        self.data['old_password'] = 'Password$20'
        response = self.client.put(path=reverse('user-change-password'), data=self.data,
                                   HTTP_AUTHORIZATION=self.authorization)
        self.assertEqual(response.status_code, 400)
        self.assertTrue('old_password' in response.data)
