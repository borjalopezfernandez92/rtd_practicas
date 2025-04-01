import requests, os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("weather_key")

# Exercise tasks:
# 1. Convert temperature from Celsius to Fahrenheit
# 2. Parse the condition text into categories
# 3. Create a structured summary dictionary
# pagination:
# 4. Implement pagination to fetch all pages
# 5. Combine data from multiple pages
# 6. Handle rate limiting delays
def menu(api_key):
    requestType = input("Escoge elejercicio: \n(1)Convert temperature from Celsius to Fahrenheit\n(2)Parse the condition text into categories\n(3)Create a structured summary dictionary\n")
    requestInt = int(requestType)

    if requestInt == 1:
        transform_weather_data(api_key)
    elif requestInt == 2:
        condition_categories(api_key)
    elif requestInt == 3:
        summary_dict(api_key)


def transform_weather_data(api_key):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q=London"
    response = requests.get(url).json()
    print(f"La temperatura en grados celsius es:[{response['current']['temp_c']}] y en fahrenheit es:[{response['current']['temp_f']}]")

def condition_categories(api_key):
    location = input(f"Escribe un lugar del cual quieras saber sus condiciones meteorológicas: ")
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}"
    response = requests.get(url).json()
    condition = response['current']['condition']['text']
    print(f"Las condiciones meteorológicas en {location} son: {condition}")

def summary_dict(api_key):
    location = input(f"Escribe un lugar del cual quieras obtener datos meteorológicos: ")
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}"
    response = requests.get(url).json()

    data = {
        "localización": {
            "nombre" : response['location']['name'],
            "region": response['location']['region'],
            "pais": response['location']['country'],
            "latitud": response['location']['lat'],
            "longitud": response['location']['lon'],
            "tz_id": response['location']['tz_id'],
            "fecha_hora_epoch": response['location']['localtime_epoch'],
            "fecha_hora": response['location']['localtime'],
        },
        "actual":{
            "ultima_actualizacion_epoch":response['current']['last_updated_epoch'],
            "ultima_actualizacion": response['current']['last_updated'],
            "temp_celsius": response['current']['temp_c'],
            "temp_fahrenheit": response['current']['temp_f'],
            "es_dia": response['current']['is_day'],
            "condicion":{
                "texto":  response['current']['condition']['text'],
                "icono":  response['current']['condition']['icon'],
                "codigo":  response['current']['condition']['code'],
            },
            "viento_mph": response['current']['wind_mph'],
            "viento_kph": response['current']['wind_kph'],
            "grados_viento": response['current']['wind_degree'],
            "dir_viento": response['current']['wind_dir'],
            "presion_mb": response['current']['pressure_mb'],
            "presion_pulg": response['current']['pressure_in'],
            "precip_mm": response['current']['precip_mm'],
            "precip_pulg": response['current']['precip_in'],
            "humedad": response['current']['humidity'],
            "nube": response['current']['cloud'],
            "percep_temp_celsius": response['current']['feelslike_c'],
            "percep_temp_fahren": response['current']['feelslike_f'],
            "viento_temp_celsius": response['current']['windchill_c'],
            "viento_temp_fahren": response['current']['windchill_f'],
            "indice_temp_celsius": response['current']['heatindex_c'],
            "indice_temp_fahren": response['current']['heatindex_f'],
            "punto_condensacion_celsius": response['current']['dewpoint_c'],
            "punto_condensacion_fahren": response['current']['dewpoint_f'],
            "vis_km": response['current']['vis_km'],
            "vis_millas": response['current']['vis_miles'],
            "uv": response['current']['uv'],
            "rafaga_mph": response['current']['gust_mph'],
            "rafaga_kph": response['current']['gust_kph'],
        }
    }
    print(data)

def pagination():
    params = {"_page": 1, "_limit": 10}
    base_url = "https://jsonplaceholder.typicode.com/posts&{params}"

    response = requests.get(base_url).json()
    print(response)

menu(api_key)