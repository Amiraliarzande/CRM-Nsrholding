from rest_framework.permissions import BasePermission
from app.accounts.models import UserType

class IsModirOrSuperUser(permissions.BasePermission):
    
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and 
            request.user.type in [UserType.MODIR_FOROOSH, UserType.SUPERUSER]
        )