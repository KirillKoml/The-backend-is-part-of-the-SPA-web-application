
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserTestCase(APITestCase):
    """Тесты для пользователей."""
    def test_user_create(self):
        """Тест на создание пользователя."""
        # Arrange(подготавливаю данные для теста)
        url = reverse('users:register')

        # Act(совершаю действие которое тестирую)
        data = {'email': 'test_email@yandex.ru', 'password': '12345'}
        response = self.client.post(url, data)

        # Assert(делаю проверки)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            User.objects.all().count(), 1
        )
