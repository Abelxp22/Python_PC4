"""""

Problema 4:
Almacene los datos de precio de Bitcoin en un archivo txt con un formato que consideré
apropiado

"""""

import requests
import json
from datetime import datetime

def get_bitcoin_price():
    # URL para obtener el precio de Bitcoin
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

    # Hacer la solicitud GET a la API
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

def save_to_txt(data, filename):
    with open(filename, 'w') as file:
        file.write(data)

def format_data(data):
    now = datetime.now()
    formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
    
    bitcoin_price = data["bitcoin"]["usd"]
    
    formatted_data = f"Fecha y Hora: {formatted_date}\nPrecio de Bitcoin (USD): ${bitcoin_price}"
    
    return formatted_data

def main():
    bitcoin_data = get_bitcoin_price()
    
    if bitcoin_data:
        formatted_data = format_data(bitcoin_data)
        
        save_to_txt(formatted_data, "bitcoin_price.txt")
        print("Datos de precio de Bitcoin guardados en 'bitcoin_price.txt'")
    else:
        print("Error al obtener los datos de precio de Bitcoin")

if __name__ == "__main__":
    main()
