from django.contrib import admin
from .models import usuario

@admin.register(usuario)
class usuarioAdmin(admin.ModelAdmin):
    list_display = ('login', 'email','id' )
    search_fields = ['login', 'email']
    list_per_page = 20