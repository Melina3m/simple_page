from flask import Flask, render_template  # Flask para crear la aplicación web y renderizar plantillas HTML
import requests  # Para hacer solicitudes HTTP
from bs4 import BeautifulSoup 

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

def extraer_precio_mercadolibre(url):
    """
    Función que extrae información de un producto de Mercado Libre.

    Parámetros:
    - url (str): La URL del producto en Mercado Libre desde el cual se extraerá la información.

    Retorna:
    - precio (str): El precio del producto.
    - titulo (str): El título del producto.
    - descripcion (str): La descripción del producto.
    - imagen_url (str): La URL de la imagen del producto.
    """

    # Hacer una solicitud GET para obtener el contenido de la página del producto
    response = requests.get(url)


    soup = BeautifulSoup(response.content, 'html.parser')

    # Extraer el precio del producto
    precio_elemento = soup.find('span', {'class': 'andes-money-amount__fraction'})
    if precio_elemento:
        precio = precio_elemento.text.strip()
    else:
        precio = "No se encontró el precio"

    # Extraer el título del producto
    titulo_elemento = soup.find('meta', {'name': 'twitter:title'})
    if titulo_elemento:
        titulo = titulo_elemento['content'].strip()
    else:
        titulo = "No se encontró el título"  # Si no se encuentra el título, se indica

    # Extraer la descripción del producto
    descripcion_elemento = soup.find('meta', {'property': 'og:description'})
    if descripcion_elemento:
        descripcion = descripcion_elemento['content'].strip()
    else:
        descripcion = "No se encontró la descripción"  # Si no se encuentra la descripción, se indica

    # Extraer la URL de la imagen del producto
    imagen_elemento = soup.find('img', {'class': 'ui-pdp-image'})
    if imagen_elemento:
        imagen_url = imagen_elemento['src']  # Extraemos la URL de la imagen
    else:
        imagen_url = "No se encontró la imagen"  # Si no se encuentra la imagen, se indica

    # Retorna la información extraída
    return precio, titulo, descripcion, imagen_url

@app.route('/')
def index():
    """
    Ruta principal que renderiza la información del producto en una página web.

    Hace una solicitud a la función extraer_precio_mercadolibre para obtener los detalles del producto
    y luego pasa esos datos a la plantilla HTML para ser mostrados en el navegador.
    """

    # URL del producto en Mercado Libre
    url_producto = "https://articulo.mercadolibre.com.co/MCO-1350238933-monitor-lg-24-lg-24gn65r-bawp-ultragear-ips-144hz-_JM"

    # Llamar a la función para obtener la información del producto
    precio, titulo, descripcion, imagen_url = extraer_precio_mercadolibre(url_producto)

    # Renderizar la plantilla 'index.html' pasando los datos del producto a la plantilla
    return render_template('index.html', precio=precio, titulo=titulo, descripcion=descripcion, imagen_url=imagen_url, url_producto=url_producto)

if __name__ == '__main__':
    """
    Configurar y ejecutar la aplicación Flask en modo de desarrollo.

    El servidor Flask se ejecutará en el puerto 8080 y estará disponible en todas las interfaces de red de la máquina.
    """
    app.run(debug=True, host='0.0.0.0', port=8080)
