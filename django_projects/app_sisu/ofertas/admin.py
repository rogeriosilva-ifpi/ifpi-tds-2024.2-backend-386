from django.contrib import admin
from ofertas.models import Universidade, Curso

# admin.site.register(Universidade)

@admin.register(Universidade)
class UniversidadeAdmin(admin.ModelAdmin):
    list_display = ('sigla', 'nome', 'cidade', 'uf', 'qtd_curso')
    search_fields = ('nome', 'cidade', 'uf')
    list_filter = ('uf',)


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'area', 'universidade')
    search_fields = ('nome', 'area')
    list_filter = ('area',)
