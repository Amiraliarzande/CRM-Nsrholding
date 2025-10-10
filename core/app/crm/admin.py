from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.db.models import Q
from .models import CallReport, FieldActivity

class FieldActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')  
    search_fields = ('name',)          
    list_filter = ('parent',)          
    ordering = ('parent', 'name') 

class CallReportAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'field_activity', 'province', 'city', 'purchase_satisfaction', 'validation', 'last_purchase')
    list_filter = ('field_activity', 'province', 'city', 'purchase_satisfaction', 'validation')
    search_fields = ('number', 'name', 'province', 'city')
    ordering = ('-number',)

admin.site.register(FieldActivity, FieldActivityAdmin)
admin.site.register(CallReport, CallReportAdmin)