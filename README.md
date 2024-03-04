# Analisis_Proyecto


# INTEGRANTES:

Cristian Paredes

Melani Barrera

jhordy Aguas


## ARQUITECTURA 

![image](https://github.com/Cristiann-Paredes/Analisis_Proyecto/assets/117744113/7e7bb816-1d8f-4703-abea-9be3e5540735)

# CODIGO PARA EL PASO DE DATOS CSV A JSON O VICEVERSA

import pandas as pd

df = pd.read_csv('tematica.csv')

def csv_to_json(csv_file, json_file):

df = pd.read_csv(csv_file)

# Conversion
df.to_json(json_file, orient='records', lines=True)

csv_filename = 'aquí irá el nombre del archivo dependiendo la temática'

json_filename = 'el nombre que le queramos poner a nuestro json'

csv_to_json(csv_filename, json_filename)














