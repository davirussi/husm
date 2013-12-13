from django.contrib import admin
from tenp.models import Paciente


class PacienteAdmin(admin.ModelAdmin):
    list_display= ('nome', 'sexo', 'peso','ativo', 'iniciotratamento')
    list_filter = ('ativo', 'nome')
    list_editable = ['ativo']
    search_fields = ['nome']
    
# Register your models here.
admin.site.register(Paciente,PacienteAdmin)
