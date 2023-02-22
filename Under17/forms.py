from django import forms
from .models import Squadra, Calciatore
from django.contrib import messages
    
class SquadraForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label

    class Meta:
        model = Squadra
        fields = ('nome_squadra', 'logo_squadra', 'indirizzo', 'mappa', 'orario_partita_di_casa')

        widgets = {

            'nome_squadra' : forms.InputField(max_length=100)
            'logo_squadra' : forms.FileField(upload_to='loghi_squadre/')
            'indirizzo' : forms.InputField(max_length=200)
            'mappa' : forms.InputField(max_length=200)
            'orario_partita_di_casa' : models.TimeField()

        }

class CalciatoreForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label

    class Meta:
        model = Calciatore
        fields = ('cognome_calciatore', 'nome_calciatore', 'data_di_nascita', 'immagine_calciatore', 'ruolo')

        widgets = {

            'cognome_calciatore' : forms.InputField(max_length=100)
            'nome_calciatore' : forms.InputField(max_length=100,)
            'data_di_nascita' : models.DateField()
            'immagine_calciatore' : forms.FileField(upload_to='loghi_squadre/', default='../static/images/chico.png', blank=True)
            'indirizzo' : forms.InputField(max_length=200)

        }
        