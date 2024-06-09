"""""

Problema 3:
Del siguiente URL
https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format
&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D
%3D
Descargue la imagen que más le agrade, según lo revisado en la clase. Posteriormente crear un
programa que permita el almacenamiento de la imagen como un archivo zip. Finalmente cree
un código que permita hacer un unzip al archivo zipeado.

"""""


import requests
import zipfile

# Paso 1: Descargar la imagen
image_url = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
response = requests.get(image_url)
image_data = response.content

# Guardar la imagen en un archivo
image_filename = "imagen_descargada.jpg"
with open(image_filename, "wb") as image_file:
    image_file.write(image_data)

# Paso 2: Guardar la imagen en un archivo ZIP
zip_filename = "imagen.zip"
with zipfile.ZipFile(zip_filename, 'w') as zip_file:
    zip_file.write(image_filename)

# Paso 3: Crear un nuevo archivo ZIP que contenga el archivo ZIP previamente creado
final_zip_filename = "archivo_final.zip"
with zipfile.ZipFile(final_zip_filename, 'w') as final_zip_file:
    final_zip_file.write(zip_filename)
