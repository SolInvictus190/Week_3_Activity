from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.owner == request.user


class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    def has_object_permission(self, request, view, obj):
        user = request.user
        print(user.get_all_permissions())
        if user.is_staff:
            if user.has_perm("product.add_product"):
                return True
            if user.has_perm("product.delete_product"):
                return True
            if user.has_perm("product.change_product"):
                return True
            if user.has_perm("product.view_product"):
                return True
            return False
        return False
