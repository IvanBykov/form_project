from django.contrib import admin
from django.urls import path
from .views import index, done

urlpatterns = [
    path('', index),
    path('done', done)
]
