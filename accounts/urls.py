from django.urls import path

from . import views

urlpatterns = [
    path('token', views.sendToken),
    path('signup', views.signup),
    path('login', views.login),
    path('logout', views.logout),
]
