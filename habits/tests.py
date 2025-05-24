
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from habits.models import UsefulHabit, PleasantHabit
from users.models import User


class UsefulHabitTestCase(APITestCase):
    """Тесты для полезных привычек"""
    # Создал необходимые модели и авторизовал пользователя
    def setUp(self):
        self.user = User.objects.create(email='test_email@yandex.ru')
        self.pleasant_habit = PleasantHabit.objects.create(title='text_title', creator=self.user)
        self.useful_habit_public = UsefulHabit.objects.create(title='text_title', place='test_place', time='06:00:00',
                                                              day_of_week=0, action='test_action', creator=self.user,
                                                              pleasant_habit=self.pleasant_habit, sign_publicity=True,
                                                              time_to_complete=120)
        self.useful_habit_non_public = UsefulHabit.objects.create(title='text_title_01', place='test_place_01',
                                                                  time='06:00:00', day_of_week=0, action='test_action_01',
                                                                  creator=self.user, pleasant_habit=self.pleasant_habit,
                                                                  sign_publicity=False, time_to_complete=120)
        self.client.force_authenticate(user=self.user)

    def test_useful_habit_create(self):
        """Тест на создание полезной привычки."""
        # Arrange(подготавливаю данные для теста)
        url = reverse('habits:useful_habit-create')

        # Act(совершаю действие которое тестирую)
        data = {'title': 'text_title_0', 'place': 'test_place_0', 'time': '07:00:00', 'action': 'test_action_0',
                'creator': self.user.pk, 'pleasant_habit': self.pleasant_habit.pk, 'sign_publicity': True,
                'time_to_complete': 120}
        response = self.client.post(url, data)

        # Assert(делаю проверки)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            UsefulHabit.objects.all().count(), 3
        )

    def test_useful_habit_update(self):
        """Тест на обновление полезной привычки."""
        # Arrange(подготавливаю данные для теста)
        url = reverse('habits:useful_habit-update', args=(self.useful_habit_public.pk,))

        # Act(совершаю действие которое тестирую)
        data = {'title': 'test_new'}
        response = self.client.patch(url, data)
        data = response.json()

        # Assert(делаю проверки)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('title'), 'test_new'
        )

    def test_useful_habit_delete(self):
        """Тест на удаление полезной привычки."""
        # Arrange(подготавливаю данные для теста)
        url = reverse('habits:useful_habit-destroy', args=(self.useful_habit_public.pk,))

        # Act(совершаю действие которое тестирую)
        response = self.client.delete(url)

        # Assert(делаю проверки)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            UsefulHabit.objects.all().count(), 1
        )

    def test_useful_habit_public_list(self):
        """Тест на просмотр списка публичных полезных привычек."""
        # Arrange(подготавливаю данные для теста)
        url = reverse('habits:useful_habit-list')

        # Act(совершаю действие которое тестирую)
        response = self.client.get(url)

        # Assert(делаю проверки)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        result = [
            {
                "id": self.useful_habit_public.pk,
                "time_to_complete": str(self.useful_habit_public.time_to_complete),
                "title": self.useful_habit_public.title,
                "place": self.useful_habit_public.place,
                "time": self.useful_habit_public.time,
                "day_of_week": self.useful_habit_public.day_of_week,
                "action": self.useful_habit_public.action,
                "award": None,
                "sign_publicity": self.useful_habit_public.sign_publicity,
                "creator": self.useful_habit_public.creator.pk,
                "pleasant_habit": self.useful_habit_public.pleasant_habit.pk
            }
        ]
        data = response.json()
        self.assertEqual(
            data, result
        )

    def test_my_useful_habit_list(self):
        """Тест на просмотр списка полезных привычек конкретного пользователя."""
        # Arrange(подготавливаю данные для теста)
        url = reverse('habits:my_useful_habit-list')

        # Act(совершаю действие которое тестирую)
        response = self.client.get(url)

        # Assert(делаю проверки)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        result = {
            "count": UsefulHabit.objects.all().count(),
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.useful_habit_public.pk,
                    "time_to_complete": str(self.useful_habit_public.time_to_complete),
                    "title": self.useful_habit_public.title,
                    "place": self.useful_habit_public.place,
                    "time": self.useful_habit_public.time,
                    "day_of_week": self.useful_habit_public.day_of_week,
                    "action": self.useful_habit_public.action,
                    "award": None,
                    "sign_publicity": self.useful_habit_public.sign_publicity,
                    "creator": self.useful_habit_public.creator.pk,
                    "pleasant_habit": self.useful_habit_public.pleasant_habit.pk
                },
                {
                    "id": self.useful_habit_non_public.pk,
                    "time_to_complete": str(self.useful_habit_non_public.time_to_complete),
                    "title": self.useful_habit_non_public.title,
                    "place": self.useful_habit_non_public.place,
                    "time": self.useful_habit_non_public.time,
                    "day_of_week": self.useful_habit_non_public.day_of_week,
                    "action": self.useful_habit_non_public.action,
                    "award": None,
                    "sign_publicity": self.useful_habit_non_public.sign_publicity,
                    "creator": self.useful_habit_non_public.creator.pk,
                    "pleasant_habit": self.useful_habit_non_public.pleasant_habit.pk
                }
            ]
        }
        data = response.json()
        self.assertEqual(
            data, result
        )


class PleasantHabitTestCase(APITestCase):
    """Тесты для приятных привычек"""
    # Создал необходимые модели и авторизовал пользователя
    def setUp(self):
        self.user = User.objects.create(email='test_email@yandex.ru')
        self.pleasant_habit = PleasantHabit.objects.create(title='text_title', creator=self.user)
        self.client.force_authenticate(user=self.user)

    def test_pleasant_habit_create(self):
        """Тест на создание приятной привычки."""
        # Arrange(подготавливаю данные для теста)
        url = reverse('habits:pleasant_habit-create')

        # Act(совершаю действие которое тестирую)
        data = {'title': 'speed_test', 'creator': self.user.pk}
        response = self.client.post(url, data)

        # Assert(делаю проверки)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            PleasantHabit.objects.all().count(), 2
        )
