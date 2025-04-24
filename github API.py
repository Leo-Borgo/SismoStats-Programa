# importar librerias
import requests
import plotly.graph_objects as go
import os
# limpiar la pantalla
os.system("cls")

# URL de la API de GitHub para obtener los repositorios mas populares
# la API de GitHub permite acceder a la informacion de los repositorios publicos
url = "https://api.github.com/search/repositories?q=stars:>1&sort=stars&order=desc&per_page=3" #a partir de esta URL, se obtienen los repositorios con mas de una estrella, en orden descendente y se limita a 3 resultados
respuesta = requests.get(url)
repositorios = respuesta.json()["items"]

# extraer la informaciond de los repositorios
# la respuesta de la API es un diccionario con una clave "items" que contiene una lista de repositorios
nombres = [repo["full_name"] for repo in repositorios] # nombre completo del repositorio
estrellas = [repo["stargazers_count"] for repo in repositorios] # cantidad de estrellas
descripciones = [repo["description"] or "Sin descripción" for repo in repositorios] # descripcion del repositorio

# crear un DataFrame de pandas con la lista de repositorios
# el DataFrame es una tabla de datos, similar a una hoja de calculo
figura = go.Figure(data=[go.Bar( # crear un grafico de barras
    x=nombres, # eje x con los nombres de los repositorios
    y=estrellas, # eje y con la cantidad de estrellas
    text=descripciones, # texto con la descripcion de los repositorios
    textposition='auto', # posicion del texto
    marker_color=["#1f77b4", "#ff7f0e", "#2ca02c"] # colores de las barras
)])
# agregar etiquetas a los ejes y un titulo al grafico
figura.update_layout( # actualizar el layout del grafico
    title="Top 3 Repositorios con Más Estrellas en GitHub",
    xaxis_title="Repositorio",
    yaxis_title="Estrellas",
    template="plotly_dark"
)

#mostrar el gráfico
figura.show()

input("\nPresiona ENTER para salir: ")
