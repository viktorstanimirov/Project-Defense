
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AppUser


@admin.register(AppUser)
class CustomUserAdmin(UserAdmin):
    model = AppUser

    def get_fieldsets(self, request, obj=None):
        default_fields = sum([list(fields) for name, fields in super().get_fieldsets(request, obj)], [])

        custom_fields = [field.name for field in AppUser._meta.fields if
                         field.name not in default_fields and field.editable and not field.many_to_many and not field.auto_created]

        fieldsets = super().get_fieldsets(request, obj) + [
            ('AppUser Fields', {'fields': custom_fields}),
        ]
        return fieldsets

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if not obj:  # Adding a new object
            default_fields = sum([list(fields) for name, fields in self.add_fieldsets], [])
            custom_fields = [field.name for field in AppUser._meta.fields if
                             field.name not in default_fields and field.editable and not field.many_to_many and not field.auto_created]
            self.add_fieldsets = self.add_fieldsets + [
                ('AppUser Fields', {'fields': custom_fields}),
            ]
        return form

