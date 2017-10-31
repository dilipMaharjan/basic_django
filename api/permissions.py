from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    message = "You must be the owner."

    def is_permitted_user(self,request,view,obj):
        return obj.user==request.user