from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User

# Create your tests here.

class UserRegistrationTest(APITestCase):
    def test_registration(self):
        # 장고에서 알아서 name에 해당되는 url을 가져온다.
        url = reverse('user_view')
        user_data = {
            "email": "hyun@naver.com",
            "password": "1234",
        }
        response = self.client.post(url, user_data)
        self.assertEqual(response.status_code, 201)