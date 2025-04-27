from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from apps.users.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (
            'Informações pessoais',
            {
                'fields': (
                    'first_name', 'last_name', 'email', 'picture'
                )
            }
        ),
        # ('Tipo de usuário', {'fields': ('is_customer', 'is_merchant')}),
        ('Datas importantes', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )

    list_display = ('username', 'email', 'first_name', 'last_name')
    search_fields = ('username', 'email')
    ordering = ('username',)


admin.site.unregister(Group)
