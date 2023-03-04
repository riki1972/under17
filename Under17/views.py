from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Squadra, Calciatore, Partita
from django.utils import timezone
from datetime import date, datetime

class SquadraBaseView(View):
    model = Squadra
    fields = '__all__'
    success_url = reverse_lazy('Under17:squadre_all')

class SquadraListView(SquadraBaseView, ListView):
    model = Squadra

class SquadraDetailView(SquadraBaseView, DetailView):
    model = Squadra

class SquadraCreateView(SquadraBaseView, CreateView):
    model = Squadra

class SquadraUpdateView(SquadraBaseView, UpdateView):
    model = Squadra

class SquadraDeleteView(SquadraBaseView, DeleteView):
    model = Squadra

class CalciatoreBaseView(View):
    model = Calciatore
    fields = '__all__'
    success_url = reverse_lazy('Under17:calciatori_all')

class CalciatoreListView(CalciatoreBaseView, ListView):
    model = Calciatore

class CalciatoreDetailView(CalciatoreBaseView, DetailView):
    model = Calciatore

class CalciatoreCreateView(CalciatoreBaseView, CreateView):
    model = Calciatore

class CalciatoreUpdateView(CalciatoreBaseView, UpdateView):
    model = Calciatore

class CalciatoreDeleteView(CalciatoreBaseView, DeleteView):
    model = Calciatore

class PartitaBaseView(View):
    model = Partita
    fields = '__all__'
    success_url = reverse_lazy('Under17:partite_all')

class PartitaListView(PartitaBaseView, ListView):
    model = Partita

    def get_context_data(self, **kwargs):
       context_data = super().get_context_data(**kwargs)
       context_data['dopo'] = Partita.objects.filter(data_partita__gte=timezone.now()).order_by('data_partita')
       context_data['prima'] = Partita.objects.filter(data_partita__lte=timezone.now()).order_by('-data_partita')
       return context_data

class PartitaDetailView(PartitaBaseView, DetailView):
    model = Partita

class PartitaCreateView(PartitaBaseView, CreateView):
    model = Partita

class PartitaUpdateView(PartitaBaseView, UpdateView):
    model = Partita

class PartitaDeleteView(PartitaBaseView, DeleteView):
    model = Partita

