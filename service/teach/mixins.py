from django.http import HttpResponseForbidden


class OwnerPermissionMixin:
    def has_permission(self):
        return bool(self.request.user == self.get_object().owner)

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission():
            return HttpResponseForbidden("Ви не власник цього курса")
        return super().dispatch(request, *args, **kwargs)