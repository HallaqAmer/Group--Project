from django.urls import path
from . import views

app_name = 'GYMapp'

urlpatterns = [
    path('', views.base,name='base'),
    path('hola',views.dashboard,name='dashboard'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('clear', views.clear, name='clear'),
]
