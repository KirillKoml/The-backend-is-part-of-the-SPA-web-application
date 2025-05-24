
from django.db import models

from users.models import User

# Список дней недели
DAY_OF_WEEK_CHOICES = [
    (0, 'Понедельник'),
    (1, 'Вторник'),
    (2, 'Среда'),
    (3, 'Четверг'),
    (4, 'Пятница'),
    (5, 'Суббота'),
    (6, 'Воскресенье'),
]


class PleasantHabit(models.Model):
    """Модель приятной привычки"""
    title = models.CharField(max_length=50, verbose_name='название приятной привычки', null=True,blank=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Создатель приятной привычки',
                                related_name='user_pleasant_habit', null=True, blank=True)

    class Meta:
        verbose_name = 'Приятная  привычка'
        verbose_name_plural = 'Приятные привычки'

    def __str__(self):
        return f'{self.title}'


class UsefulHabit(models.Model):
    """Модель полезной привычки."""
    title = models.CharField(max_length=35, verbose_name='название полезной привычки')
    place = models.CharField(max_length=35, verbose_name='название места')
    time = models.TimeField(verbose_name='время')
    day_of_week = models.IntegerField(choices=DAY_OF_WEEK_CHOICES, verbose_name='День недели', null=True, blank=True)
    action = models.CharField(max_length=50, verbose_name='название действия')
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Создатель полезной привычки',
                                related_name='user_useful_habit', null=True, blank=True)
    pleasant_habit = models.ForeignKey(PleasantHabit, on_delete=models.SET_NULL, verbose_name='приятная привычка',
                               related_name='pleasant_habit', null=True, blank=True)
    award = models.CharField(max_length=50, verbose_name='Вознаграждение за выполнение полезной привычки', null=True,
                             blank=True)
    sign_publicity = models.BooleanField(verbose_name='Публичная полезная привычка или нет')
    time_to_complete = models.PositiveIntegerField(verbose_name='Время на выполнение в секундах', default=120)

    class Meta:
        verbose_name = 'Полезная привычка'
        verbose_name_plural = 'Полезные привычки'

    def __str__(self):
        return f'{self.title}'
