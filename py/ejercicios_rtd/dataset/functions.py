import pandas as pd
import numpy as np
import re
from rapidfuzz import fuzz
from countryMatches import *

def textCleaner(text):
    clean_text = []
    for i in text:
        clean_parenth = re.sub(r'\([^)]*\)', '', i)
        clean_dot_comma = clean_parenth.replace(".", "").replace(",", "").upper()

        clean_text.append(clean_dot_comma)

    return clean_text

def formatCountry(data):
        
    country_configs = {
        'US': {'mask_func': is_us_match, 'code': 'US'},
        'GB': {'mask_func': is_uk_match, 'code': 'GB'},
        'CAD': {'mask_func': is_cad_match, 'code': 'CAD'},
        'NL': {'mask_func': is_nl_match, 'code': 'NL'},
        'AF': {'mask_func': is_af_match, 'code': 'AF'},
        'NZ': {'mask_func': is_nz_match, 'code': 'NZ'},
        'AR': {'mask_func': is_ar_match, 'code': 'AR'},
    }

    masks = {country: data.apply(config['mask_func'])
            for country, config in country_configs.items()}
    
    formated_data = data.copy()
    all_masks = pd.Series(False, index=data.index)

    for country in ['US', 'GB', 'CAD', 'NL', 'AF','NZ']:
        mask = masks[country]
        exclude_mask = all_masks if all_masks.any() else pd.Series(False, index=data.index)
        final_mask = mask & ~exclude_mask
        formated_data[final_mask] = country_configs[country]['code']
        all_masks |= mask

    return formated_data

def formatCurrency(data,dataExtra):                     # Formateo de divisa
    formated_data = []

    for i in range(len(data)):                          # Recorro data e igualo las posiciones de las dos variables. En el momento en el que el valor de data es "other", almacena el valor de la misma fila de la columna contigua (dataExtra).
        current_currency = data[i]
        extra_value = dataExtra[i]
        
        if current_currency.lower() == "other":
            if pd.notna(extra_value):
                formated_data.append(extra_value)
            else:
                formated_data.append("other(unknown)")
        else:
            formated_data.append(current_currency)
    return formated_data

def formatAddIncome(data):                                # Función que formatea la información extra del income
    return ["noData" if pd.isna(x) else x for x in data]  # Devolverá "noData" cuando el valor sea NaN, es decir, cuando los campos estén vacíos.


def formatBonusSalary(data):                # Función que formatea el extra del salario
    formated_data = []

    for i in data:
        if np.isnan(i):                    # Comprueba si recibe NaN, en cual caso devolverá 0, sino, devolverá el valor numérico.
            formated_data.append(0)
        else:
            formated_data.append(i)
    return formated_data


def formatJobTitleExtra(data):              # Función que formatea la información extra de los títulos de trabajo
    formated_data = []
    for i in data:                          # Comprueba que reciba un string, y si no es así asume que no es data valido, devolviendo "noData"
        if isinstance(i, str):
            formated_data.append(i)
        else:
            formated_data.append("noData")
    
    return formated_data


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