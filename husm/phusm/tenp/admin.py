from django.contrib import admin
from tenp.models import Paciente, Macronutriente, Micronutriente, Outronutriente
from django import forms


class PacienteAdmin(admin.ModelAdmin):
    list_display= ('nome', 'sexo', 'peso','ativo', 'iniciotratamento')
    list_filter = ('ativo', 'nome')
    list_editable = ['ativo']
    search_fields = ['nome']
    
class MacronutrienteAdmin(admin.ModelAdmin):
    list_display= ('nome', 'tipo', 'caloria','porcentagemgrama')
    #fields = ('nome', 'tipo', 'caloria','porcentagemgrama')
    list_filter = ['tipo']
    list_editable = ['caloria','porcentagemgrama']
    search_fields = ['nome']    


class OutronutrienteAdmin(admin.ModelAdmin):
    list_display= ('nome', 'tipo', 'caloria','porcentagemgrama')
    #fields = ('nome', 'tipo', 'caloria','porcentagemgrama')
    list_filter = ['tipo']
    list_editable = ['caloria','porcentagemgrama']
    search_fields = ['nome']    

class MyMicronutrienteForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super(MyMicronutrienteForm, self).clean()
        tipo = cleaned_data.get("tipo")
        meqsodio = cleaned_data.get("meqsodio")
        if tipo=='Sodio':
            if meqsodio!=0.0:
                raise forms.ValidationError("Quando tipo Sodio for selecionado campo meq de sodio precisa ser igual a 0.0")
        return self.cleaned_data    

          
class MicronutrienteAdmin(admin.ModelAdmin):
    list_display= ('nome', 'tipo', 'caloria','meq','meqsodio')
    list_filter = ['tipo']
    list_editable = ['caloria','meq']
    search_fields = ['nome']
    form = MyMicronutrienteForm 
    
    class Media:
        js = (
            'js/admin-forms.js',
        ) 

# Register your models here.
admin.site.register(Paciente,PacienteAdmin)
admin.site.register(Macronutriente,MacronutrienteAdmin)
admin.site.register(Micronutriente,MicronutrienteAdmin)
admin.site.register(Outronutriente,OutronutrienteAdmin)
