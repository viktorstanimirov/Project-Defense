from django.contrib.auth import views as auth_views, get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView

from FastFoodApp.accounts.forms import AppUserCreationForm, LoginAppUserForm, UpdateAppUserForm

UserModel = get_user_model()


class UserAccountCreateView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = "profiles/create-profile.html"
    success_url = reverse_lazy('menu')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginAppUserView(auth_views.LoginView):
    template_name = "profiles/login.html"
    form_class = LoginAppUserForm
    success_url = reverse_lazy("index")


class LogoutAppUserView(LogoutView):
    next_page = reverse_lazy('home')


class AppUserProfileView(DetailView):
    model = UserModel
    template_name = 'profiles/profile.html'
    context_object_name = 'appsuser'

    def get_object(self):
        pk = self.kwargs.get('pk')
        if pk:
            return get_object_or_404(UserModel, pk=pk)
        else:
            return self.request.user


class AppUserProfileUpdateView(SuccessMessageMixin, UpdateView):
    model = UserModel
    form_class = UpdateAppUserForm
    success_message = "The profile was successfully edited!"
    template_name = "profiles/update-profile.html"

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        return reverse("profile", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.username = self.request.user.username
        form.instance.email = self.request.user.email
        form.save()
        return super().form_valid(form)
