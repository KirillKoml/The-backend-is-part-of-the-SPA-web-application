from rest_framework.generics import CreateAPIView

from users.models import User
from users.serializers import UserCreateSerializer


class UserCreateAPIView(CreateAPIView):
    """Класс для создания моделей пользователей."""
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    def perform_create(self, serializer):
        """Вмешиваюсь в логику контроллера для его правильной регистрации пользователей."""
        # Сохраняю пользователя и сразу делаю его активным
        user = serializer.save(is_active=True)

        # Хэширую пароль пользователя и сохраняю пользователя
        user.set_password(user.password)
        user.save()