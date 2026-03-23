from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Admins can do anything; users can only read.
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            # Check role field instead of is_staff
            return getattr(request.user, "role", "user") == "admin" or request.method in permissions.SAFE_METHODS
        return False


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Custom permission to allow owners of an object or admins to edit or delete it.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            if obj.privacy == "private":
                return obj.author == request.user or request.user.is_staff or request.user.is_superuser
            return True
        
        # Allow if the user is the author
        if hasattr(obj, "author") and obj.author == request.user:
            return True
        
        # Allow if the user has admin role
        if getattr(request.user, "role", "user") == "admin":
            return True
        
        #Allow if the user is Django staff/superuser
        if request.user.is_staff or request.user.is_superuser:
            return True
        
        # Otherwise deny
        return False
