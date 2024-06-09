"""""

Problema 1:
En este problema debe generar un programa que realice:
- Solicite al usuario por línea de comando un valor de “n” el cual representa la cantidad
de bitcoins que posee el usuario.
- Consulte la API del índice de precios de Bitcoin de CoinDesk en el siguiente link
(https://api.coindesk.com/v1/bpi/currentprice.json), la cual retornará un objeto JSON,
entre cuyas claves anidadas encontrará el precio actual de Bitcoin como un número
decimal. Asegúrese de detectar cualquier excepción, como el siguiente código:
import requests
- Muestra el costo actual de “n” Bitcoins en USD con cuatro decimales, usando , como
separador de miles.

"""""


import requests

def obtener_precio_bitcoin():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        return float(data["bpi"]["USD"]["rate"])  # Precio actual de Bitcoin en USD
    except requests.RequestException as e:
        print("Error al obtener el precio de Bitcoin:", e)
        return None

def main():
    while True:
        try:
            bitcoins = float(input("Ingrese la cantidad de bitcoins que posee: "))
            break
        except ValueError:
            print("Ingrese un valor numérico válido.")


    precio_bitcoin = obtener_precio_bitcoin()
    if precio_bitcoin is not None:
        costo_usd = bitcoins * precio_bitcoin

        print(f"Costo actual de {bitcoins} bitcoins en USD: ${costo_usd:,.4f}")
    else:
        print("No se pudo obtener el precio de Bitcoin. Intente nuevamente más tarde.")

if __name__ == "__main__":
    main()
