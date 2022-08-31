from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, names='index'),
    path('greeting/', views.greeting, names='greeting'),
    path('dinner/', views.dinner, name='dinner'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('hello/<name>/', views.hello, name='hello'),
]
