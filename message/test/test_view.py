from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.models import User
from django.urls import reverse
from message.models import Message


class TestMessageView(APITestCase):
    def setUp(self):
        self.sender = User.objects.create(username='peter87', password='Password12!')
        self.receiver = User.objects.create(username='jackson87', password='Password12!')
        self.s_authorization = f' Bearer {AccessToken.for_user(self.sender)}'
        self.r_authorization = f' Bearer {AccessToken.for_user(self.receiver)}'
        self.msg_data = {'sender': self.sender, 'receiver': self.receiver, 'text': 'text'}

    def test_create_message(self):
        response = self.client.post(reverse('send_list_message'), data=self.msg_data,
                                    HTTP_AUTHORIZATION=self.s_authorization)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Message.objects.count(), 1)

    def test_list_sent_message(self):
        Message.objects.create(**self.msg_data)
        response = self.client.get(reverse('send_list_message', ),
                                   HTTP_AUTHORIZATION=self.s_authorization)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_list_received_message(self):
        Message.objects.create(**self.msg_data)
        response = self.client.get(reverse('received_message'), HTTP_AUTHORIZATION=self.r_authorization)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_message_for_receiver(self):
        msg = Message.objects.create(**self.msg_data)
        response = self.client.get(reverse('retrieve_update_delete_message', kwargs={'pk': msg.pk}),
                                   HTTP_AUTHORIZATION=self.r_authorization)
        self.assertEqual(response.status_code, 200)

    def test_update_message_by_receiver(self):
        msg = Message.objects.create(**self.msg_data)
        response = self.client.put(reverse('retrieve_update_delete_message', kwargs={'pk': msg.pk}),
                                   HTTP_AUTHORIZATION=self.r_authorization)
        self.assertEqual(response.status_code, 403)

    def test_update_message_by_sender(self):
        msg = Message.objects.create(**self.msg_data)
        response = self.client.put(reverse('retrieve_update_delete_message', kwargs={'pk': msg.pk}),
                                   data={'text': 'hello'}, HTTP_AUTHORIZATION=self.s_authorization)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Message.objects.first().text, 'hello')

    def test_delete_message_by_receiver(self):
        msg = Message.objects.create(**self.msg_data)
        response = self.client.delete(reverse('retrieve_update_delete_message', kwargs={'pk': msg.pk}),
                                      HTTP_AUTHORIZATION=self.r_authorization)
        self.assertEqual(response.status_code, 403)

    def test_delete_message_by_sender(self):
        msg = Message.objects.create(**self.msg_data)
        response = self.client.delete(reverse('retrieve_update_delete_message', kwargs={'pk': msg.pk}),
                                      HTTP_AUTHORIZATION=self.s_authorization)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Message.objects.count(), 0)
