from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.logar, name='logar'),
    path('logout/', views.logout_user),
    path('submit', views.autenticar),
    path('login/submit', views.autenticar),
    path('menu', views.menu, name='menu')
]