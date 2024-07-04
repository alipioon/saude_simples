from rest_framework import serializers
from .models import Menu, SubMenu

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['nome', 'id', 'tipo']

class SubMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubMenu
        fields = ['id', 'menu_id', 'classe', 'link']
        # ordering_fields = ('id')

