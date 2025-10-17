from django.http import HttpResponse
from django.shortcuts import render


from rest_framework import viewsets

from app.crm.models import CallReport
from app.crm.api.v1.filters import CallReportFilter
from app.crm.api.v1.serializer import CallReportSerializer
from app.crm.api.v1.paginations import CustomPagination

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class CallReportViewSet(viewsets.ModelViewSet):
   
    queryset = CallReport.objects.all().order_by('-created_at')
    serializer_class = CallReportSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = CallReportFilter  
    search_fields = ['name', 'number', 'province', 'city']
    ordering_fields = ['created_at', 'name']

    # Add custom pagination
    pagination_class = CustomPagination

