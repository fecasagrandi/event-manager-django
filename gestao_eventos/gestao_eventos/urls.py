from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('eventos/', views.listar_eventos, name='listar_eventos'),
    path('eventos/criar/', views.criar_evento, name='criar_evento'),
    path('eventos/editar/<int:evento_id>/', views.editar_evento, name='editar_evento'),
    path('eventos/deletar/<int:evento_id>/', views.deletar_evento, name='deletar_evento'),

    path('participantes/', views.listar_participantes, name='listar_participantes'),
    path('participantes/criar/', views.criar_participante, name='criar_participante'),
    path('participantes/editar/<int:participante_id>/', views.editar_participante, name='editar_participante'),
    path('participantes/deletar/<int:participante_id>/', views.deletar_participante, name='deletar_participante'),
    
    path('ingressos/', views.listar_ingressos, name='listar_ingressos'),
    path('ingressos/criar/', views.criar_ingresso, name='criar_ingresso'),
    path('ingressos/deletar/<int:ingresso_id>/', views.deletar_ingresso, name='deletar_ingresso'),
    
    path('feedbacks/', views.listar_feedbacks, name='listar_feedbacks'),
    path('feedbacks/criar/', views.criar_feedback, name='criar_feedback'),
    path('feedbacks/deletar/<int:feedback_id>/', views.deletar_feedback, name='deletar_feedback'),
    
    path('artistas/', views.listar_artistas, name='listar_artistas'),
    path('artistas/criar/', views.criar_artista, name='criar_artista'),
    path('artistas/editar/<int:artista_id>/', views.editar_artista, name='editar_artista'),
    path('artistas/deletar/<int:artista_id>/', views.deletar_artista, name='deletar_artista'),
]