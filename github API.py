import requests
import plotly.graph_objects as go

#obtener los 3 repositorios con más estrellas en GitHub
url = "https://api.github.com/search/repositories?q=stars:>1&sort=stars&order=desc&per_page=3"
respuesta = requests.get(url)
repositorios = respuesta.json()["items"]

#extraer datos para el gráfico
nombres = [repo["full_name"] for repo in repositorios]
estrellas = [repo["stargazers_count"] for repo in repositorios]
descripciones = [repo["description"] or "Sin descripción" for repo in repositorios]

#crear gráfico de barras
figura = go.Figure(data=[go.Bar(
    x=nombres,
    y=estrellas,
    text=descripciones,
    textposition='auto',
    marker_color=["#1f77b4", "#ff7f0e", "#2ca02c"]
)])

figura.update_layout(
    title="Top 3 Repositorios con Más Estrellas en GitHub",
    xaxis_title="Repositorio",
    yaxis_title="Estrellas",
    template="plotly_dark"
)

#mostrar el gráfico
figura.show()
