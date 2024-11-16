from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento, Participante

def listar_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/evento_list.html', {'eventos': eventos})

def listar_participantes(request):
    participantes = Participante.objects.all()
    return render(request, 'eventos/participante_list.html', {'participantes': participantes})

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
