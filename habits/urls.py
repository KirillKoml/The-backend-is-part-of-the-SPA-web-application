from django.urls import path

from habits.apps import HabitsConfig
from habits.views import UsefulHabitPublicListAPIView, UsefulHabitCreateAPIView, UsefulHabitUpdateAPIView, \
    UsefulHabitDestroyAPIView, UsefulHabitUserListAPIView, PleasantHabitCreateAPIView

app_name = HabitsConfig.name

urlpatterns = [
    # Урлы для полезных привычек
    path('list/', UsefulHabitPublicListAPIView.as_view(), name='useful_habit-list'),
    path('create/', UsefulHabitCreateAPIView.as_view(), name='useful_habit-create'),
    path('<int:pk>/update/', UsefulHabitUpdateAPIView.as_view(), name='useful_habit-update'),
    path('<int:pk>/destroy/', UsefulHabitDestroyAPIView.as_view(), name='useful_habit-destroy'),
    path('my_list/', UsefulHabitUserListAPIView.as_view(), name='my_useful_habit-list'),

    # Урлы для приятных привычек
    path('create_pleasant_habit/', PleasantHabitCreateAPIView.as_view(), name='pleasant_habit-create'),
]
