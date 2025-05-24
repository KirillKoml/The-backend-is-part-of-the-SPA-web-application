from rest_framework.serializers import ValidationError


def validate_time_to_complete(value):
    """Проверка на то, что время выполнения не больше 120 секунд."""
    if int(value) > 120:
        raise ValidationError('Время на выполнение больше 120 секунд')
