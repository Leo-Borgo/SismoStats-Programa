import requests
import pandas as pd
import plotly.express as px
import os
os.system("cls")

#URL de la API de USGS para terremotos en las últimas 24 horas
url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"

#obtener los datos
respuesta = requests.get(url)
datos = respuesta.json()

#extraer los datos relevantes
elementos = datos['features']
terremotos = []

for elemento in elementos:
    propiedades = elemento['properties']
    geometria = elemento['geometry']
    terremotos.append({
        'Lugar': propiedades['place'],
        'Magnitud': propiedades['mag'],
        'Tiempo': pd.to_datetime(propiedades['time'], unit='ms'),
        'Longitud': geometria['coordinates'][0],
        'Latitud': geometria['coordinates'][1],
        'Profundidad': geometria['coordinates'][2]
    })

#convertir a DataFrame
tabla_terremotos = pd.DataFrame(terremotos)
tabla_terremotos = tabla_terremotos[tabla_terremotos["Magnitud"] > 0]

#crear un archivo csv para ver los datos
tabla_terremotos.to_csv("terremotos_ultimas_24hs.csv", index=False)

#crear el mapa
figura = px.scatter_geo(tabla_terremotos,
    lat='Latitud',
    lon='Longitud',
    hover_name='Lugar',
    size='Magnitud',
    color='Magnitud',
    projection="natural earth",
    title="Terremotos en las últimas 24 horas",
    color_continuous_scale="Inferno"
)

print(tabla_terremotos.head(10))
figura.show()

input("\npresione ENTER para salir")
