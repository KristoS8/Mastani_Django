from django.urls import path

from . import views

app_name = "Home"

urlpatterns = [
    path('', views.index, name=""),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register")
]