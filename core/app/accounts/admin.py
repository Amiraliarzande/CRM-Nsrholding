from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.contrib.sessions.models import Session

User = get_user_model()


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("id", "phone_number", "first_name", "last_name",
                    "is_superuser", "is_active", "is_verified")
    list_filter = ("is_superuser", "is_active", "is_verified", "type")
    search_fields = ("phone_number", "first_name", "last_name")
    ordering = ("-id",)

    # ✅ این خط رو اضافه کن
    readonly_fields = ("created_date", "updated_date", "last_login")

    fieldsets = (
        (
            "Authentication",
            {"fields": ("phone_number", "password")},
        ),
        (
            "Personal info",
            {"fields": ("first_name", "last_name")},
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "is_verified",
                    "groups",
                    "user_permissions",
                    "type",
                )
            },
        ),
        (
            "Important dates",
            {
                "fields": ("last_login", "created_date", "updated_date"),
            },
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "phone_number",
                    "password1",
                    "password2",
                    "first_name",
                    "last_name",
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "is_verified",
                    "type",
                ),
            },
        ),
    )



class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['session_key', '_session_data', 'expire_date']
    readonly_fields = ['_session_data']
admin.site.register(Session, SessionAdmin)