from django.http import HttpResponseForbidden
from django.shortcuts import render


class OwnerPermissionMixin:
    def has_permission(self):
        return bool(self.request.user == self.get_course().owner)

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission():
            return render(request, 'includes/access_denied.html', {'error':'Доступ заборонено', 'status':'403'}, status=403)
        return super().dispatch(request, *args, **kwargs)
