from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj): 
        if request.method == 'DELETE' or 'POST': 
            return obj == request.user
