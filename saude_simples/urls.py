"""saude_simples URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from menu.views import logar, menu

#urlpatterns = [
#    url(r'^admin/', admin.site.urls),
#    url('', admin.site.urls),
#
#]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('menu.urls')),
    path('menu/', include('menu.urls')),
    path('cadastros/', include('cadastros.urls')),
    path('', logar),
    path('login/', logar),
    path('menu/', menu),
    path('chaining/', include('smart_selects.urls')),
    ]
