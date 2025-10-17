from django.urls import path,include
from django.conf import settings
from app.crm.api.v1.views import CallReportViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('call-reports', CallReportViewSet, basename='callreport')
urlpatterns = router.urls