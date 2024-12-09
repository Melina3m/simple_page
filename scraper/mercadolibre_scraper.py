import requests
from bs4 import BeautifulSoup

def extraer_precio_mercadolibre(url):
    """Extrae el precio, título, descripción e imagen de un producto de Mercado Libre."""

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extraer el precio
    precio_elemento = soup.find('span', {'class': 'andes-money-amount__fraction'})
    if precio_elemento:
        precio = precio_elemento.text.strip()
    else:
        precio = "No se encontró el precio"

    # Extraer el título
    titulo_elemento = soup.find('meta', {'name': 'twitter:title'})
    if titulo_elemento:
        titulo = titulo_elemento['content'].strip()
    else:
        titulo = "No se encontró el título"

    # Extraer la descripción
    descripcion_elemento = soup.find('meta', {'property': 'og:description'})
    if descripcion_elemento:
        descripcion = descripcion_elemento['content'].strip()
    else:
        descripcion = "No se encontró la descripción"

    # Extraer la imagen
    imagen_elemento = soup.find('img', {'class': 'ui-pdp-image'})
    if imagen_elemento:
        imagen_url = imagen_elemento['src']
    else:
        imagen_url = "No se encontró la imagen"

    return precio, titulo, descripcion, imagen_url

# URL del producto en Mercado Libre
url_producto = "https://articulo.mercadolibre.com.co/MCO-1350238933-monitor-lg-24-lg-24gn65r-bawp-ultragear-ips-144hz-_JM"

precio, titulo, descripcion, imagen_url = extraer_precio_mercadolibre(url_producto)


