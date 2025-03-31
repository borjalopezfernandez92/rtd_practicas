import pandas as pd
import numpy as np
import re, json
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
    # country_configs = {
    #     'US': {'mask_func': is_us_match, 'code': 'US'},
    #     'GB': {'mask_func': is_uk_match, 'code': 'GB'},
    #     'CA': {'mask_func': is_ca_match, 'code': 'CA'},
    #     'NL': {'mask_func': is_nl_match, 'code': 'NL'},
    #     'AF': {'mask_func': is_af_match, 'code': 'AF'},
    #     'NZ': {'mask_func': is_nz_match, 'code': 'NZ'},
    #     'AR': {'mask_func': is_ar_match, 'code': 'AR'},
    #     'AU': {'mask_func': is_au_match, 'code': 'AU'},
    #     'SP': {'mask_func': is_sp_match, 'code': 'SP'},
    #     'FL': {'mask_func': is_fl_match, 'code': 'FL'},
    #     'FR': {'mask_func': is_fr_match, 'code': 'FR'},
    #     'DE': {'mask_func': is_de_match, 'code': 'DE'},
    #     'IE': {'mask_func': is_ie_match, 'code': 'IE'},
    #     'IN': {'mask_func': is_in_match, 'code': 'IN'},
    #     'ISA': {'mask_func': is_isa_match, 'code': 'ISA'},
    #     'DK': {'mask_func': is_dk_match, 'code': 'DK'},
    #     'CH': {'mask_func': is_ch_match, 'code': 'CH'},
    #     'BM': {'mask_func': is_bm_match, 'code': 'BM'},
    #     'MY': {'mask_func': is_my_match, 'code': 'MY'},
    #     'MX': {'mask_func': is_mx_match, 'code': 'MX'},
    #     'ZA': {'mask_func': is_za_match, 'code': 'ZA'},
    #     'SE': {'mask_func': is_se_match, 'code': 'SE'},
    #     'HK': {'mask_func': is_hk_match, 'code': 'HK'},
    #     'KW': {'mask_func': is_kw_match, 'code': 'KW'},
    #     'NO': {'mask_func': is_no_match, 'code': 'NO'},
    #     'LK': {'mask_func': is_lk_match, 'code': 'LK'},
    #     'VI': {'mask_func': is_vi_match, 'code': 'VI'},
    #     'GR': {'mask_func': is_gr_match, 'code': 'GR'},
    #     'JP': {'mask_func': is_jp_match, 'code': 'JP'},
    #     'BR': {'mask_func': is_br_match, 'code': 'BR'},
    #     'HU': {'mask_func': is_hu_match, 'code': 'HU'},
    #     'LU': {'mask_func': is_lu_match, 'code': 'LU'},
    #     'CO': {'mask_func': is_co_match, 'code': 'CO'},
    #     'TT': {'mask_func': is_tt_match, 'code': 'TT'},
    #     'KY': {'mask_func': is_ky_match, 'code': 'KY'},
    #     'CZ': {'mask_func': is_cz_match, 'code': 'CZ'},
    #     'LV': {'mask_func': is_lv_match, 'code': 'LV'},
    #     'PR': {'mask_func': is_pr_match, 'code': 'PR'},
    #     'RW': {'mask_func': is_rw_match, 'code': 'RW'},
    #     'AE': {'mask_func': is_ae_match, 'code': 'AE'},
    #     'BD': {'mask_func': is_bd_match, 'code': 'BD'},
    #     'RO': {'mask_func': is_ro_match, 'code': 'RO'},
    #     'RS': {'mask_func': is_rs_match, 'code': 'RS'},
    #     'PH': {'mask_func': is_ph_match, 'code': 'PH'},
    #     'RU': {'mask_func': is_ru_match, 'code': 'RU'},
    #     'PL': {'mask_func': is_pl_match, 'code': 'PL'},
    #     'TR': {'mask_func': is_tr_match, 'code': 'TR'},
    #     'IT': {'mask_func': is_it_match, 'code': 'IT'},
    #     'JE': {'mask_func': is_je_match, 'code': 'JE'},
    #     'CN': {'mask_func': is_cn_match, 'code': 'CN'},
    #     'IL': {'mask_func': is_il_match, 'code': 'IL'},
    #     'TW': {'mask_func': is_tw_match, 'code': 'TW'},
    #     'KH': {'mask_func': is_kh_match, 'code': 'KH'},
    #     'VN': {'mask_func': is_vn_match, 'code': 'VN'},
    #     'SG': {'mask_func': is_sg_match, 'code': 'SG'},
    #     'KR': {'mask_func': is_kr_match, 'code': 'KR'},
    #     'TH': {'mask_func': is_th_match, 'code': 'TH'},



    #     'other': {'mask_func': is_other_match, 'code': 'other'},
    # }

    masks = {country: data.apply(create_country_matcher(config['valid_terms']))
             for country, config in country_configs.items()}
    
    formatted_data = data.copy()
    all_masks = pd.Series(False, index=data.index)
    
    for country in country_configs.keys():
        mask = masks[country]
        exclude_mask = all_masks if all_masks.any() else pd.Series(False, index=data.index)
        final_mask = mask & ~exclude_mask
        formatted_data[final_mask] = country_configs[country]['code']
        all_masks |= mask
    
    return formatted_data


    # masks = {country: data.apply(config['mask_func'])
    #         for country, config in country_configs.items()}
    
    # formated_data = data.copy()
    # all_masks = pd.Series(False, index=data.index)

    # for country in country_configs.keys():
    #     mask = masks[country]
    #     exclude_mask = all_masks if all_masks.any() else pd.Series(False, index=data.index)
    #     final_mask = mask & ~exclude_mask
    #     formated_data[final_mask] = country_configs[country]['code']
    #     all_masks |= mask

    # return formated_data


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