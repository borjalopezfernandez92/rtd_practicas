import requests
from . import dataFrame

def get_currency(dataFrame):

    print(dataFrame['cantidad_total'])

    url = f"https://api.coingecko.com/api/v3/coins/list"
    response = requests.get(url).json()
    # print(response)
    name = response[0]['name'] # variable con nombre
    res_tuplas = res_tuplas + tuple(name.split()) # agrego tupla con split para coger palabra completa

    price = response[0]['current_price'] # variable con precio actual
    dataFrame = dataFrame * price
    res_tuplas = res_tuplas + (dataFrame,) # agrego tupla con split para coger valor completo
    print(res_tuplas)


__all__ = [
    'get_currency'
]