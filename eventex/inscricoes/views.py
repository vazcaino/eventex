from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string

from eventex.inscricoes.forms import FormInscricoes


def inscrever(request):
    if request.method == 'POST':
        form = FormInscricoes(request.POST)

        if form.is_valid():
            body = render_to_string('inscricoes/email_inscricao.txt', form.cleaned_data)

            mail.send_mail('Confirmação de inscrição',
                           body,
                           'vazcaino@gmail.com',
                           ['vazcaino@gmail.com', form.cleaned_data['email']])

            messages.success(request, 'Inscrição realizada com sucesso!')

            return HttpResponseRedirect('/inscricao/')
        else:
            return render(request, 'inscricoes/form_inscricao.html', {'form': form})
    else:
        return render(request, 'inscricoes/form_inscricao.html', {'form': FormInscricoes()})
