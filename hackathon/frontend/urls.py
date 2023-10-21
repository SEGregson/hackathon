from django.urls import path, include
from .views import index

urlpatterns = [
    path('home/', index, name="Index"),
]