from django.urls import path
from . import views

urlpatterns = [
    path('tiponormas/', views.TipoNormas),
    # path('logout/', views.logout_user),
    # path('login/submit', views.autenticar),
    #path('municipe/', views.municipes, name='municipes')
]