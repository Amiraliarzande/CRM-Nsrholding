from django.urls import path,include
from django.conf import settings

urlpatterns = [
    path('api/v1/', include('app.crm.api.v1.urls')),
]
