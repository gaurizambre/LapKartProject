from django.urls import path
from .import views

urlpatterns = [
    path("register/",views.registerview),
    path("login/",views.login_view),
    path("logout/",views.logout_view),
    path("home/",views.homeview),
]