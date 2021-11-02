import pandas as pd
import re



def new_activity(x):
    dic_activities = { 
        'Swimming': '.*wi.*|.*mmi.*|.*bath.*|.*ading.*|.*swim.*',
        'Surfing': '.*urf.*|.*addl.*|.*oard.*|.*Board.*|.*surf.*|.+Surf.*',
        'Diving': '.*spear.*|.*div.*|.*photo.*|.*subm.*|.*merged.*|.*norkel.*|.*scuba.*',
        'Fishing': '.*shin.*|.*fish.*|.*Fish.*',
        'Boating': '.*kay.*|.*yak.*|.*banana.*|.*sail.*|.*atch.*|.*anoing.*',
        'Feeding': '.*feed.*|.*food.*'
        }
    for key, values in dic_activities.items():
        if re.match(values, x):
            return key
    return 'Otra'



def clean_fatal (x):

    """
    Esta función sirve para transformar los valores de la columna fatal_(y/n) en 'Y' o 'N'
    """
    if x['fatal_(y/n)'] == "N":
        i = "N"
    elif x['fatal_(y/n)'] == " N":
        i = "N"
    elif x['fatal_(y/n)'] == "N ":
        i = "N"   
    elif x['fatal_(y/n)'] == "Y":
        i = "Y"
    elif x['fatal_(y/n)'] == "nan":
        i = "Desconocido"
    elif x['fatal_(y/n)'] == "M":
        i = "Desconocido"
    elif x['fatal_(y/n)'] == "Unknown":
        i = "Desconocido"
    elif x['fatal_(y/n)'] == "2017":
        i = "Desconocido"
    elif x['fatal_(y/n)'] == ", ":
        i = "Desconocido"
    else:
        i = "Y"
    return i


def clean_species (y):

    """
    Esta funcion sirve para limpiar la columna de 'species'. 
    Reduce las categorias a las reales.
    """
    dic_species = {  
        'White shark': '.*white.*|.*great.*|.*hite.*|.*grea.*',
        'Bull shark' : '.*bull.*|.*ull.*',
        'Hammerhead Shark' : '.*ham.*|.*mmer.*|.*head.*',
        'Tiger shark' : '.*tig.*|.*ger.*',
        'Whitetip shark' : '.*tip.*',
        'Blacktip Shark' : '.*bla.*|.*ack.*',
        'Shortfin Mako Shark' : '.*fin.*|.*shor.*|.*mak.*|.*ko.*',
        'Sand Tiger Shark' : '.*san.*'}

    for key,values in dic_species.items():

        if re.match(values, y):
            return key 
        
    return "Desconocido"


def new_country (x): 
    if x == 'USA':
        return 'USA'
    elif x == 'AUSTRALIA':
        return 'AUSTRALIA'
    elif x == 'SOUTH AFRICA':
        return 'SOUTH AFRICA'
    else:
        'OTHER'

