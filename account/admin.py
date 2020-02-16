from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User, UserProfile


class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ['id', 'username', 'first_name', 'last_name',
                    'phone', 'email', 'lekki', 'ikoyi', 'eko_atlantic', 'is_employer']
    fieldsets = (
        (('User'), {'fields': ('username', 'phone',
                               'email', 'first_name', 'last_name', 'lekki', 'ikoyi', 'eko_atlantic', 'is_employer')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')})
    )

    list_filter = ['is_employer', 'eko_atlantic', 'ikoyi', 'lekki']

admin.site.register(User, UserAdmin)
admin.site.register(UserProfile)


