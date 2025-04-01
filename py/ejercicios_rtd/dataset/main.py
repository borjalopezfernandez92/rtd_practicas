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
    """
    Convierto el timestamp para coger sólo hasta los minutos
    """
    timeStamp_convert = pd.to_datetime(excelData.iloc[:, 0]).dt.floor('min') 
    
    ## Edad
    """
    Convierto la edad en integer que harán función de ID a una tabla de rangos de edad
    """
    age_data = excelData.iloc[:, 1]
    age_convert = []
    for age in age_data:
        age_convert.append(formatAge(age))

    ## Industria
    """
    Obtengo los valores en la columna de las industrias y lo reduzco a minúsculas
    luego llamo a la función que se encarga de formatearlo, en la cual cojo la primera palabra de cada entrada y aparto el resto.
    """
    industry_data = excelData.iloc[:, 2].str.lower()
    industry_convert,industry_extra = formatIndustry(industry_data)

    ## Job Title
    """
    Obtengo los títulos de trabajo pasándolos a minúscula
    """
    jobTitle_data = excelData.iloc[:, 3].str.lower()
    ## Job Title Extra
    """
    Obtengo la información extra de los títulos de trabajo en minúscula
    Y Llamo a la función encargada del formateo; si no recibe un string, devuelve 'noData' al ser no ser data valido
    """
    jobTitleExtra_data = excelData.iloc[:, 4].str.lower()
    jobTitleExtra_data_convert = formatJobTitleExtra(jobTitleExtra_data) 

    ## Salary
    """
    Simplemente obtengo el salario
    """
    salary_data = excelData.iloc[:, 5]                                       

    ## Bonus salary
    """
    Obtengo los extras del salario si existen
    Y los paso a la función que los formatea, 
    la cual sustituye los valores nulos por 0 para poder calcularlo después.
    """
    bonusSalary_data = excelData.iloc[:, 6] 
    bonusSalary_data_converted = formatBonusSalary(bonusSalary_data)

    ## Divisa
    """
    Obtengo la columna currency y la que tiene la información extra.
    La formateo en una función donde en el caso de que la divisa sea "other", se trae la información que haya en la columna contigua.
    """
    currency_data = excelData.iloc[:, 7]
    currency_data_extra = excelData.iloc[:, 8]
    currency_data_converted = formatCurrency(currency_data, currency_data_extra)

    ## Additional Income
    """
    Formateo los datos devolviendo "noData" cuando los campos estén vacíos
    """
    addIncome_data = excelData.iloc[:, 9]
    addIncome_data_converted = formatAddIncome(addIncome_data)

    ## Country
    """
    Obtengo los países, las palabras que los relacionan y sus códigos de un json externo
    Llamo a la función que ataca casos concretos dificiles de filtrar.
    Dentro de esta función llamo a otra función encargada de formatear los países (formatCountry()).
    Aquí convierto todos los inputs en el código del país que le corresponda, obteniendo finalmente los códigos de cada país.
    """
    country_configs = load_country_configs('country_configs.json') 
    country_data_converted = formatUnMatchedCountries(excelData, country_configs)

    ## US State
    """
    Utilizo librería "us" para validar los inputs comparándolos con estados norteamericanos.
    Si el input no es un estado válido devolverá "other(invalid_data)".
    Hay un par de casos difíciles de filtrar que he atacado directamente.
    """
    state_data = excelData
    column = "If you're in the U.S., what state do you work in?"
    state_data.replace({column: 'District of Columbia'}, {column: 'Washington'}, inplace=True)  # Sustitución de inputs difíciles de filtrar
    state_data.replace({column: 'DC'}, {column: 'Washington'}, inplace=True)
    state_data_converted = formatStates(state_data.iloc[:,11])

    ## City
    """
    Al no requerir validación de ciudades implemento los datos tal y como se encuentran.
    """
    city_data = excelData.iloc[:, 12]

    ## Work Experience
    """
    Formateo las edades convirtiéndo los inputs en números que servirán como ID para una tabla que los relacionará.
    """
    we_data = excelData
    column = "How many years of professional work experience do you have overall?"
    we_data_converted = formatExperience(we_data, column, 13)

    ## Field Experience
    """
    Reutilizando la misma función que en el WorkExperience hago lo mismo.
    """
    fe_dat = excelData
    column = "How many years of professional work experience do you have in your field?"  
    fe_dat_converted = formatExperience(fe_dat, column, 14)

    ## Education
    """
    Formateo los inputs en números que servirán como ID para una tabla que los relacionará.
    """
    education_data = excelData
    education_data_converted = formatEducation(education_data)

    ## Gender
    """
    Formateo los inputs en números que servirán como ID para una tabla que los relacionará.
    """
    gender_data = excelData
    gender_data_converted = formatEducation(gender_data)

    ## Race
    """
    En el caso de que haya múltiples razas escogidas, sustituyo el input por "múltiple"
    """
    race_data = excelData
    race_data_converted = formatRace(race_data)

    #### DataFrame
    """
    Construcción del dataframe
    """
    df = pd.DataFrame({
        'time_stamp': timeStamp_convert,                                     # Inserción de timestamp formateado
        'age': age_convert,                                                  # Inserción de edad formateada
        'industry': industry_convert,                                        # Inserto las industrias a modo de categoría
        'industry_extra': industry_extra,                                    # Y guardo el resto de la información de las categorías
        'job_title': jobTitle_data,                                          # Inserción de los títulos de los trabajos
        'job_title_extra': jobTitleExtra_data_convert,                       # Y de información extra cuando existe
        'salary': salary_data,                                               # Inserción del salario
        'bonus_salary': bonusSalary_data_converted,                          # Inserción de los bonus del salario
        'currency': currency_data_converted,                                 # Inserción de currency
        'additional_income': addIncome_data_converted,                       # Inserción de información adicional sobre el income
        'country': country_data_converted,                                   # Inserción de países
        'us_state': state_data_converted,                                    # Inserción de estados americanos
        'city': city_data,                                                   # Inserción de ciudades
        'work_experience': we_data_converted,                                # Inserción años de experiencia trabajados
        'field_experience': fe_dat_converted,                                # Inserción de años experiencia campo trabajo
        'education': education_data_converted,                               # Inserción de mayor nivel educación
        'gender': gender_data_converted,                                     # Inserción de género
        'race': race_data_converted                                          # Inserción de Raza

    })

    print(df)
    df.to_excel('clean_data.xlsx', index=False) # Creación de excel con datos limpios


if __name__ == "__main__":
    getData("dataSet.xlsx")
