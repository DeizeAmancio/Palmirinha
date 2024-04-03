from django.contrib import admin
from ReceitaApp.models import Categoria, Receita

# Register your models here.
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ['Nome', 'Ingredientes', 'Modo_de_Preparo', 'Grau_de_Dificuldade','Categoria']
    list_display_links = ['Categoria', 'Nome']
    list_filter = ['Nome']
    search_fields = ['Nome']


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['Nome']
    list_display_links = ['Nome']
    search_fields =['Nome']


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Receita, ReceitaAdmin)
