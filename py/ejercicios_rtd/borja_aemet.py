import os, requests
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("AEMET_KEY")

print(key)

url = "https://opendata.aemet.es/opendata/api/prediccion/especifica/municipio/horaria/065"

querystring = {"api_key":key}
print(querystring)

headers = {
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)