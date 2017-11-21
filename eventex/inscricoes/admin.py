from django.contrib import admin
from django.utils.timezone import now

from eventex.inscricoes.models import Inscricao

class InscricaoModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'cpf', 'criado_em',
                    'inscritos_hoje')
    date_hierarchy = 'criado_em'
    search_fields = ('name', 'email', 'phone', 'cpf', 'criado_em')
    list_filter = ('criado_em',)

    def inscritos_hoje(self, obj):
        return obj.criado_em == now().date()

    inscritos_hoje.short_description = 'inscrito hoje?'
    inscritos_hoje.boolean = True

admin.site.register(Inscricao, InscricaoModelAdmin)