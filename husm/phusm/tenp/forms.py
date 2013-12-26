from django import forms
from tenp.models import Prescricao

class PrescreverForm(forms.ModelForm):
    #name = forms.CharField(max_length=128, help_text="Please enter the gategory name")
    #fluido = forms.FloatField(initial=0.0)
    #likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    
    class Meta:
        model = Prescricao
