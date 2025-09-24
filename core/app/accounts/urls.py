from django.urls import path
from app.accounts import views
urlpatterns = [
    path('', views.home, name='home'),
]
