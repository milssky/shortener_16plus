from rest_framework.permissions import BasePermission, SAFE_METHODS


class HaveSecretWordOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if "secret_word" in request.data and request.data["secret_word"] == "admin":
            return True
        return False
