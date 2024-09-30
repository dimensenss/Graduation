from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    def has_permission(self, request, view):
        # Проверяем, что пользователь аутентифицирован
        if not request.user.is_authenticated: #TODO проверка на аутентификацию
            return False

        # Получаем объект, к которому осуществляется доступ
        instance = view.get_object()
        # Проверяем, что текущий пользователь является владельцем
        return bool(instance.course.info.owner == request.user)