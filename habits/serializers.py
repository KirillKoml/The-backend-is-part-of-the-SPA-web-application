
from rest_framework.serializers import ModelSerializer, CharField
from rest_framework import serializers

from habits.models import UsefulHabit, PleasantHabit
from habits.validators import validate_time_to_complete


class UsefulHabitCreateSerializer(ModelSerializer):
    """Сериализатор для моделей полезных привычек для создания."""
    # Проверка на то, что поле time_to_complete не больше 120 секунд
    time_to_complete = CharField(validators=[validate_time_to_complete])

    def validate(self, data):
        """Проверка на выполнение условий."""
        # Проверка на то, что одновременно не заполнены поля приятная привычка и вознаграждение
        if ('pleasant_habit' in data and data['pleasant_habit']) and ('award' in data and data['award']):
            raise serializers.ValidationError({
                'error': 'У вас должно быть заполнено либо поле приятной привычки, либо вознаграждение за выполнение '
                         'полезной привычки'
            })

        # # Проверка на то, чтобы пользователь при создании полезной привычки использовал только свои приятные привычки
        # if data['pleasant_habit'].creator != self.context['request'].user:
        #     raise serializers.ValidationError("Используйте только свои приятные привычки.")
        return data

    class Meta:
        model = UsefulHabit
        fields = '__all__'


class UsefulHabitSerializer(ModelSerializer):
    """Сериализатор для моделей полезных привычек, кроме создания."""
    # Проверка на то, что поле time_to_complete не больше 120 секунд
    time_to_complete = CharField(validators=[validate_time_to_complete])

    def validate(self, data):
        """Проверка на выполнение условий."""
        # Проверка на то, что одновременно не заполнены поля приятная привычка и вознаграждение
        if ('pleasant_habit' in data and data['pleasant_habit']) and ('award' in data and data['award']):
            raise serializers.ValidationError({
                'error': 'У вас должно быть заполнено либо поле приятной привычки, либо вознаграждение за выполнение '
                         'полезной привычки'
            })

        return data

    class Meta:
        model = UsefulHabit
        fields = '__all__'


class PleasantHabitSerializer(ModelSerializer):
    """Сериализатор для моделей полезных привычек."""
    class Meta:
        model = PleasantHabit
        fields = '__all__'
