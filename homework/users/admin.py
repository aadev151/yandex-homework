from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from users.forms import EmailUserChangeForm, EmailUserCreationForm
from users.models import User


class UserAdmin(BaseUserAdmin):
    add_form = EmailUserCreationForm
    form = EmailUserChangeForm
    model = User
    ordering = ('email',)
    list_display = ('email', 'is_staff', 'is_active', 'birthday',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Статус', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'email',
                    'password1',
                    'password2',
                    'is_staff',
                    'is_active'
                )
            }
        ),
    )


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
