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

def listar_participantes(request):
    participantes = Participante.objects.all()
    return render(request, 'eventos/participante_list.html', {'participantes': participantes})

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
