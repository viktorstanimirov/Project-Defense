
from django.contrib import admin

from FastFoodApp.accounts.forms import AppUserCreationForm
from FastFoodApp.accounts.models import AppUser


@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    add_form = AppUserCreationForm

    list_display = ("username", "email", "first_name", "last_name", "phone_number",
                    "date_of_birth", "is_staff", "is_superuser")
    fields = ("username", "password", "is_staff", "is_superuser", "groups")
    list_filter = ("username", "is_staff", "is_superuser")
    ordering = ("username", "first_name")
    search_fields = ("username", "first_name", "last_name", "phone_number", "is_staff", "is_superuser")

    # def save(self, *args, **kwargs):
    #     if not self.pk:  )
    #         self.set_password(self.password)  # Hash password
    #     super(AppUser, self).save(*args, **kwargs)