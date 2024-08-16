from django.contrib import admin
from .models import *

@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('cat_number', 'cliente')

@admin.register(Ordem)
class OrdemAdmin(admin.ModelAdmin):
    list_display = ('cat_number', 'cliente')

@admin.register(Start)
class StartAdmin(admin.ModelAdmin):
    list_display = ('cat_number', 'cliente')

@admin.register(Servicos)
class ServicosAdmin(admin.ModelAdmin):
    list_display = ('cat_number', 'cliente')

@admin.register(Pressurizador)
class PressurizadorAdmin(admin.ModelAdmin):
    list_display = ('cat_number', 'cliente')

@admin.register(Filtros)
class FiltrosAdmin(admin.ModelAdmin):
    list_display = ('cat_number', 'cliente')

@admin.register(Dosagem)
class DosagemAdmin(admin.ModelAdmin):
    list_display = ('cat_number', 'cliente')

@admin.register(Desmi)
class DesmiAdmin(admin.ModelAdmin):
    list_display = ('cat_number', 'cliente')

@admin.register(Osmose)
class OsmoseAdmin(admin.ModelAdmin):
    list_display = ('cat_number', 'cliente')

@admin.register(Leito)
class LeitoAdmin(admin.ModelAdmin):
    list_display = ('cat_number', 'cliente')

@admin.register(Afericao)
class AfericaoAdmin(admin.ModelAdmin):
    list_display = ('cat_number', 'cliente')

@admin.register(Ozonio)
class OzonioAdmin(admin.ModelAdmin):
    list_display = ('cat_number', 'cliente')

@admin.register(Uv)
class UvAdmin(admin.ModelAdmin):
    list_display = ('cat_number', 'cliente')

@admin.register(Recup_Rejeito)
class RecupRejeitoAdmin(admin.ModelAdmin):
    list_display = ('cat_number', 'cliente')

@admin.register(Analise_Agua)
class AnaliseAguaAdmin(admin.ModelAdmin):
    list_display = ('cat_number', 'cliente')
