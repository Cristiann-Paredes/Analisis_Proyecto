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


# CÓDIGO PARA LA LIMPIEZA/FILTRACIÓN DE DATOS

Función para limpiar los caracteres no deseados de una cadena y convertirlo de csv a json def limpiar_cadena(cadena):

Eliminamos las comas, puntos y comas, y espacios vacíos

cadena_limpia = ''.join(caracter for caracter in cadena if caracter not in [',', ';', ' '])

return cadena_limpia

Función para convertir un archivo CSV a JSON con la limpieza realizada previamente def csv_to_json(csvFilePath, jsonFilePath):

jsonArray = []

csvFilePath = r'accidentes.csv'

jsonFilePath = r'accidentes.json'

csv_to_json(csvFilePath, jsonFilePath)

with open(csvFilePath, encoding='utf-8') as csvf:

![image](https://github.com/Cristiann-Paredes/Analisis_Proyecto/assets/117744113/85035ce2-f978-4ab8-85c3-fd8530f15174)
![image](https://github.com/Cristiann-Paredes/Analisis_Proyecto/assets/117744113/4c2dab92-f265-420a-847e-b4fd0e6457b7)

# Función para convertir un archivo JSON a CSV con limpieza de cadenas

def json_to_csv(jsonFilePath, csvFilePath):

jsonFilePath = 'eventslimpio.json'

csvFilePath = 'events3.csv'

json_to_csv(jsonFilePath, csvFilePath)

![image](https://github.com/Cristiann-Paredes/Analisis_Proyecto/assets/117744113/c108a316-4c26-469d-8a66-3e908b4681cc)

Este código carga datos desde un archivo JSON llamado eventslimpio, limpia las cadenas de caracteres de caracteres

no deseados y los convierte en un archivo CSV con encabezados. La función limpiar_cadena es utilizada para eliminar

comas, puntos y espacios en blanco de las cadenas de caracteres antes de escribir los datos en el archivo CSV.

eventos
import pandas as pd

from pymongo import MongoClient

def load_csv_to_mongodb(database_name, collection_name, csv_file):

![image](https://github.com/Cristiann-Paredes/Analisis_Proyecto/assets/117744113/b30226c1-1794-4368-98b3-ae287aa72758)

# Paso de datos Json a Couchdb y de Couchdb a SQL Managment Studio

Temática: Eventos y noticias mundiales


import pandas as pd

Especificamos la ruta del archivo CSV que deseamos leer

archivo_csv = 'abcnews-date-text.csv'

Leemos el archivo CSV en un DataFrame de pandas

data = pd.read_csv(archivo_csv)



Mostramos las primeras filas del DataFrame para verificar la lectura

data.head()


Leemos el archivo CSV

archivo_csv = 'abcnews-date-text.csv'

data = pd.read_csv(archivo_csv)



Transformamos el DataFrame a JSON y guardamos

archivo_json = 'abc-news.json'

data.to_json(archivo_json, orient='records', lines=True)

print(f'Archivo JSON guardado en {archivo_json}')


Conexión a la base de datos CouchDB

server = couchdb.Server('http://admin:Cristian@123####:5984/')

db_name = 'politica'


Cargamos y procesamos el archivo JSON línea por línea

ruta_json = 'abc-news.json'

with open(ruta_json, 'r', encoding='utf-8') as file:

![image](https://github.com/Cristiann-Paredes/Analisis_Proyecto/assets/117744113/86c77755-29da-4d86-9fd2-1803f77557b5)


Conexión a SQL Server

server = 'DESKTOP-A3ENU4G'

database = 'Politico'

conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes'

connection = pyodbc.connect(conn_str)


Inserción de los datos de couchdb en SQL Server

cursor = connection.cursor()

for doc in db.view('_all_docs', include_docs=True):

![image](https://github.com/Cristiann-Paredes/Analisis_Proyecto/assets/117744113/2e44b3ce-30ae-47a6-bc07-9bf503e865f4)


Confirmamos la transacción y cerramos la conexión

connection.commit()

connection.close()














