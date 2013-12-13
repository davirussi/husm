from django.db import models
import datetime

# paciente
class Paciente(models.Model):
    HOMEM = 'H'
    MULHER = 'M'
    SEXO = (
        (HOMEM, 'Homem'),
        (MULHER, 'Mulher'),
    )
    
    nome = models.CharField(max_length=60)
    rg = models.CharField(max_length=12, blank=True, null=True)
    sexo = models.CharField(max_length=1, choices=SEXO, default=HOMEM)    
    datanascimento = models.DateField('Data Nascimento', default=datetime.date.today)
    iniciotratamento = models.DateField('Inicio Tratamento', default=datetime.date.today)
    peso = models.FloatField(default=0.0)
    altura = models.FloatField(blank=True, null=True)
    same = models.CharField(max_length=20, blank=True, null=True)
    convenio = models.CharField(max_length=10, blank=True, default='SUS', null=True)
    prematuro = models.BooleanField(blank=True)
    ativo = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.nome
