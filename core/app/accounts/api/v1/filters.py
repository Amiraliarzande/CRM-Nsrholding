import django_filters
from app.accounts.models import User

class UserFilter(django_filters.FilterSet):
    full_name = django_filters.CharFilter(method='filter_full_name', label='Full Name')

    class Meta:
        model = User
        fields = ['type', 'is_active', 'is_verified', 'phone_number']

    def filter_full_name(self, queryset, name, value):
        return queryset.filter(
            first_name__icontains=value
        ) | queryset.filter(
            last_name__icontains=value
        )