from django.conf import settings
from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template.loader import render_to_string

from eventex.inscricoes.forms import FormInscricoes
from eventex.inscricoes.models import Inscricao


def inscrever(request):
    if request.method == 'POST':
        return criar(request)
    else:
        return novo(request)


def criar(request):
    form = FormInscricoes(request.POST)

    if not form.is_valid():
        return render(request, 'inscricoes/form_inscricao.html', {'form': form})

    inscricao = Inscricao.objects.create(**form.cleaned_data)

    body = render_to_string('inscricoes/email_inscricao.txt', {'inscricao': inscricao})

    _enviar_email('Confirmação de inscrição',
                  settings.DEFAULT_FROM_EMAIL,
                  inscricao.email,
                  body,
                  )

    return HttpResponseRedirect('/inscricao/{}/'.format(inscricao.pk))


def novo(request):
    return render(request, 'inscricoes/form_inscricao.html', {'form': FormInscricoes()})


def detalhe(request, pk):
    try:
        inscricao = Inscricao.objects.get(pk=pk)
    except Inscricao.DoesNotExist:
        raise Http404


    return render(request, 'inscricoes/inscricao_detalhe.html', {'inscricao': inscricao})


def _enviar_email(subject, from_, to_, body):
    mail.send_mail(subject, body, from_, [from_, to_])