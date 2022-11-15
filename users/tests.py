from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User

# Create your tests here.

class UserRegistrationTest(APITestCase):
    def test_registration(self):
        url = reverse('user_view')
        
        user_data = {
            "username": "testuser",
            "fullname": "테스트",
            "email": "test@test.com",
            "password": "password",
        }
        response = self.client.post(url, user_data)
        self.assertEqual(response.data['message'], "가입 완료!!")