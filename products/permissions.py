from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    """
    Allows read-only access to authenticated users,
    but write access only to admin users.
    """

    def has_permission(self, request, view):
        # SAFE_METHODS = GET, HEAD, OPTIONS
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated

        # Write permissions: admin only
        return request.user.is_staff
