from django.contrib.auth.mixins import AccessMixin

class LoginAndOrganisationRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:# and request.user.is_organization:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)