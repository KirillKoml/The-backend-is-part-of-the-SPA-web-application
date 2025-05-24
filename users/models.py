from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователя."""
    username = None

    email = models.EmailField(verbose_name='Почта', unique=True)
    tg_chat_id = models.CharField(max_length=50, unique=True, verbose_name='Телеграмм chat_id', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email


