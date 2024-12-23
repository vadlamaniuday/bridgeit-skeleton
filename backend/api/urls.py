from django.contrib import admin
from django.urls import path
from .views import list_items

urlpatterns = [
    path("items", list_items),
]
