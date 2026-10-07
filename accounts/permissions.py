from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    """শুধুমাত্র Admin রোলের ইউজারদের অ্যাক্সেস দেবে"""
    def has_permission(self, request, view):
        return bool(
            request.user and 
            request.user.is_authenticated and 
            (request.user.role == 'admin' or request.user.is_superuser)
        )

class IsStaffOrAdmin(BasePermission):
    """Staff অথবা Admin রোলের ইউজারদের অ্যাক্সেস দেবে"""
    def has_permission(self, request, view):
        return bool(
            request.user and 
            request.user.is_authenticated and 
            (request.user.role in ['admin', 'staff'] or request.user.is_staff or request.user.is_superuser)
        )

class IsViewerOrAbove(BasePermission):
    """যেকোনো লগইনকৃত ইউজারকে (Viewer/Staff/Admin) অ্যাক্সেস দেবে"""
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)