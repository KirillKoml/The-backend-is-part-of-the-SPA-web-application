import requests

from celery import shared_task

from config.settings import tg_token
from habits.models import UsefulHabit

from django.utils.timezone import now
from django.db.models import Q


@shared_task
def send_notification_tg_about_useful_habit():
    """Периодическая задача для отправки напоминания выполнить полезную привычку в телеграмм."""
    # Получаю текущий день недели
    today = now().date().weekday()

    # Получаю полезные привычки которые необходимо сделать сегодня
    useful_habit_today = UsefulHabit.objects.filter(Q(day_of_week=today) | Q(day_of_week=None))

    # Отправляю по каждой привычке сообщения
    for info in useful_habit_today:
        if info.creator.tg_chat_id:
            params = {
                'text': f'Здравствуйте, сегодня вы планировали {info.action} в {info.time} в {info.place}',
                'chat_id': info.creator.tg_chat_id
            }
            requests.get(f'https://api.telegram.org/bot{tg_token}/sendMessage', params=params)
