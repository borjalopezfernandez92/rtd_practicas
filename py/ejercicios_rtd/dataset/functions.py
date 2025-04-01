import pandas as pd
import numpy as np
from typing import List, Tuple
import re, json, us
from rapidfuzz import fuzz
from countryMatches import *

def textCleaner(text):
    clean_text = []
    for i in text:
        clean_parenth = re.sub(r'\([^)]*\)', '', i)
        clean_dot_comma = clean_parenth.replace(".", "").replace(",", "").upper()

        clean_text.append(clean_dot_comma)

    return clean_text

def load_country_configs(path):
    """Load country configurations from JSON file."""
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Could not find configuration file at {path}")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {path}")
        return {}

def formatCountry(data, country_configs):

    masks = {country: data.apply(create_country_matcher(config['valid_terms']))
             for country, config in country_configs.items()}
    
    clean_data = data.copy()
    all_masks = pd.Series(False, index=data.index)
    
    for country in country_configs.keys():
        mask = masks[country]
        exclude_mask = all_masks if all_masks.any() else pd.Series(False, index=data.index)
        final_mask = mask & ~exclude_mask
        clean_data[final_mask] = country_configs[country]['code']
        all_masks |= mask

    clean_data[~all_masks] = 'other'
    
    return clean_data


def formatUnMatchedCountries(data, country_configs):
    ## Para reemplazar una celda concreta agregar una línea con la siguiente estructura:
    ##     data.replace({column: 'Texto a reemplazar'}, {column: 'Texto de reemplazo'}, inplace=True)

    column = 'What country do you work in?'
    data.replace({column: 'Trinidad and tobago'}, {column: 'TT'}, inplace=True)
    data.replace({column: 'I.S.'}, {column: 'america'}, inplace=True)
    data.replace({column: 'The Bahamas'}, {column: 'Bahamas'}, inplace=True)
    data.replace({column: 'Costa Rica'}, {column: 'C0R'}, inplace=True)
    data.replace({column: 'Company in Germany. I work from Pakistan.'}, {column: 'Pakistan'}, inplace=True)
    data.replace({column: 'San Francisco'}, {column: 'america'}, inplace=True)
    data.replace({column: 'From New Zealand but on projects across APAC'}, {column: 'new zealand'}, inplace=True)
    data.replace({column: "I work for an US based company but I'm from Argentina."}, {column: 'argentina'}, inplace=True)
    data.replace({column: 'ARGENTINA BUT MY ORG IS IN THAILAND'}, {column: 'argentina'}, inplace=True)
    data.replace({column: 'na'}, {column: 'america'}, inplace=True)
    data.replace({column: 'Bosnia and Herzegovina'}, {column: 'B0SN14'}, inplace=True)
    data.replace({column: 'Tanzania'}, {column: 'T4NZ4'}, inplace=True)
    data.replace({column: 'nz'}, {column: 'Z34L4ND'}, inplace=True)

    codeFormat = formatCountry(data.iloc[:, 10], country_configs)

    return codeFormat

def formatCurrency(data,dataExtra):                     # Formateo de divisa
    clean_data = []

    for i in range(len(data)):                          # Recorro data e igualo las posiciones de las dos variables. En el momento en el que el valor de data es "other", almacena el valor de la misma fila de la columna contigua (dataExtra).
        current_currency = data[i]
        extra_value = dataExtra[i]
        
        if current_currency.lower() == "other":
            if pd.notna(extra_value):
                clean_data.append(extra_value)
            else:
                clean_data.append("other(unknown)")
        else:
            clean_data.append(current_currency)
    return clean_data

def formatStates(state_data) -> List[str]:              # Función formalización de estados
    results = []
    
    for state_entry in state_data:
                                                        # En caso de NaN
        if pd.isna(state_entry):
            results.append(f"other(invalid_data)")
            continue
            
        state_str = str(state_entry).strip().upper()
                                                        # Búsqueda de estados
        try:
            state = us.states.lookup(state_str)
                                                        # En caso de None
            if state is None:
                results.append(f"other(invalid_data)")
            else:
                results.append(state.name)
                
        except KeyError:
            results.append(f"other(invalid_data)")
            
    return results


def formatAddIncome(data):                                # Función que formatea la información extra del income
    return ["noData" if pd.isna(x) else x for x in data]  # Devolverá "noData" cuando el valor sea NaN, es decir, cuando los campos estén vacíos.


def formatBonusSalary(data):                # Función que formatea el extra del salario
    clean_data = []

    for i in data:
        if np.isnan(i):                    # Comprueba si recibe NaN, en cual caso devolverá 0, sino, devolverá el valor numérico.
            clean_data.append(0)
        else:
            clean_data.append(i)
    return clean_data


def formatJobTitleExtra(data):              # Función que formatea la información extra de los títulos de trabajo
    clean_data = []
    for i in data:                          # Comprueba que reciba un string, y si no es así asume que no es data valido, devolviendo "noData"
        if isinstance(i, str):
            clean_data.append(i)
        else:
            clean_data.append("noData")
    
    return clean_data

def formatEducation(data):

    column = 'What is your highest level of education completed?'
    data[column] = data[column].fillna(0)

    education_map = {
        "Master's degree": 1,
        "College degree": 2,
        "PhD": 3,
        "High School": 4,
        "Professional degree (MD, JD, etc.)": 5,
        "Some college": 6
    }
    data[column] = data[column].replace(education_map)

    return data.iloc[:,15]

def formatGender(data):
    column = 'What is your gender?'
    data[column] = data[column].fillna(0)

    gender_map = {
        "Man": 1,
        "Non-binary":2,
        "Other or prefer not to answer": 3,
        "Prefer not to answer": 4,
        "Woman":5
    }
    data[column] = data[column].replace(gender_map)

    return data.iloc[:,16]


def formatRace(data):
    column = 'What is your race? (Choose all that apply.)'
    data[column] = data[column].str.replace(',', ' or ', regex=False)
    data[column] = data[column].apply(lambda x: 'multiple' if str(x).count('or') > 1 else x)
    data[column] = data[column].fillna('noData')
    return data.iloc[:,17]


def formatIndustry(industryData):   ## Función que maneja el formato de la industria
    industry_list = []              ## Lista que almacenará las industriar
    industry_extra = []             ## Lista que almacenará la información extra

    for industry in industryData:   ## Recorro la lista que recibo por parámetro y de cada valor compruebo:
        if isinstance (industry, str):  ## Compruebo si es un string
            if len(industry.split()) == 1:  ## Y si trae una sola palabra
                industry_list.append(industry.split()[0])   ## Para agregar esta palabra a la lista
                industry_extra.append("noData")               ## Y un valor predeterminado a extra al estar vacío.
            else:                                           ## Si el valor tiene más de una palabra
                industry_list.append(industry.split()[0])   ## cojo la primera palabra como industria
                industry_extra.append(' '.join(industry.split()[1:])if len(industry.split()) > 1 else "") ## Y el resto como extra
        else:
            industry_list.append("unclassified")    # En caso de que el valor no sea un string, lo formateo como industria sin clasificar
            industry_extra.append("noData")           # haciendo lo mismo con la información extra

    return industry_list,industry_extra


def formatExperience(data, column, position):
    data.replace({column: '1 year or less'}, {column: 1}, inplace=True)
    data.replace({column: '2 - 4 years'}, {column: 2}, inplace=True)
    data.replace({column: '5-7 years'}, {column: 3}, inplace=True)
    data.replace({column: '8 - 10 years'}, {column: 4}, inplace=True)
    data.replace({column: '11 - 20 years'}, {column: 5}, inplace=True)
    data.replace({column: '21 - 30 years'}, {column: 6}, inplace=True)
    data.replace({column: '31 - 40 years'}, {column: 7}, inplace=True)
    data.replace({column: '41 years or more'}, {column: 8}, inplace=True)

    return data.iloc[:, position]

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
    formatAge()
    formatIndustry()
    formatJobTitleExtra()
    formatBonusSalary()
    formatAddIncome()
    formatCurrency()
    formatUnMatchedCountries()
    formatStates()
    formatExperience()
    formatEducation()
    textCleaner()
    load_country_configs()
    formatGender()
    formatRace()