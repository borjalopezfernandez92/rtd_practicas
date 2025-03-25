import freecurrencyapi
import requests
import os, requests
from dotenv import load_dotenv
from datetime import datetime,timedelta

load_dotenv()

key = os.getenv("CURRENCY_KEY")
client = freecurrencyapi.Client(key)

def fcaMenu():
    
    requestType = input("Escoge el tipo de request a realizar: \n(1)Comprobar Status\n(2)Obtener currency\n(3)Obtener tasas de cambio\n(4)Obtener historial de tasas de cambio\n(5)Conversor de divisas\n(6)Ejercicio Rupias\n(7)Ejercicio multiAPIS")
    requestInt = int(requestType)
    if requestInt == 1:
        print(checkStatus())
    elif requestInt == 2:
        currency = input("Ingresa el codigo de la divisa que quieres comprobar (EJ: USD): ").upper()
        print(checkSingleCurrency(currency))
    
    elif requestInt == 3:
        result = client.latest()
        print(result)
    
    elif requestInt == 4:
        date = input("Escoge la fecha desde la que obtener el historial (formato: 2022-12-31): ")
        currency = [input("Escoge la divisa que deseas (EJ USD): ").upper()]
        print(currencyHistorical(date,currency))

    elif requestInt == 5:
        print(convertCurrency())

    elif requestInt == 6:
        rupees()

    elif requestInt == 7:
        multiApi()

def checkStatus():
    url = f"https://api.freecurrencyapi.com/v1/status?apikey={key}"
    fetch = requests.get(url).json()

    return fetch

def checkSingleCurrency(currency):
    url = f"https://api.freecurrencyapi.com/v1/currencies?apikey={key}&currency={currency}"
    fetch = requests.get(url).json()

    return fetch

def checkLatest():
    url = f"https://api.freecurrencyapi.com/v1/latest?apikey={key}"
    fetch = requests.get(url).json()

    return fetch


class CurrencyConverter:
    def __init__(self, key):
        self.key = key
        self.base_url = f"https://api.freecurrencyapi.com/v1/latest?apikey={key}"

    def convert(self, amount, from_currency, to_currency):
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Utiliza una cantidad positiva")
            
            params ={
                "currencies": to_currency,
                "base_currency": from_currency
            }
            
            response = requests.get(self.base_url, params=params)

            if response.status_code != 200:
                raise Exception(f"Error al conseguir data: {response.text}")
            
            data= response.json()
            if "data" not in data:
                raise Exception("Formato de respuesta invalido")
            
            rate = data["data"][to_currency]

            result = amount * rate
            return round(result,2)
    
        except ValueError as e:
            print(f"Error: Cantidad invalida - {str(e)}")
            return None
        except KeyError:
            print(f"Error: Codigo de divisa invalido: '{to_currency}'")
            return None
        except Exception as e:
            print(f"Error: {str(e)}")
            return None
        

def currencyHistorical(date, currency,base_curr):
        
        print(f"date en historical ->", date)
        print(f"currency en histoical ->", currency)
        print(f"base_curr en histoical ->", base_curr)


        if date is None:
            date = input("Escoge la fecha desde la que obtener el historial (formato: 2022-12-31): ")
        if currency is None:
            currency = input("Escoge la divisa que deseas (EJ USD): ").upper()
        
        if type(currency) is not list:
            raise Exception("Currencies needs to be a list")

        fetchUrl = f"https://api.freecurrencyapi.com/v1/historical?apikey={key}&date={date}&currencies={currency[0].upper()}&base_currency={base_curr.upper()}"
        fetch = requests.get(fetchUrl).json()

        print(f"-->",fetch)
        result = fetch['data'][date][currency[0].upper()]
        # print("precio de la divisa ["+ currency +"] en la fecha ["+date+"]: ",result)
        return round(result, 2)


def convertCurrency(from_date=None,from_curr=None, to_date=None,to_curr=None, amount=None):
    # converter = CurrencyConverter("fca_live_IfvOgd1jKgQuynk8SvKcqG3rxwa464IxrAC86vto")
    while True:
        try:
            if from_curr is None:
                from_curr = input("Ingresa el codigo de la divisa a convertir (EJ: USD): ".upper())
            if from_date is None:
                from_date = input("Introduce la fecha de la divisa a convertir (EJ: 2020-12-31)")
            if to_curr is None:
                to_curr = input("Ingresa el codigo de la divisa que quieres conseguir (EJ: EUR): ".upper())
            if to_date is None:
                to_date = input("Introduce la fecha de la divisa a convertir (EJ: 2020-12-31)")
            if amount is None:
                amount = input("Ingresa la cantidad a convertir: ")

            to_curr_converted = currencyHistorical(to_date, [to_curr], from_curr)
            result = float(amount) * to_curr_converted

            if result is not None:
                return [amount, from_curr, round(result), to_curr]

        except KeyboardInterrupt:
            print("\nExisting...")
            break

def multiApi():

#### 1. ¿Cuántos rublos (RUB) pagaste por el abrigo el 26 de enero de 2020?

    rubPrice = currencyHistorical("2020-01-26", ["USD"], "RUB")  # Llamo a la función que me traerá el valor del rublo en la fecha especificada
    coatUrl = f"https://fakestoreapi.com/products/17"            # Recojo los datos del producto 17, el abrigo en cuestión
    coatPrice = requests.get(coatUrl).json()
    coatPrice = coatPrice['price']                               # y me quedo con el precio
    
    result1 = coatPrice / rubPrice                               # multiplico el valor del rublo en la fecha en cuestión por el valor del abrigo

    print("Ejercicio 1: ")
    print("El abrigo me costó [",coatPrice,"] dolares, y en en Rublos costó: [",result1,"]")
    print("-"*20)
    # return result1

##### 2. ¿Por cuántos rublos (RUB) vendiste el abrigo el 3 de marzo de 2022, considerando la inflación del rublo?

    rubPrice = currencyHistorical("2022-03-03", ["RUB"], "USD")  # Obtengo el valor del rublo en la fecha [2022-03-03]
    result2 = round(rubPrice * coatPrice)                        # multiplico el valor del rublo en la fecha en cuestión por el valor del abrigo
    
    print("Ejercicio 2: ")
    print("El abrigo se vendió por [",result2,"] rublos")
    print("-"*20)

    # return result2
    
##### 3. ¿Cuántos florines húngaros (HUF) obtuviste el 1 de septiembre de 2024 al convertir los rublos de la venta?
        
    hufConverted = convertCurrency("2024-09-01","RUB", "2024-09-01","HUF", result2) # Convierto la cantidad de rublos de los que dispongo
    
    print("Ejercicio 3: ")
    print("Tenía [",hufConverted[0], "] rublos.\nLo cual corresponde a [",hufConverted[2],"] florines húngaros en la fecha especificada.")
    print("-"*20)

    result3 = hufConverted[2]                                                       # Y almaceno el resultado
    # return result3
##### 4. ¿Qué cantidad de Ethereum (ETH) obtuviste ayer al convertir los florines húngaros?

    yesterday = datetime.now() - timedelta(days=1)
    format_date = yesterday.strftime('%d-%m-%Y')
    ethUrl = f"https://api.coingecko.com/api/v3/coins/ethereum/history?date={format_date}"     # Recojo los datos del ethereum
    response = requests.get(ethUrl).json()
    ethPrice =response['market_data']['current_price']['huf']                                  # Y me quedo con el valor actual (2088.78)
    result4 = round(ethPrice / result3)                                                        # Y divido la cantidad de florines que tengo entre el precio del Ethereum
    
    print("Ejercicio 4: ")
    print("Puedo obtener [",result4,"] Ethereum.")
    print("-"*20)

    #return result4

def rupees():
    inrPrice = currencyHistorical("2023-01-01", ["INR"], "TRY")            # Obtengo el precio de la rupia en la fecha correspondiente
    tryPrice = currencyHistorical("2023-01-01", ["TRY"], "INR")            # Y el de las liras turcas

    inrAmount = tryPrice * 200                                             # Calculo cuánto cuestan valen 200 liras turcas
# round(inrAmount, 2) = inrAmount / inrPrice                               # Y lo divido entre el valor de las rupias para saber cuántas compré

    sellInr = currencyHistorical("2024-03-04", ["INR"],"TRY")              # obtengo el precio de las rupias en la fecha de venta
    print(f"sellInr ->", sellInr)
    print(f"inramount ->", inrAmount)

    inrAmount = inrAmount * sellInr                                        # y lo multiplico por la cantidad de rupias que tengo
    inrPrice = currencyHistorical("2024-03-04", ["TRY"], "INR")            # por último obtengo el precio de las liras en la fecha de la última compra
    resultRupees = inrAmount / inrPrice

    print(f"resultado final: ",resultRupees)

if __name__ == "__main__":
   fcaMenu()


