from django.core import serializers
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Menu, SubMenu
from .serializers import MenuSerializer, SubMenuSerializer
from django.db.models import Avg, Count, Min, Sum
from django.http import HttpResponse


def logar(request):
    request.session['mainM'] = ''
    request.session['subM'] = ''
    return render(request, 'login.html', {})

def menu(request):
     # try:
        var01 = Menu.objects.all()
        mainmenu = MenuSerializer(var01, many=True)
        data = mainmenu.data
        request.session['mainM'] = data

        var02 = SubMenu.objects.all()
        submenu = SubMenuSerializer(var02, many=True)
        data = submenu.data
        request.session['subM'] = data

        return render(request, 'index.html', {})

     # except Exception as identifier:
     #    return render(request, 'index.html', {})

# @login_required(login_url='/login/')
@csrf_protect
def autenticar(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        #print(username)
        #print(password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/menu/')
        else:
            messages.error(request, 'Usuário ou Senha invalido(s)....')
            return redirect('/login/')

def logout_user(request):
    logout(request)
    return redirect('/login/')