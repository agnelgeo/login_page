from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('signup', views.signup, name='SignUp'),
    path('signin', views.signin, name='SignIn'),
    path('signout', views.signout, name='SignOut'),
    path('forgotpass', views.forgotpass, name='forgotpass')
]
