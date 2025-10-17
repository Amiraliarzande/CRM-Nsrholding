from django_filters.rest_framework import DjangoFilterBackend, FilterSet, ChoiceFilter
from app.crm.models import CallReport

class CallReportFilter(FilterSet):
    
    validation = ChoiceFilter(
        field_name='validation__name', 
        choices=[('خوب','خوب'), ('متوسط','متوسط'), ('بد','بد')]
    )

    class Meta:
        model = CallReport
        fields = ['validation']