import os, requests
from dotenv import load_dotenv
import pandas as pd


load_dotenv()                   # Utilizo dotenv para cargar las variables de entorno
key = os.getenv("AEMET_KEY")    # Cargo la api key

querystring = {"api_key":key}   # Preparo la api_key
headers = {
    'cache-control': "no-cache" # Y los headers
    }

urlEstaciones = "https://opendata.aemet.es/opendata/api/valores/climatologicos/inventarioestaciones/todasestaciones/" # preparo la url
responseEstaciones = requests.request("GET", urlEstaciones, headers=headers, params=querystring).json()               # para traer todos los códigos

urlData = responseEstaciones['datos']                                                               # Filtro la url de la respuesta
responseData = requests.request("GET", urlData, headers=headers, params=querystring).json()         # Y me traigo todos los códigos

df = pd.DataFrame(responseData)                                                                     # Creo un dataframe con los datos
getafe = df[df['nombre'].str.contains('GETAFE', case=False)]                                        # Y busco la que contiene getafe
getafeCode = getafe.iloc[0]['indicativo']                                                             # Busco su código

firstDate = '2024-08-22T08%3A30%3A30UTC'                                                            # Preparo las fechas de búsqueda
secondDate = '2024-08-23T08%3A30%3A30UTC'                                                           #   "             "         "

urlGetafe = f'https://opendata.aemet.es/opendata/api/valores/climatologicos/diarios/datos/fechaini/{firstDate}/fechafin/{secondDate}/estacion/{getafeCode}' #Preparo la URL para obtener las temperaturas

responseGetafe = requests.request("GET", urlGetafe, headers=headers, params=querystring).json()    # y me las traigo

urlFinalData = responseGetafe['datos']                                                             # Accedo a la url que recibo

finalData = requests.request("GET", urlFinalData, headers=headers).json()                          # Y pido los datos que corresponden a las fechas y estación correspondientes

print("┌","-"*40,"┐")

print("  Q1-> ¿Cuantas requests os hacen falta hacer?")
print("  R1 -> 2 Requests para obtener los datos de getafe.\n4 Para obtener la media de las temperaturas")
print(" ","-"*40)
print("  Q2-> ¿Cómo vais a meter getafe?")
print("  R2 -> Realizo un request a la url 'urlEstaciones' la cual me devuelve otra url. Al hacer un request a ésta y filtrar los resultados por Getafe, recibo el código que le corresponde bajo la clave 'indicativo'.")
print(" ","-"*40)
print("  Q3 -> ¿cuál es la request final?")
print("  R3 -> 'finalData' en mi código. Realizo una petición al enlace que contiene los datos meteorológicos de Getafe en las fechas correspondientes")
print(f"  La temperatura media es: {finalData[0]['tmed']}º")                                         # Resultado final
print("└","-"*40,"┘")
