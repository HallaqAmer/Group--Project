from django.urls import path
from . import views

app_name = 'login_app'

urlpatterns = [
    path('', views.call_home, name="home"),
    path('about', views.call_about, name="about"),
    path('pricing', views.call_pricing, name="price"),
    path('login', views.call_login, name="login"),

]