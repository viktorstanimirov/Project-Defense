from django.contrib import messages
from django.contrib.auth import views as auth_views, get_user_model, logout
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views import generic as view

from FastFoodApp.accounts.forms import AppUserCreationForm, LoginAppUserForm, UpdateAppUserForm

UserModel = get_user_model()


class UserAccountCreateView(view.CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = "accounts/create-profile.html"
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginAppUserView(auth_views.LoginView):
    template_name = "accounts/login.html"
    form_class = LoginAppUserForm

    def get_success_url(self):
        user = self.request.user
        if not user.first_name or not user.last_name or not user.email:
            return reverse("menu")
        return super().get_success_url()

    def form_valid(self, form):
        valid = super().form_valid(form)
        return redirect(self.get_success_url())


def logout_user(request):
    logout(request)

    return redirect("index")


class AppUserProfileView(view.DetailView):
    model = UserModel
    template_name = 'accounts/profile.html'
    context_object_name = 'appsuser'

    def get_object(self):
        pk = self.kwargs.get('pk')
        if pk:
            return get_object_or_404(UserModel, pk=pk)
        else:
            return self.request.user


class AppUserProfileUpdateView(SuccessMessageMixin, view.UpdateView):
    model = UserModel
    form_class = UpdateAppUserForm

    template_name = "accounts/update-profile.html"

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


def appsuser_delete(request, pk):
    appsuser = get_object_or_404(UserModel, pk=pk)
    if request.method == "POST":
        appsuser.delete()

        return redirect("index")
    return render(request, "accounts/delete-profile.html", {"appsuser": appsuser})


