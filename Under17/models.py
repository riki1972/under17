from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User
from django import forms
from django.db.models.functions import Lower
from datetime import date, datetime

class Squadra(models.Model):
    nome_squadra = models.CharField(max_length=100)
    logo_squadra = models.ImageField(upload_to='loghi_squadre/', default='../static/images/shield.png', blank=True)
    indirizzo = models.CharField(max_length=200)
    mappa = models.CharField(max_length=200)
    orario_partita_di_casa = models.TimeField()

    class Meta:
        verbose_name = "Squadra"
        verbose_name_plural = "Squadre"
        ordering = [(Lower('nome_squadra'))] #importo lower in alto e lo inserisco qui, in modo che i calciatori con letter minuscole vadano in ordine alfabetico ugualmente

    def __str__(self):
        return f'{self.nome_squadra}'

    def get_absolute_url(self):
        """Returns the URL to access a particular instance of the model."""
        return reverse('Squadra-detail-view', args=[str(self.id)])


RUOLI = (
    (None, ('Seleziona il Ruolo')),
    ("P", "Portiere"),
    ("D", "Difensore"),
    ("C", "Centrocampista"),
    ("A", "Attaccante"),
)

class Calciatore(models.Model):
    cognome_calciatore = models.CharField(max_length=100, help_text='inserisci il cognome')
    nome_calciatore = models.CharField(max_length=100, help_text='inserisci il nome')
    data_di_nascita = models.DateField(null=False,blank=False)
    immagine_calciatore = models.ImageField(upload_to='foto_calciatori/', default='../static/images/chico.png', blank=True)
    ruolo = models.CharField(
        max_length = 1,
        choices = RUOLI,
        default = 'none',
        help_text= 'ruolo',
        )
    
    class Meta:
        verbose_name = "Calciatore"
        verbose_name_plural = "Calciatori"
        ordering = [(Lower('cognome_calciatore'))] #importo lower in alto e lo inserisco qui, in modo che i calciatori con letter minuscole vadano in ordine alfabetico ugualmente

    def clean(self):
        self.cognome = self.cognome_calciatore.upper()
        self.nome = self.nome_calciatore.upper()

    def __str__(self):
        return f'{self.cognome_calciatore} {self.nome_calciatore}'

    def annata(self):
        return self.data_di_nascita.strftime('%Y')

    def get_absolute_url(self):
        #Returns the URL to access a particular instance of the model.
        return reverse('Calciatore-detail-view', args=[str(self.id)])
    
class Partita(models.Model):
    giornata = models.IntegerField(null=False, unique=True)
    data_partita = models.DateField(null=False,blank=False, default=date.today)
    ora_partita = models.TimeField(null=False,blank=False, default=datetime.now)
    casa = models.ForeignKey('Squadra', related_name='casa', on_delete=models.DO_NOTHING)
    trasferta = models.ForeignKey('Squadra', related_name='trasferta', on_delete=models.DO_NOTHING)
    gol_casa = models.IntegerField(blank=True, default=0)
    gol_trasferta = models.IntegerField(blank=True, default=0)

    class Meta:
        verbose_name = "Partita"
        verbose_name_plural = "Partite"
        # ordering = ['giornata']

    def __str__(self):
        return "{}ª {} {} - {} Vs {} : {} - {}".format(self.giornata, self.data_partita, self.ora_partita, self.casa, self.trasferta, self.gol_casa, self.gol_trasferta)
        # return (f'{self.giornata}ª giornata - {self.casa} Vs {self.trasferta}')

    def match(self):
        return self.data_partita.strftime('%a %d %b %Y')
    
    def get_absolute_url(self):
       """Returns the URL to access a particular instance of the model."""
       return reverse('Partita-detail-view', args=[str(self.id)])