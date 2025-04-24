# SismoStats-Programa
Trabajo Practico - Tabla de Terremotos

Este programa utiliza datos en tiempo real de la API del [USGS](https://earthquake.usgs.gov/) para mostrar información sobre los terremotos ocurridos en las últimas 24 horas. Los datos se visualizan en un mapa interactivo usando Plotly.

---

## ¿Qué hace este programa?

 Se conecta a la API del USGS  
 Extrae datos como lugar, magnitud, profundidad y coordenadas  
 Genera un archivo `.csv` con los datos  
 Muestra un mapa con los epicentros y la intensidad de cada sismo  

---

##  Tecnologías utilizadas

- Python
- `requests` para acceder a la API
- `pandas` para manejar datos
- `plotly.express` para la visualización
- `GeoJSON` (formato de la API de USGS)

---

##  Fuentes y recursos utilizados

- [Documentación oficial de la API del USGS](https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php)  
  Explica cómo acceder a los datos de terremotos en tiempo real en formato GeoJSON.

- [Documentación de Plotly Express](https://plotly.com/python/plotly-express/)  
  Para crear gráficos y mapas interactivos de forma sencilla en Python.

- [Documentación de la librería requests](https://docs.python-requests.org/en/latest/)  
  Utilizada para conectarse a la API del USGS.

- [Documentación de pandas](https://pandas.pydata.org/docs/)  
  Para manipular los da tos y convertirlos en un DataFrame.

## Autor

Hecho por **Leo Borgo**  
Abril 2025
