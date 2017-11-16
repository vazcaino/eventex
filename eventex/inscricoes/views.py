from django.conf import settings
from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string

from eventex.inscricoes.forms import FormInscricoes


def inscrever(request):
    if request.method == 'POST':
        return criar(request)
    else:
        return novo(request)


def criar(request):
    form = FormInscricoes(request.POST)

    if not form.is_valid():
        return render(request, 'inscricoes/form_inscricao.html', {'form': form})

    _enviar_email('Confirmação de inscrição',
                  settings.DEFAULT_FROM_EMAIL,
                  form.cleaned_data['email'],
                  'inscricoes/email_inscricao.txt',
                  form.cleaned_data)

    messages.success(request, 'Inscrição realizada com sucesso!')

    return HttpResponseRedirect('/inscricao/')


def novo(request):
    return render(request, 'inscricoes/form_inscricao.html', {'form': FormInscricoes()})


def _enviar_email(subject, from_, to_, template_name, context):
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, from_, [from_, to_])