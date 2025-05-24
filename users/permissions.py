from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """Права доступа только для создателя привычки."""
    def has_object_permission(self, request, view, obj):
        if obj.creator == request.user:
            return True
        return False