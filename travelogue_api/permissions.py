from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
        Adding permission to check if the user is 
        the owner of the profile
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
