from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect


class RestrictedAppUserAccessMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser and request.user.pk != kwargs["pk"]:
            messages.info(request, "You have not access to this page!")
            return redirect("home page")

        return super().dispatch(request, *args, **kwargs)


class LogoutRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, "You are already logged in to the site!")
            return redirect("index")

        return super().dispatch(request, *args, **kwargs)