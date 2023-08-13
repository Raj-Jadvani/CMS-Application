from rest_framework import permissions


# Custom permission to only allow owners of a post to edit/delete it.
class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the author of the post.
        return obj.author == request.user
