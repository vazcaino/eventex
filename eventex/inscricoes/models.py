from django.db import models

class Inscricao(models.Model):
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    criado_em = models.DateTimeField(auto_now_add=True)