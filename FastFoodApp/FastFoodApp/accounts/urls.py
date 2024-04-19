from django.urls import path

from FastFoodApp.accounts.views import LoginAppUserView, UserAccountCreateView, AppUserProfileView, \
    AppUserProfileUpdateView, logout_user, appsuser_delete

urlpatterns = (
    path("singup/", UserAccountCreateView.as_view(), name="signup"),
    path("login/", LoginAppUserView.as_view(), name="login"),
    path("logout/", logout_user, name="logout"),
    path("profile/<int:pk>/", AppUserProfileView.as_view(), name="profile"),
    path("profile/update/<int:pk>/", AppUserProfileUpdateView.as_view(), name="update-profile"),
    path("profile/delete/<int:pk>/",  appsuser_delete, name="delete-profile"),
)
