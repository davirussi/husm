from django.contrib import admin
from tenp.models import Paciente, Macronutriente, Micronutriente, Outronutriente, Prescricao, MacronutrientePrescricao, MicronutrientePrescricao, OutronutrientePrescricao
from django import forms
from django.contrib.auth.models import User


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

class MacronutrientePrescricaoInline(admin.TabularInline):
    model = MacronutrientePrescricao
    extra = 1

class MicronutrientePrescricaoInline(admin.TabularInline):
    model = MicronutrientePrescricao
    extra = 1

class OutronutrientePrescricaoInline(admin.TabularInline):
    model = OutronutrientePrescricao
    extra = 1

class PrescricaoAdmin(admin.ModelAdmin):
    list_display= ('nomemedico', 'nomepaciente', 'dataprescricao')
    list_filter = ['nomemedico', 'nomepaciente']
    search_fields = ['nomemedico__username','nomepaciente__nome']
    inlines = (MacronutrientePrescricaoInline,
               MicronutrientePrescricaoInline,
               OutronutrientePrescricaoInline,)
    def render_change_form(self, request, context, *args, **kwargs):
         context['adminform'].form.fields['nomemedico'].queryset = User.objects.filter(is_staff=False)
         context['adminform'].form.fields['nomepaciente'].queryset = Paciente.objects.filter(ativo=True)
         return super(PrescricaoAdmin, self).render_change_form(request, context, args, kwargs)  


# Register your models here.
admin.site.register(Paciente,PacienteAdmin)
admin.site.register(Macronutriente,MacronutrienteAdmin)
admin.site.register(Micronutriente,MicronutrienteAdmin)
admin.site.register(Outronutriente,OutronutrienteAdmin)
admin.site.register(Prescricao, PrescricaoAdmin)
