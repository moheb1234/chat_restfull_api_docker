from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSenderOrReadOnlyReceiver(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        if obj.receiver == user and request.method in SAFE_METHODS:
            return True
        return obj.sender == user
