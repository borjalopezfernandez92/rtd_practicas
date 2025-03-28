import pandas as pd
import json
from pathlib import Path
from sqlalchemy import create_engine
from functions import *


################## Configuración

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

################## DB Engine
def create_database_engine(config):
    """Create a SQLAlchemy engine for database connection"""
    try:
        url = f"postgresql://{config['user']}:{config['password']}@{config['host']}/{config['database']}"
        engine = create_engine(url)
        return engine
    except Exception as e:
        print(f"Error creating database engine: {e}")
        raise


def searchTest():       ## Función guía para query simple en DB northwind
    try:
        config = load_config()
        engine = create_database_engine(config)
        
        query = """
        SELECT * from borja.question
        """
        
        # Ejecución de Query y creación de dataframe
        df = pd.read_sql_query(query, engine)
        dataFrame = pd.DataFrame(data=df)
        # print("Data loaded successfully:")
        print(dataFrame)
        return dataFrame
        
    except Exception as e:
        print(f"Error executing database operation: {e}")
        raise

def getData(file):

    excelData = pd.read_excel(file) # Leo el excel

    ## TimeStamp
    timeStamp_convert = pd.to_datetime(excelData.iloc[:, 0]).dt.floor('min') #Convierto el timestamp para coger sólo hasta los minutos
    
    ## Edad
    age_data = excelData.iloc[:, 1]                                          # Convierto la edad en integer que harán función de ID a una tabla de rangos de edad
    age_convert = []                                                         # Lista inicializada para almacenar las edades
    for age in age_data:                                                     # Formateo de las edades usando función encargada de ello.
        age_convert.append(formatAge(age))

    ## Industria
    industry_data = excelData.iloc[:, 2].str.lower()                         # Obtengo los valores en la columna de las industrias y lo reduzco a minúsculas
    industry_convert,industry_extra = formatIndustry(industry_data)          # llamo a la función que se encarga de formatearlo, en la cual cojo la primera palabra de cada entrada y el resto aparte.

    ## Job Title
    jobTitle_data = excelData.iloc[:, 3].str.lower()                         # Obtengo los títulos de trabajo 

    ## Job Title Extra
    jobTitleExtra_data = excelData.iloc[:, 4].str.lower()                    # Obtengo la información extra de los títulos de trabajo
    jobTitleExtra_data_convert = formatJobTitleExtra(jobTitleExtra_data)     # Llamo a la función encargada del formateo

    ## Salary
    salary_data = excelData.iloc[:, 5]                                       # Obtengo el salario

    ## Bonus salary
    bonusSalary_data = excelData.iloc[:, 6]                                  # Obtengo los extras del salario si existen
    bonusSalary_data_converted = formatBonusSalary(bonusSalary_data)         # Y los paso a la función que los formatea. Sustituye los valores nulos por 0 para poder calcularlo después.

    ## Divisa
    currency_data = excelData.iloc[:, 7]                                     # Obtengo la columna currency
    currency_data_extra = excelData.iloc[:, 8]                               # Y la que tiene la información extra
    currency_data_converted = formatCurrency(currency_data, currency_data_extra)   # La formateo en una función donde en el caso de que la divisa sea "other", se trae la información que haya en la columna contigua.

    ## Additional Income
    addIncome_data = excelData.iloc[:, 9]
    addIncome_data_converted = formatAddIncome(addIncome_data)

    ## Country
    country_data = excelData.iloc[:, 10]
    country_data_converted = formatCountry(country_data)
    print(f"-> {country_data[0]}")
    # print(us)
    print(country_data_converted)

    # print(f"original -> {len(country_data)}")
    # ## DataFrame
    # df = pd.DataFrame({
    #     'time_stamp': timeStamp_convert,                                     # Inserción de timestamp formateado
    #     'age': age_convert,                                                  # Inserción de edad formateada
    #     'industry': industry_convert,                                        # Inserto las industrias a modo de categoría
    #     'industry_extra': industry_extra,                                    # Y guardo el resto de la información de las categorías
    #     'job_title': jobTitle_data,                                          # Inserción de los títulos de los trabajos
    #     'job_title_extra': jobTitleExtra_data_convert,                       # Y de información extra cuando existe
    #     'salary': salary_data,                                               # Inserción del salario
    #     'bonus_salary': bonusSalary_data_converted,                          # Inserción de los bonus del salario
    #     'currency': currency_data_converted,                                 # Inserción de currency
    #     'additional_income': addIncome_data_converted,                       # Inserción de información adicional sobre el income
    #     'country': country_data_converted,
    # })

    # print(df)


if __name__ == "__main__":
    getData("dataSet.xlsx")
