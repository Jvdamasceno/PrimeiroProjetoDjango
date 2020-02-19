from django.contrib import admin
from .models import Cardapio
# Register your models here.


@admin.register(Cardapio)
class CardapioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'imagem', 'preco')
