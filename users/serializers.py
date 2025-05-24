from rest_framework.serializers import ModelSerializer
from users.models import User


class UserCreateSerializer(ModelSerializer):
    """Сериализатор для создания моделей пользователей."""
    class Meta:
        model = User
        fields = ('email', 'tg_chat_id', 'password')