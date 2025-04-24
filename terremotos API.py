# importar librerias
import requests
import pandas as pd
import plotly.express as px
import os
# limpiar la pantalla
os.system("cls")

#URL de la API de USGS para terremotos en las últimas 24 horas
url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"

#obtener los datos
respuesta = requests.get(url)
datos = respuesta.json()

# extraer la lista de terremotos
# la respuesta de la API es un diccionario con una clave "features" que contiene una lista de terremotos
# cada terremoto es un diccionario con claves "properties", informacion del terremoto y "geometry", su ubicacion
elementos = datos['features']
terremotos = []

# extraer la informacion de cada terremoto
for elemento in elementos: # por cada elemento en la lista de terremotos
    # extraer propiedades y geometria
    propiedades = elemento['properties']
    geometria = elemento['geometry']
    # crear un diccionario con la informacion relevante
    terremotos.append({
        'Lugar': propiedades['place'],
        'Magnitud': propiedades['mag'],
        'Tiempo': pd.to_datetime(propiedades['time'], unit='ms'), # convertir el tiempo de milisegundos a un objeto datetime
        'Longitud': geometria['coordinates'][0],
        'Latitud': geometria['coordinates'][1],
        'Profundidad': geometria['coordinates'][2]
    })

# crear un DataFrame de pandas con la lista de terremotos
# el DataFrame es una tabla de datos, similar a una hoja de calculo
# cada fila es un terremoto y cada columna es una propiedad del terremoto
tabla_terremotos = pd.DataFrame(terremotos)
tabla_terremotos = tabla_terremotos[tabla_terremotos["Magnitud"] > 0] # filtrar terremotos con magnitud mayor a 0

# guardar la tabla en un archivo CSV
# este archivo se puede abrir con Excel o cualquier otro programa que soporte CSV
# el archivo se guarda en la misma carpeta que el script
tabla_terremotos.to_csv("terremotos_ultimas_24hs.csv", index=False)

# crear un grafico con
figura = px.scatter_geo(tabla_terremotos, 
    lat='Latitud',
    lon='Longitud',
    hover_name='Lugar',
    size='Magnitud',
    color='Magnitud',
    projection="natural earth", #natural earth, equirectangular, orthographic, mercator, kavrayskiy7, miller, robinson
    title="Terremotos en las últimas 24 horas",
    color_continuous_scale="Inferno"
)

#imprime los 10 terremotos mas recientes y muestra el mapa
print(tabla_terremotos.head(10))
figura.show()

input("\nPresiona ENTER para salir: ")
