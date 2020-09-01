from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Client, License
from django.utils import timezone
from datetime import timedelta, date
import datetime
from .call_triggers import trigger, email_para_enviar
# Create your views here.


def index(request):
    """ renderiza index """
    return render(request, 'index.html')


@csrf_exempt
def valida(request):
    """ executa a validação e retorna para tela """
    trigger()
    return render(request, 'valida.html', {'email_para_enviar': email_para_enviar})
