from django.contrib import admin

from .models import Squadra, Calciatore
from django.utils.html import format_html

@admin.register(Calciatore)
class CalciatoreAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<div style="width:80px; height:80px; overflow: hidden;"><img src="{}" style="width:80px; height:auto;"/></div>'.format(obj.immagine_calciatore.url))

    list_display = ['image_tag', 'cognome_calciatore', 'nome_calciatore', 'ruolo', 'data_di_nascita', 'annata']
    
    #se volessi far visualizzare le voci cognome e nome sulla stessa riga
    #durante la creazione/modfica del calciatore
    #fields = [('cognome', 'nome'), 'data_di_nascita', 'immagine', 'ruolo']
   
    list_filter = ['ruolo']
    search_fields = ['cognome_calciatore', 'nome_calciatore', 'data_di_nascita']
    ordering = ['cognome_calciatore']

@admin.register(Squadra)
class SquadraAdmin(admin.ModelAdmin):

    def image_logo(self, obj):
        return format_html('<div style="width:50px; height:40px; overflow: hidden;"><img src="{}" style="width:auto; height:40px;"/></div>'.format(obj.logo_squadra.url))

    def nome_squadra(self, obj):
        return format_html('<div style="display:grid;justify-item:center;"></div>'.format(obj.nome_squadra))

    list_display = ['image_logo', 'nome_squadra', 'indirizzo', 'mappa', 'orario_partita_di_casa']
    list_filter = ['nome_squadra']
    search_fields = ['nome_squadra']
    ordering = ['nome_squadra']
