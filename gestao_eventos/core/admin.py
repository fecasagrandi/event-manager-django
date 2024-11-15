from django.contrib import admin
from .models import Evento, Participante, Ingresso, Palestrante, Feedback

admin.site.register(Evento)
admin.site.register(Participante)
admin.site.register(Ingresso)
admin.site.register(Palestrante)
admin.site.register(Feedback)
