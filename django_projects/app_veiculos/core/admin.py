from django.contrib import admin
from core.models import Fabricante, Modelo


@admin.register(Fabricante)
class FabricanteAdmin(admin.ModelAdmin):
  list_display = ('nome', 'pais', 'ano_fundacao', 'idade')
  list_filter = ('pais',)
  search_fields = ('nome', 'pais')


@admin.register(Modelo)
class ModeloAdmin(admin.ModelAdmin):
  list_display = ('nome', 'motor', 'fabricante',)
  list_filter = ('fabricante',)
  search_fields = ('nome', 'fabricante__nome',)
