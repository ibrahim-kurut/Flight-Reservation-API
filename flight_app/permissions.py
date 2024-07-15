from rest_framework import permissions



class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Allow only administrators to edit data.
    """
    
    def has_permission(self, request, view):
        # Check if the request uses a secure method (read-only methods)
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Check if the current user exists and is an admin
        return bool(request.user and request.user.is_staff)


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    allow only object owners or administrators to edit it.
    """
    
    def has_object_permission(self, request, view, obj):
        # Check if the request uses a secure method (read-only methods)
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Allow editing if the current user is the object owner or an admin
        return bool(obj.user == request.user or request.user.is_staff)


