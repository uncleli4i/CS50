from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('invent', views.invent, name="invent"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
 
]