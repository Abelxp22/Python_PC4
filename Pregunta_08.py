import requests
import sqlite3
from datetime import date

def obtener_precio_bitcoin():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status() 
        data = response.json()
        return {
            "USD": float(data["bpi"]["USD"]["rate"]),
            "GBP": float(data["bpi"]["GBP"]["rate"]),
            "EUR": float(data["bpi"]["EUR"]["rate"])
        }
    except requests.RequestException as e:
        print("Error al obtener el precio de Bitcoin:", e)
        return None

def obtener_tipo_cambio_pen_usd():
    try:
        response = requests.get("https://api.sunat.cloud/tipo-cambio-real")
        response.raise_for_status()
        data = response.json()
        return float(data["venta"])
    except requests.RequestException as e:
        print("Error al obtener el tipo de cambio de PEN a USD:", e)
        return None

def crear_tabla_bitcoin(conexion):
    cursor = conexion.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS bitcoin (
                      fecha DATE PRIMARY KEY,
                      precio_usd REAL,
                      precio_gbp REAL,
                      precio_eur REAL,
                      precio_pen REAL)''')
    conexion.commit()

def insertar_datos_bitcoin(conexion, precios):
    cursor = conexion.cursor()
    fecha_actual = date.today()
    cursor.execute('''INSERT INTO bitcoin (fecha, precio_usd, precio_gbp, precio_eur, precio_pen)
                      VALUES (?, ?, ?, ?, ?)''', (fecha_actual, precios["USD"], precios["GBP"], precios["EUR"], precios["PEN"]))
    conexion.commit()

def obtener_precio_bitcoin_pen(precio_usd, tipo_cambio_pen_usd):
    return precio_usd * tipo_cambio_pen_usd

def obtener_precio_compra_10_bitcoins(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT precio_pen, precio_eur FROM bitcoin ORDER BY fecha DESC LIMIT 1")
    fila = cursor.fetchone()
    if fila:
        precio_pen = fila[0]
        precio_eur = fila[1]
        precio_compra_10_bitcoins_pen = 10 * precio_pen
        precio_compra_10_bitcoins_eur = 10 * precio_eur
        return precio_compra_10_bitcoins_pen, precio_compra_10_bitcoins_eur
    else:
        return None, None

def main():
    precios_bitcoin = obtener_precio_bitcoin()
    if precios_bitcoin:
        tipo_cambio_pen_usd = obtener_tipo_cambio_pen_usd()
        if tipo_cambio_pen_usd:
            precios_bitcoin["PEN"] = obtener_precio_bitcoin_pen(precios_bitcoin["USD"], tipo_cambio_pen_usd)

            conexion = sqlite3.connect('base.db')

            crear_tabla_bitcoin(conexion)

            insertar_datos_bitcoin(conexion, precios_bitcoin)

            precio_compra_10_bitcoins_pen, precio_compra_10_bitcoins_eur = obtener_precio_compra_10_bitcoins(conexion)
            if precio_compra_10_bitcoins_pen is not None and precio_compra_10_bitcoins_eur is not None:
                print(f"Precio de compra de 10 bitcoins en PEN: {precio_compra_10_bitcoins_pen:,.4f}")
                print(f"Precio de compra de 10 bitcoins en EUR: {precio_compra_10_bitcoins_eur:,.4f}")
            else:
                print("No se pudo obtener el precio de compra de 10 bitcoins en la base de datos.")

            conexion.close()
        else:
            print("No se pudo obtener el tipo de cambio de PEN a USD.")
    else:
        print("No se pudo obtener el precio de Bitcoin en USD, GBP y EUR.")

if __name__ == "__main__":
    main()
