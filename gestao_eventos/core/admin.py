from django.contrib import admin
from .models import Evento, Participante, Ingresso, Artista, Feedback

admin.site.register(Evento)
admin.site.register(Participante)
admin.site.register(Ingresso)
admin.site.register(Artista)
admin.site.register(Feedback)
