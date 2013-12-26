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
        
        
# macronutriente
class Macronutriente(models.Model):
    TIPOS = (
        ('Aminoacido', 'Aminoacido'),
        ('Carboidrato', 'Carboidrato'),
        ('Glutamina', 'Glutamina'),
        ('Lipideo', 'Lipideo'),
    )
    
    nome = models.CharField(max_length=20)
    tipo = models.CharField(max_length=15, choices=TIPOS, default='Aminoacido')    
    caloria = models.FloatField(default=0.0, verbose_name='calorias em 100ml')
    porcentagemgrama = models.FloatField(default=0.0, verbose_name="gramas em 100ml")
    
    def __unicode__(self):
        return self.nome
        

# micronutrientes
class Micronutriente(models.Model):
    TIPOS = (
        ('Calcio', 'Calcio'),
        ('Fosforo', 'Fosforo'),
        ('Magnesio', 'Magnesio'),
        ('Sodio', 'Sodio'),
        ('Potassio', 'Potassio'),
    )
    
    nome = models.CharField(max_length=20)
    tipo = models.CharField(max_length=15, choices=TIPOS, default='Calcio')    
    caloria = models.FloatField(default=0.0, verbose_name='calorias em 100ml')
    meq = models.FloatField(default=0.0, verbose_name=" mEq em 100ml")
    meqsodio = models.FloatField(default=0.0, verbose_name=" mEq de sodio em 100ml")
    
    def __unicode__(self):
        return self.nome
        
        
# macronutriente
class Outronutriente(models.Model):
    TIPOS = (
        ('Oligoelementos', 'Oligoelementos'),
        ('Zinco', 'Zinco'),
        ('Selenio', 'Selenio'),
        ('Agua Destilada', 'Agua Destilada'),
    )
    
    nome = models.CharField(max_length=20)
    tipo = models.CharField(max_length=15, choices=TIPOS, default='Oligoelemento')    
    caloria = models.FloatField(default=0.0, verbose_name='calorias em 100ml')
    porcentagemgrama = models.FloatField(default=0.0, verbose_name="gramas em 100ml")
    
    def __unicode__(self):
        return self.nome

    
