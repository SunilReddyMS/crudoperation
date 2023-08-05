
from django.contrib import admin
from django.urls import path


from . import views

urlpatterns = [
    path("",views.index, name="home" ),
    path("register", views.register_request),
    path("loginpage", views.loginpage,name="loginpage"),
    path("signuppage", views.signuppage,name="signuppage"),
]
     

