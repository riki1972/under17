from django.urls import path
from . import views

app_name = 'Under17'

urlpatterns = [

    path('Under17/squadre/', views.SquadraListView.as_view(), name='squadre_all'),
    path('Under17/<int:pk>/squadra_detail', views.SquadraDetailView.as_view(), name='squadra_detail'),
    path('Under17/squadra_create/', views.SquadraCreateView.as_view(), name='squadra_create'),
    path('Under17/<int:pk>/squadra_update/', views.SquadraUpdateView.as_view(), name='squadra_update'),
    path('Under17/<int:pk>/squadra_delete/', views.SquadraDeleteView.as_view(), name='squadra_delete'),
    path('Under17/calciatori/', views.CalciatoreListView.as_view(), name='calciatori_all'),
    path('Under17/<int:pk>/calciatore_detail', views.CalciatoreDetailView.as_view(), name='calciatore_detail'),
    path('Under17/calciatore_create/', views.CalciatoreCreateView.as_view(), name='calciatore_create'),
    path('Under17/<int:pk>/calciatore_update/', views.CalciatoreUpdateView.as_view(), name='calciatore_update'),
    path('Under17/<int:pk>/calciatore_delete/', views.CalciatoreDeleteView.as_view(), name='calciatore_delete'),
    path('Under17/partite/', views.PartitaListView.as_view(), name='partite_all'),
    path('Under17/<int:pk>/partita_detail', views.PartitaDetailView.as_view(), name='partita_detail'),
    path('Under17/partita_create/', views.PartitaCreateView.as_view(), name='partita_create'),
    path('Under17/<int:pk>/partita_update/', views.PartitaUpdateView.as_view(), name='partita_update'),
    path('Under17/<int:pk>/partita_delete/', views.PartitaDeleteView.as_view(), name='partita_delete'),
    
]