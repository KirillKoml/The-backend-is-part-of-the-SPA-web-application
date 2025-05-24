from django.contrib import admin

from habits.models import UsefulHabit


@admin.register(UsefulHabit)
class UsefulHabitAdmin(admin.ModelAdmin):
    """Админка для полезных привычек."""
    list_display = ('id', 'title')