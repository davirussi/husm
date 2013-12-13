from django.contrib import admin
from tenp.models import Paciente, Macronutriente


class PacienteAdmin(admin.ModelAdmin):
    list_display= ('nome', 'sexo', 'peso','ativo', 'iniciotratamento')
    list_filter = ('ativo', 'nome')
    list_editable = ['ativo']
    search_fields = ['nome']
    
class MacronutrienteAdmin(admin.ModelAdmin):
    list_display= ('nome', 'tipo', 'caloria','porcentagemgrama')
    list_filter = ['tipo']
    list_editable = ['caloria','porcentagemgrama']
    search_fields = ['nome']    
    
# Register your models here.
admin.site.register(Paciente,PacienteAdmin)
admin.site.register(Macronutriente,MacronutrienteAdmin)
