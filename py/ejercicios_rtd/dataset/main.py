import pandas as pd
import json
from pathlib import Path
import requests
from sqlalchemy import create_engine


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
    salary_data = excelData.iloc[:, 5]

    ## Bonus salary
    bonusSalary_data = excelData.iloc[:, [6]]
    bonusSalary_data_converted = formatBonusSalary(bonusSalary_data)
    print(bonusSalary_data)
    ## DataFrame
    df = pd.DataFrame({
        'time_stamp': timeStamp_convert,                                     # Inserción de timestamp formateado
        'age': age_convert,                                                  # Inserción de edad formateada
        'industry': industry_convert,                                        # Inserto las industrias a modo de categoría
        'industry_extra': industry_extra,                                    # Y guardo el resto de la información de las categorías
        'job_title': jobTitle_data,                                          # Inserción de los títulos de los trabajos
        'job_title_extra': jobTitleExtra_data_convert,                       # Y de información extra cuando existe
        'salary': salary_data,                                               # Inserción del salario
        'bonus_salary': bonusSalary_data_converted,
    })

    print(df)

def formatBonusSalary(data):
    formated_data = []

    for i in data:
        print(f"here{i}")
        if isinstance(i, float):
            formated_data.append(0)
        else:
            formated_data.append(i)
    return formated_data


def formatJobTitleExtra(data):
    formated_data = []
    for i in data:
        if isinstance(i, str):
            formated_data.append(i)
        else:
            formated_data.append("na")
    
    return formated_data


def formatIndustry(industryData):   ## Función que maneja el formato de la industria
    industry_list = []              ## Lista que almacenará las industriar
    industry_extra = []             ## Lista que almacenará la información extra

    for industry in industryData:   ## Recorro la lista que recibo por parámetro y de cada valor compruebo:
        if isinstance (industry, str):  ## Compruebo si es un string
            if len(industry.split()) == 1:  ## Y si trae una sola palabra
                industry_list.append(industry.split()[0])   ## Para agregar esta palabra a la lista
                industry_extra.append("na")               ## Y un valor predeterminado a extra al estar vacío.
            else:                                           ## Si el valor tiene más de una palabra
                industry_list.append(industry.split()[0])   ## cojo la primera palabra como industria
                industry_extra.append(' '.join(industry.split()[1:])if len(industry.split()) > 1 else "") ## Y el resto como extra
        else:
            industry_list.append("unclassified")    # En caso de que el valor no sea un string, lo formateo como industria sin clasificar
            industry_extra.append("na")           # haciendo lo mismo con la información extra

    return industry_list,industry_extra


def formatAge(age): #función que convierte los rangos de edad en ids para insertar en DB

    if isinstance(age, int):    # formato que espera integers
        if age < 18:
            return 0
        elif age >= 18 and age < 25:
            return 1
        elif age >= 25 and age < 35:
            return 2
        elif age >= 35 and age < 45:
            return 3
        elif age >= 45 and age < 55:
            return 4
        elif age >= 55 and age < 65:
            return 5
        elif age >= 65:
            return 6
    
    elif isinstance(age, str):  # formato encontrado en el excel
        if age == "18-24":
            return 1
        elif age == "25-34":
            return 2
        elif age == "35-44":
            return 3
        elif age == "45-54":
            return 4
        elif age == "55-64":
            return 5
        elif age == "65 or over":
            return 6
        else:
            return 0

if __name__ == "__main__":
    getData("dataSet.xlsx")
