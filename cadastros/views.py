from django.shortcuts import render
# from menu.models import Menu, SubMenu
# from menu.serializers import MenuSerializer, SubMenuSerializer


def TipoNormas(request):

    return render(request, 'tiponormas.html')
