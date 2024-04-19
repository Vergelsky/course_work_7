from rest_framework.permissions import BasePermission


class IsUserCreater(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if hasattr(view, 'get_object'):
            return
        print(user, '\n\n\n\n')
        return True
