#https://parzibyte.me/blog/2021/02/11/python-peticion-http-post-json/

"""
# https://parzibyte.me/blog
import requests

url = "https://https://www.google.com/posts"
usuario = {
    "title": "Título",
    "body": "El cuerpo",
}
respuesta = requests.post(url, json=usuario)
# Ahora decodificamos la respuesta como json
como_json = respuesta.json()
print("La respuesta del servidor es:")
print(como_json)
# Podemos acceder al id por ejemplo
print(f"El id es: {id}")
"""

# https://parzibyte.me/blog
import requests

url = "127.0.0.1/"
datos = "Hola mundo"  # <- El json que enviamos
respuesta = requests.post(url, json=datos)
# Ahora decodificamos la respuesta como json
#como_json = respuesta.json()
print("La respuesta del servidor es:")
#print(como_json)