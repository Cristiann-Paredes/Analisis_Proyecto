# Analisis_Proyecto


# INTEGRANTES:

Cristian Paredes

Melani Barrera

Jhordy Aguas


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

## visualizacion de los diferentes casos de studio 

# Pulso político en 20 ciudades principales de Ecuador

Visualizacion de los gastos economicos durante el periodo politico de las ciudades del ecuador 
![image](https://github.com/Cristiann-Paredes/Analisis_Proyecto/assets/117744113/0eb3c672-9982-4f5a-a824-58ae90d85fdd)

Datos recopiladdos de twitter que se filtraron que son escritos dentro de ecuador y datos que no se escribieron dentro de estas cuidades 

![image](https://github.com/Cristiann-Paredes/Analisis_Proyecto/assets/117744113/04436345-c1cd-4454-a7a4-ee920ca33b52)
![image](https://github.com/Cristiann-Paredes/Analisis_Proyecto/assets/117744113/707cb98e-454d-4b98-ae09-d8b2fde3bc76)

# Pulso político en provincias de Ecuador

Visualización de las provincias  del Ecuador donde se realiza twists relacionaos con partidos Politicos
![image](https://github.com/Cristiann-Paredes/Analisis_Proyecto/assets/117744113/73ecc318-45a6-4872-8bdb-ccb45da24b0f)

La población de estudio correspondiente a la: “Formacion Institucional” del numero de personas que participan en eventos politicos 
![image (1)](https://github.com/Cristiann-Paredes/Analisis_Proyecto/assets/117744113/b748f9ee-2eec-4774-8bb7-8ab429a737ca)

Los hastag Usados en twitter que los usuarios postearon dentro del ambito politico  
![image](https://github.com/Cristiann-Paredes/Analisis_Proyecto/assets/117744113/9942282b-2ff0-4a4f-a109-67ba5a5d51e6)

Candidatos con mas respuesta del publico

![image](https://github.com/Cristiann-Paredes/Analisis_Proyecto/assets/117744113/24277b2a-85c7-4c61-839c-22d9371fd92c)

# Eventos o noticias mundiales

Contaminacion de la poblacion en ecuador durante el periodo de covid 19

![image (3)](https://github.com/Cristiann-Paredes/Analisis_Proyecto/assets/117744113/c0fa770f-2b43-4f5f-beca-5f3ae635cac7)
![image (2)](https://github.com/Cristiann-Paredes/Analisis_Proyecto/assets/117744113/7148b24a-1236-4bf3-b9bc-853d84a5d2cd)

Datos de lo nuevos casos registrados de infección de la población mundial
![image (5)](https://github.com/Cristiann-Paredes/Analisis_Proyecto/assets/117744113/dd1d1ab5-368b-4a74-813a-244fa5811c7a)

Suma de contaminación por semana de los continentes en periodo de COVID
![image (4)](https://github.com/Cristiann-Paredes/Analisis_Proyecto/assets/117744113/80aa4e15-8edb-47ee-914b-af7b936e6759)

# Juegos en línea por países

Suma de numero de unidades de videojuegos a nivel mundial 
![image (6)](https://github.com/Cristiann-Paredes/Analisis_Proyecto/assets/117744113/a88718dc-710b-4f14-aa0b-e0f96c188b12)

Empresas con mayor numero de ventas a nivel mundial 
![image (7)](https://github.com/Cristiann-Paredes/Analisis_Proyecto/assets/117744113/8e94d07c-a803-4395-94cc-c10478dd003b)

Mayor numero de ventas a nivel mundial en las diferentes consolas
![image (8)](https://github.com/Cristiann-Paredes/Analisis_Proyecto/assets/117744113/22eb9b9c-b8fb-48fe-ba33-5b3c41f04f2f)

Categoria de los videojuegos con mayor numero de ventas
![image (9)](https://github.com/Cristiann-Paredes/Analisis_Proyecto/assets/117744113/06d1e4dd-37a7-4b81-bde3-4c852beb4e19)
















