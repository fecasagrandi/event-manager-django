from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.listar_eventos, name='listar_eventos'),
    path('eventos/', views.listar_eventos, name='listar_eventos'),
    path('eventos/criar/', views.criar_evento, name='criar_evento'),
    path('participantes/', views.listar_participantes, name='listar_participantes'),
    path('eventos/editar/<int:evento_id>/', views.editar_evento, name='editar_evento'),
    path('eventos/deletar/<int:evento_id>/', views.deletar_evento, name='deletar_evento'),
]
