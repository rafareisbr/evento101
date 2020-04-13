from django.shortcuts import render

from .models import Evento, Inscricao, TipoInscricao


# Create your views here.
def index(request):
    tipoInscricao = TipoInscricao.objects.all()
    eventos = Evento.objects.all()
    return render(
        request, 'inscricoes/index.html', 
        { 'eventos': eventos, 'tiposEvento': tipoInscricao }
    )