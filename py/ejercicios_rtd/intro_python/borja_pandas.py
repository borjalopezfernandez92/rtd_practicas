import pandas as pd
import json
from pathlib import Path
import requests
from sqlalchemy import create_engine


def load_config(filename='connection_data.json'):
    """Load configuration data from JSON file"""
    try:
        file_path = Path(filename)
        if not file_path.exists():
            raise FileNotFoundError(f"Configuration file '{filename}' not found.")
        with open(filename, 'r') as f:
            config = json.load(f)
        required_keys = ['host', 'database', 'user', 'password']
        if not all(key in config for key in required_keys):
            raise ValueError(f"Missing required configuration keys: {required_keys}")
        return config
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON file: {e}")
        raise
    except Exception as e:
        print(f"Error loading configuration: {e}")
        raise

def create_database_engine(config):
    """Create a SQLAlchemy engine for database connection"""
    try:
        url = f"postgresql://{config['user']}:{config['password']}@{config['host']}/{config['database']}"
        engine = create_engine(url)
        return engine
    except Exception as e:
        print(f"Error creating database engine: {e}")
        raise

def search(query):
    try:
        config = load_config()
        engine = create_database_engine(config)

        query = query
        df = pd.read_sql_query(query,engine)
        dataFrame = pd.DataFrame(data=df)

        return dataFrame
    except Exception as e:
        print(f"Error executing database operation: {e}")
        raise

def mainPandas():
    try:
        config = load_config()
        engine = create_database_engine(config)
        
        # query de ejercicio 2 "devuelvan el id y precio total de la orden de id 10248 (order_details) en un dataframe"
        query = """
        SELECT order_id, round(sum(unit_price * quantity)) AS cantidad_total
        FROM order_details 
        WHERE order_id = 10248
        GROUP BY order_id;
        """
        
        # Ejecución de Query y creación de dataframe
        df = pd.read_sql_query(query, engine)
        dataFrame = pd.DataFrame(data=df)
        # print("Data loaded successfully:")
        # print(dataFrame)
        get_currency(dataFrame)
        return dataFrame
        
    except Exception as e:
        print(f"Error executing database operation: {e}")
        raise



def get_currency(dataFrame):
    url = f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc"
    response = requests.get(url).json()
    res_tuplas = () # Inicialización tupla

    name = response[0]['name'] # variable con nombre
    res_tuplas = res_tuplas + tuple(name.split()) # agrego tupla con split para coger palabra completa

    price = response[0]['current_price'] # variable con precio actual
    dataFrame = dataFrame['cantidad_total'] * price
    res_tuplas = res_tuplas + (dataFrame,) # agrego tupla con split para coger valor completo
    # print(res_tuplas)


if __name__ == "__main__":
   mainPandas()
