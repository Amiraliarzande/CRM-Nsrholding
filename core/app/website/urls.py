from django.contrib import admin
from django.urls import path,include
from app.website import views

urlpatterns = [
    path("", views.index_view, name="index"),
    path("about/", views.about_view, name="about"),
    path("contact/", views.contact_view, name="contact"),
    path("amenities/", views.amenities_view, name="amenities"),
    path("location/", views.location_view, name="location"),
    path("rooms/", views.rooms_view, name="rooms"),
]