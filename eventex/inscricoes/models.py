from django.db import models

class Inscricao(models.Model):
    name = models.CharField('nome', max_length=100)
    cpf = models.CharField('cpf',max_length=11)
    email = models.EmailField('e-mail')
    phone = models.CharField('fone',max_length=20)
    criado_em = models.DateTimeField('criado em',auto_now_add=True)

    class Meta:
        verbose_name = 'inscrição'
        verbose_name_plural = 'inscrições'
        ordering = ('-criado_em',)

    def __str__(self):
        return self.name