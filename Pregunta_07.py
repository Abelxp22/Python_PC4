"""""

Problema 7:
Del ejercicio de Clase. Emplee el API de SUNAT que corresponda para obtener el precio de compra y
venta del dólar durante todo el 2023. Almacene dicha información en base de datos ‘base.db’ con
nombre de tabla sunat_info.
Finalmente deberá mostrar el contenido de dicha tabla.
Lee la documentación del API: https://apis.net.pe/api-tipo-cambio.html


"""""

import requests
import sqlite3

def obtener_precios_dolar():

    url = "https://apis.net.pe/api-tipo-cambio/v1/tipo-cambio"
    parametros = {"token": "tu_token", "fechaInicio": "2023-01-01", "fechaFin": "2023-12-31"}
    respuesta = requests.get(url, params=parametros)

    if respuesta.status_code == 200:
        datos = respuesta.json()
        return [(registro['fecha'], registro['compra'], registro['venta']) for registro in datos['result']]
    else:
        print("Error al obtener los precios del dólar:", respuesta.status_code)
        return None

def crear_tabla_sunat_info(conexion):
    cursor = conexion.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS sunat_info (
                      fecha TEXT PRIMARY KEY,
                      precio_compra REAL,
                      precio_venta REAL)''')
    conexion.commit()

def insertar_datos_sunat_info(conexion, datos):
    cursor = conexion.cursor()
    cursor.executemany('INSERT OR IGNORE INTO sunat_info (fecha, precio_compra, precio_venta) VALUES (?, ?, ?)', datos)
    conexion.commit()

def mostrar_contenido_tabla(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM sunat_info")
    filas = cursor.fetchall()
    for fila in filas:
        print(fila)

def main():
    precios_dolar = obtener_precios_dolar()
    if precios_dolar:
        conexion = sqlite3.connect('base.db')

        crear_tabla_sunat_info(conexion)

        insertar_datos_sunat_info(conexion, precios_dolar)

        print("Contenido de la tabla sunat_info:")
        mostrar_contenido_tabla(conexion)

        conexion.close()
    else:
        print("No se pudieron obtener los datos del dólar de la API.")

if __name__ == "__main__":
    main()






