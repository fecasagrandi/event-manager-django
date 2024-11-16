from django.db import models

class Evento(models.Model):
    nome = models.CharField(max_length=100)
    local = models.CharField(max_length=150)
    data = models.DateTimeField()

    def __str__(self):
        return self.nome

class Participante(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome

class Ingresso(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE)
    data_compra = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ingresso para {self.evento.nome} - {self.participante.nome}"

class Artista(models.Model):
    nome = models.CharField(max_length=100)
    biografia = models.TextField()
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Feedback(models.Model):
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    comentario = models.TextField()
    nota = models.IntegerField()

    def __str__(self):
        return f"Feedback de {self.participante.nome} para {self.artista.nome}"
