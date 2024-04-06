from django.urls import path

from FastFoodApp.accounts.views import LogoutAppUserView, LoginAppUserView, UserAccountCreateView, AppUserProfileView, \
    AppUserProfileUpdateView

urlpatterns = (
    path("singup/", UserAccountCreateView.as_view(), name="signup"),
    path("login/", LoginAppUserView.as_view(), name="login"),
    path("logout/", LogoutAppUserView.as_view(), name="logout"),
    path("profile/<int:pk>/", AppUserProfileView.as_view(), name="profile"),
    path("profile/update/<int:pk>/", AppUserProfileUpdateView.as_view(), name="update-profile"),
)
