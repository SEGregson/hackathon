# url boiler plate djangofrom django.urls import path
from .views import *
from django.urls import path

urlpatterns = [
    path('index/', index, name='index'),
    path('getInfo/', getInfo, name='getInfo'),
]
