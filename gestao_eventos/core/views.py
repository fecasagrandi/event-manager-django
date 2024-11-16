from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento, Participante, Ingresso, Feedback, Artista

def listar_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/evento_list.html', {'eventos': eventos})

def listar_participantes(request):
    participantes = Participante.objects.all()
    return render(request, 'eventos/participante_list.html', {'participantes': participantes})

def listar_ingressos(request):
    ingressos = Ingresso.objects.all()
    return render(request, 'eventos/ingresso_list.html', {'ingressos': ingressos})

def listar_artistas(request):
    artistas = Artista.objects.all()
    return render(request, 'eventos/artista_list.html', {'artistas': artistas})

def listar_feedbacks(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'eventos/feedback_list.html', {'feedbacks': feedbacks})

def criar_evento(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        local = request.POST.get('local')
        data = request.POST.get('data')
        Evento.objects.create(nome=nome, local=local, data=data)
        return redirect('listar_eventos')
    return render(request, 'eventos/evento_form.html')

def editar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    if request.method == 'POST':
        evento.nome = request.POST.get('nome')
        evento.local = request.POST.get('local')
        evento.data = request.POST.get('data')
        evento.save()
        return redirect('listar_eventos')
    return render(request, 'eventos/evento_form.html', {'evento': evento})

def deletar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    evento.delete()
    return redirect('listar_eventos')

def criar_participante(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        Participante.objects.create(nome=nome, email=email)
        return redirect('listar_participantes')
    return render(request, 'eventos/participante_form.html')

def editar_participante(request, participante_id):
    participante = get_object_or_404(Participante, id=participante_id)
    if request.method == 'POST':
        participante.nome = request.POST.get('nome')
        participante.email = request.POST.get('email')
        participante.save()
        return redirect('listar_participantes')
    return render(request, 'eventos/participante_form.html', {'participante': participante})

def deletar_participante(request, participante_id):
    participante = get_object_or_404(Participante, id=participante_id)
    participante.delete()
    return redirect('listar_participantes')

def criar_ingresso(request):
    eventos = Evento.objects.all()
    participantes = Participante.objects.all()
    if request.method == 'POST':
        evento_id = request.POST.get('evento')
        participante_id = request.POST.get('participante')
        evento = get_object_or_404(Evento, id=evento_id)
        participante = get_object_or_404(Participante, id=participante_id)
        Ingresso.objects.create(evento=evento, participante=participante)
        return redirect('listar_ingressos')
    return render(request, 'eventos/ingresso_form.html', {'eventos': eventos, 'participantes': participantes})

def deletar_ingresso(request, ingresso_id):
    ingresso = get_object_or_404(Ingresso, id=ingresso_id)
    ingresso.delete()
    return redirect('listar_ingressos')

def criar_feedback(request):
    participantes = Participante.objects.all()
    eventos = Evento.objects.all()
    artistas = Artista.objects.all()
    if request.method == 'POST':
        participante_id = request.POST.get('participante')
        evento_id = request.POST.get('evento')
        artista_id = request.POST.get('artista')
        comentario = request.POST.get('comentario')
        nota = request.POST.get('nota')

        participante = get_object_or_404(Participante, id=participante_id)
        evento = get_object_or_404(Evento, id=evento_id)
        artista = get_object_or_404(Artista, id=artista_id)

        Feedback.objects.create(
            participante=participante,
            evento=evento,
            artista=artista,
            comentario=comentario,
            nota=nota
        )
        return redirect('listar_feedbacks')
    return render(request, 'eventos/feedback_form.html', {
        'participantes': participantes,
        'eventos': eventos,
        'artistas': artistas
    })

def deletar_feedback(request, feedback_id):
    feedback = get_object_or_404(Feedback, id=feedback_id)
    feedback.delete()
    return redirect('listar_feedbacks')

def criar_artista(request):
    eventos = Evento.objects.all()
    if request.method == 'POST':
        nome = request.POST.get('nome')
        biografia = request.POST.get('biografia')
        evento_id = request.POST.get('evento')
        evento = get_object_or_404(Evento, id=evento_id)
        Artista.objects.create(nome=nome, biografia=biografia, evento=evento)
        return redirect('listar_artistas')
    return render(request, 'eventos/artista_form.html', {'eventos': eventos})

def editar_artista(request, artista_id):
    artista = get_object_or_404(Artista, id=artista_id)
    eventos = Evento.objects.all()
    if request.method == 'POST':
        artista.nome = request.POST.get('nome')
        artista.biografia = request.POST.get('biografia')
        evento_id = request.POST.get('evento')
        artista.evento = get_object_or_404(Evento, id=evento_id)
        artista.save()
        return redirect('listar_artistas')
    return render(request, 'eventos/artista_form.html', {'artista': artista, 'eventos': eventos})

def deletar_artista(request, artista_id):
    artista = get_object_or_404(Artista, id=artista_id)
    artista.delete()
    return redirect('listar_artistas')