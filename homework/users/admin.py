from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Profile


class ProfileInlined(admin.StackedInline):
    model = Profile
    max_num = 1
    min_num = 1
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInlined, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
