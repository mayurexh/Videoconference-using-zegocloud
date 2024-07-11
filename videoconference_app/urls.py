from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [ 
    path("", views.home_view, name = "home"),
    path("register/", views.register_view, name= "register"),
    path("logout/", views.logout_view, name="logout"),
    path("dashboard/", views.dashboard_view, name= "dashboard"),
    path("login/", auth_views.LoginView.as_view(template_name= "login.html"), name= "login"),
    path("meeting/", views.videocall, name="meeting"),
    path("joinroom/", views.joinroom, name="joinroom")

]