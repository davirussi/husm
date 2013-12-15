import os
import sys

def populate():
    python_cat = add_cat('Python',
        views=128,
        likes=64)

    add_page(cat=python_cat,
        title="Official Python Tutorial",
        url="http://docs.python.org/2/tutorial/")

    add_macronutriente(
        nome='Aminoacidos a 10%',
        tipo='Aminoacido',
        caloria='0.0',
        porcentagemgrama='10'
    )
    
    add_macronutriente(
        nome='SG 5%',
        tipo='Carboidrato',
        caloria='0.0',
        porcentagemgrama='5'
    )
    add_macronutriente(
        nome='SG 10%',
        tipo='Carboidrato',
        caloria='0.0',
        porcentagemgrama='10'
    )
    add_macronutriente(
        nome='SG 50%',
        tipo='Carboidrato',
        caloria='0.0',
        porcentagemgrama='50'
    )    
    add_macronutriente(
        nome='Lipidio 10%',
        tipo='Lipidio',
        caloria='0.0',
        porcentagemgrama='10'
    )    
    add_macronutriente(
        nome='Lipidio 20%',
        tipo='Lipidio',
        caloria='0.0',
        porcentagemgrama='20'
    )    
    add_macronutriente(
        nome='Glutamina 20%',
        tipo='Glutamina',
        caloria='0.0',
        porcentagemgrama='20'
    )
    add_micronutriente(
        nome='NaCl 20%',
        tipo='Sodio',
        caloria='0.0',
        meq='2',
        meqsodio='0'
    )
    add_micronutriente(
        nome='kCl 10%',
        tipo='Potassio',
        caloria='0.0',
        meq='1',
        meqsodio='0'
    )
    add_micronutriente(
        nome='Sulfato Mg 50%',
        tipo='Magnesio',
        caloria='0.0',
        meq='5',
        meqsodio='0'
    )
    add_micronutriente(
        nome='Gluconato Ca 10%',
        tipo='Calcio',
        caloria='0.0',
        meq='1',
        meqsodio='0'
    )
    add_micronutriente(
        nome='Fosforo',
        tipo='Fosforo',
        caloria='0.0',
        meq='1',
        meqsodio='0'
    )
    # Print out what we have added to the user.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))



def add_macronutriente(nome,tipo,caloria,porcentagemgrama):
    c = Macronutriente.objects.get_or_create(nome=nome, tipo=tipo, caloria=caloria, porcentagemgrama=porcentagemgrama)[0]
    return c

def add_micronutriente(nome,tipo,caloria,meq,meqsodio):
    c = Micronutriente.objects.get_or_create(nome=nome, tipo=tipo, caloria=caloria, meq=meq, meqsodio=meqsodio)[0]
    return c
    
def add_outronutriente(nome,tipo,caloria,porcentagemgrama):
    c = Outronutriente.objects.get_or_create(nome=nome, tipo=tipo, caloria=caloria, porcentagemgrama=porcentagemgrama)[0]
    return c 

# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')
    from tenp.models import Macronutriente, Micronutriente, OutroNutriente
    populate()
