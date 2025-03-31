from rapidfuzz import fuzz
# import fuzzywuzzy.fuzz as fuzz
from typing import Dict, List, Union

# def is_us_match(x):     # United States 'US'
#     try:
#         x = str(x)
#         tokens = []
#         for token in x.split():
#             cleaned_token = ''.join(c for c in token if c.isalnum()).upper()
#             if cleaned_token:
#                 tokens.append(cleaned_token)
        
#         valid_terms = ['US', 'USA', 'UNITED STATES', 'AMERICA', 'HARTFORD', 'VIRGINIA']
        
#         for token in tokens:
#             if token in valid_terms:
#                 return True
        
#         for token in tokens:
#             for valid_term in valid_terms:
#                 score = fuzz.partial_token_sort_ratio(token, valid_term)
#                 if score > 80:
#                     return True
                    
#         return False
        
#     except Exception as e:
#         print(f"Error processing token: {str(e)}")
#         return False

        
# def is_uk_match(x):     # Britain 'GB'
#     try:
#         x=str(x)
#         tokens = x.upper().split()
#         valid_terms = ['UK', 'UNITED KINGDOM', 'GB','BRITAIN', 'ENGLAND', 'SCOTLAND', 'WALES', 'NORTHERN']

#         for token in tokens:
#             if token in valid_terms:
#                 return True
            
#         for valid_term in valid_terms:
#             score = fuzz.partial_token_sort_ratio(token, valid_term)

#             if score > 80:
#                     return True
#         return False
#     except:
#         return False
        
# def is_ca_match(x):    # Canada 'CA'

#     try:
#         x=str(x)
#         tokens = x.upper().split()
#         valid_terms = ['CANADA', 'OTTAWA', 'ONTARIO']

#         for token in tokens:
#             if token in valid_terms:
#                 return True
            
#         for valid_term in valid_terms:
#             score = fuzz.partial_token_sort_ratio(token, valid_term)

#             if score > 80:
#                     return True
#         return False
#     except:
#         return False
    
# def is_nl_match(x):     # Netherlands 'NL'

#     try:
#         x=str(x)
#         tokens = ''.join(c for c in x if c.isalnum() or c.isspace()).upper().split()
#         valid_terms = ['NETHERLANDS', 'AMSTERDAM']

#         for token in tokens:
#             if token in valid_terms:
#                 return True
            
#         for valid_term in valid_terms:
#             score = fuzz.partial_token_sort_ratio(token, valid_term)

#             if score > 95:
#                     return True
#         return False
#     except:
#         return False
        
# def is_af_match(x):     # Afghanistan 'AF'

#     try:
#         x=str(x)
#         tokens = ''.join(c for c in x if c.isalnum() or c.isspace()).upper().split()
#         valid_terms = ['AFGHANISTAN', 'KABUL']

#         for token in tokens:
#             if token in valid_terms:
#                 return True
            
#         for valid_term in valid_terms:
#             score = fuzz.partial_token_sort_ratio(token, valid_term)

#             if score > 80:
#                     return True
#         return False
#     except:
#         return False
        
# def is_nz_match(x):     # New Zealand 'nz'

#     try:
#         x=str(x)
#         tokens = ''.join(c for c in x if c.isalnum() or c.isspace()).upper().split()
#         valid_terms = ['NEW ZEALAND', 'nZ']

#         for token in tokens:
#             if token in valid_terms:
#                 return True
            
#         for valid_term in valid_terms:
#             score = fuzz.partial_token_sort_ratio(token, valid_term)

#             if score > 80:
#                     return True
#         return False
#     except:
#         return False
    

# def is_ar_match(x):     # Argentine 'AR'
#     try:
#         x=str(x)
#         tokens = x.upper().split()
#         valid_terms = ['ARGENTINA']

#         for token in tokens:
#             if token in valid_terms:
#                 return True
        
#         for valid_term in valid_terms:
#             score = fuzz.partial_token_sort_ratio(token, valid_term)

#             if score > 80:
#                 return True
#         return False
#     except:
#         return False

# def is_au_match(x):     # Australia 'AU'
#     try:
#         x=str(x)
#         tokens = x.upper().split()
#         valid_terms = ['AUSTRALIA']

#         for token in tokens:
#             if token in valid_terms:
#                 return True
        
#         for valid_term in valid_terms:
#             score = fuzz.partial_token_sort_ratio(token, valid_term)

#             if score > 95:
#                 return True
#         return False
#     except:
#         return False
    

# def is_sp_match(x):     # Spain 'SP'
#     try:
#         x=str(x)
#         tokens = x.upper().split()
#         valid_terms = ['SPAIN', 'ESPAÑA', 'CATALONIA']

#         for token in tokens:
#             if token in valid_terms:
#                 return True
        
#         for valid_term in valid_terms:
#             score = fuzz.partial_token_sort_ratio(token, valid_term)

#             if score > 80:
#                 return True
#         return False
#     except:
#         return False
    
# def is_fl_match(x):     # Finland 'FL'
#     try:
#         x=str(x)
#         tokens = ''.join(c for c in x if c.isalnum() or c.isspace()).upper().split()
#         valid_terms = ['FINLAND', 'HELSINKI']

#         for token in tokens:
#             if token in valid_terms:
#                 return True
        
#         for valid_term in valid_terms:
#             score = fuzz.partial_token_sort_ratio(token, valid_term)
#             if score > 80:
#                     return True
            
#         return False
#     except:
#         return False

# def is_fr_match(x):     # France 'FR'
#     try:
#         x=str(x)
#         tokens = ''.join(c for c in x if c.isalnum() or c.isspace()).upper().split()
#         valid_terms = ['FRANCE', 'PARIS']

#         for token in tokens:
#             if token in valid_terms:
#                 return True
        
#         for valid_term in valid_terms:
#             score = fuzz.partial_token_sort_ratio(token, valid_term)

#             if score > 80:
#                     return True
#         return False
#     except:
#         return False

# def is_de_match(x):     # Germany 'DE'
#     try:
#         x=str(x)
#         tokens = ''.join(c for c in x if c.isalnum() or c.isspace()).upper().split()
#         valid_terms = ['GERMANY', 'FEDERAL REPUBLIC OF GERMANY','GERMAN FEDERAL REPUBLIC', 'DEUTSCHLAND']

#         for token in tokens:
#             if token in valid_terms:
#                 return True
            
#         for valid_term in valid_terms:
#             score = fuzz.partial_token_sort_ratio(token, valid_term)

#             if score > 80:
#                     return True
#         return False
#     except:
#         return False
    
# def is_ie_match(x):     # Ireland 'IE'
#     try:
#         x=str(x)
#         tokens = ''.join(c for c in x if c.isalnum() or c.isspace()).upper().split()
#         valid_terms = ['IRELAND', 'DUBLIN']

#         for token in tokens:
#             if token in valid_terms:
#                 return True
            
#         for valid_term in valid_terms:
#             score = fuzz.partial_token_sort_ratio(token, valid_term)

#             if score > 80:
#                     return True
#         return False
#     except:
#         return False

# def is_in_match(x):     # India 'IN'
#     try:
#         x=str(x)
#         tokens = ''.join(c for c in x if c.isalnum() or c.isspace()).upper().split()
#         valid_terms = ['INDIA', 'DEHLI', 'NEW DEHLI']

#         for token in tokens:
#             if token in valid_terms:
#                 return True
            
#         for valid_term in valid_terms:
#             score = fuzz.partial_token_sort_ratio(token, valid_term)

#             if score > 80:
#                     return True
#         return False
#     except:
#         return False


# def is_isa_match(x):     # International Solar Alliance 'ISA'
#     try:
#         x=str(x)
#         tokens = ''.join(c for c in x if c.isalnum() or c.isspace()).upper().split()
#         valid_terms = ['ISA', 'INTERNATIONAL SOLAR ALLIANCE']

#         for token in tokens:
#             if token in valid_terms:
#                 return True
            
#         for valid_term in valid_terms:
#             score = fuzz.partial_token_sort_ratio(token, valid_term)

#             if score > 80:
#                     return True
#         return False
#     except:
#         return False

# def is_dk_match(x):     # Denmark 'DK'
#     try:
#         x=str(x)
#         tokens = ''.join(c for c in x if c.isalnum() or c.isspace()).upper().split()
#         valid_terms = ['DENMARK', 'COPENHAGEN']

#         for token in tokens:
#             if token in valid_terms:
#                 return True
            
#         for valid_term in valid_terms:
#             score = fuzz.partial_token_sort_ratio(token, valid_term)

#             if score > 80:
#                     return True
#         return False
#     except:
#         return False

# def is_ch_match(x):     # Switzerland 'CH'
#     try:
#         x=str(x)
#         tokens = ''.join(c for c in x if c.isalnum() or c.isspace()).upper().split()
#         valid_terms = ['SWITZERLAND']

#         for token in tokens:
#             if token in valid_terms:
#                 return True
            
#         for valid_term in valid_terms:
#             score = fuzz.partial_token_sort_ratio(token, valid_term)

#             if score > 80:
#                     return True
#         return False
#     except:
#         return False
    

# def is_bm_match(x):     # Bermuda 'BM'
#     try:
#         x=str(x)
#         tokens = ''.join(c for c in x if c.isalnum() or c.isspace()).upper().split()
#         valid_terms = ['BERMUDA', 'HAMILTON']

#         for token in tokens:
#             if token in valid_terms:
#                 return True
            
#         for valid_term in valid_terms:
#             score = fuzz.partial_token_sort_ratio(token, valid_term)

#             if score > 80:
#                     return True
#         return False
#     except:
#         return False


# def is_my_match(x):     # Malaysia 'MY'
#     try:
#         x=str(x)
#         tokens = ''.join(c for c in x if c.isalnum() or c.isspace()).upper().split()
#         valid_terms = ['MALAYSIA', 'KUALA LUMPUR']

#         for token in tokens:
#             if token in valid_terms:
#                 return True
            
#         for valid_term in valid_terms:
#             score = fuzz.partial_token_sort_ratio(token, valid_term)

#             if score > 80:
#                     return True
#         return False
#     except:
#         return False
    

# def is_mx_match(x):     # MEXICO 'MX'
#     try:
#         x=str(x)
#         tokens = ''.join(c for c in x if c.isalnum() or c.isspace()).upper().split()
#         valid_terms = ['MEXICO', 'MEJICO', 'CIUDAD DE MEXICO']

#         for token in tokens:
#             if token in valid_terms:
#                 return True
            
#         for valid_term in valid_terms:
#             score = fuzz.partial_token_sort_ratio(token, valid_term)

#             if score > 80:
#                     return True
#         return False
#     except:
#         return False
    
# def is_za_match(x):     # South Africa 'ZA'
#     try:
#         x=str(x)
#         tokens = ''.join(c for c in x if c.isalnum() or c.isspace()).upper().split()
#         valid_terms = ['SOUTH AFRICA', 'PRETORIA', 'CAPE TOWN', 'BLOEMFONTEIN']

#         for token in tokens:
#             if token in valid_terms:
#                 return True
            
#         for valid_term in valid_terms:
#             score = fuzz.partial_token_sort_ratio(token, valid_term)

#             if score > 80:
#                     return True
#         return False
#     except:
#         return False   


# def is_se_match(x):     # Sweden 'SE'
#     try:
#         x=str(x)
#         tokens = ''.join(c for c in x if c.isalnum() or c.isspace()).upper().split()
#         valid_terms = ['SWEDEN', 'STOKHOLM']

#         for token in tokens:
#             if token in valid_terms:
#                 return True
            
#         for valid_term in valid_terms:
#             score = fuzz.partial_token_sort_ratio(token, valid_term)

#             if score > 80:
#                     return True
#         return False
#     except:
#         return False


# def is_hk_match(x):     # Hong Kong 'HK'
#     try:
#         x = str(x)
#         tokens = []
#         for token in x.split():
#             cleaned_token = ''.join(c for c in token if c.isalnum()).upper()
#             if cleaned_token:
#                 tokens.append(cleaned_token)
        
#         valid_terms = ['HONK KONG', 'VICTORIA']
        
#         for token in tokens:
#             if token in valid_terms:
#                 return True
        
#         for token in tokens:
#             for valid_term in valid_terms:
#                 score = fuzz.partial_token_sort_ratio(token, valid_term)
#                 if score > 80:
#                     return True
                    
#         return False
        
#     except Exception as e:
#         print(f"Error processing token: {str(e)}")
#         return False
    

# def is_kw_match(x):     # Kuwait 'KW'
#     try:
#         x = str(x)
#         tokens = []
#         for token in x.split():
#             cleaned_token = ''.join(c for c in token if c.isalnum()).upper()
#             if cleaned_token:
#                 tokens.append(cleaned_token)
        
#         valid_terms = ['KUWAIT', 'KUWAIT CITY']
        
#         for token in tokens:
#             if token in valid_terms:
#                 return True
        
#         for token in tokens:
#             for valid_term in valid_terms:
#                 score = fuzz.partial_token_sort_ratio(token, valid_term)
#                 if score > 80:
#                     return True
                    
#         return False
        
#     except Exception as e:
#         print(f"Error processing token: {str(e)}")
#         return False
    

# def is_no_match(x):     # Norway 'NO'
#     try:
#         x = str(x)
#         tokens = []
#         for token in x.split():
#             cleaned_token = ''.join(c for c in token if c.isalnum()).upper()
#             if cleaned_token:
#                 tokens.append(cleaned_token)
        
#         valid_terms = ['NORWAY', 'OSLO']
        
#         for token in tokens:
#             if token in valid_terms:
#                 return True
        
#         for token in tokens:
#             for valid_term in valid_terms:
#                 score = fuzz.partial_token_sort_ratio(token, valid_term)
#                 if score > 80:
#                     return True
                    
#         return False
        
#     except Exception as e:
#         print(f"Error processing token: {str(e)}")
#         return False
    

# def is_lk_match(x):     # Sri Lanka 'LK'
#     try:
#         x = str(x)
#         tokens = []
#         for token in x.split():
#             cleaned_token = ''.join(c for c in token if c.isalnum()).upper()
#             if cleaned_token:
#                 tokens.append(cleaned_token)
        
#         valid_terms = ['SRI LANKA', 'SRI JAYAWARDENEPURA KOTTE']
        
#         for token in tokens:
#             if token in valid_terms:
#                 return True
        
#         for token in tokens:
#             for valid_term in valid_terms:
#                 score = fuzz.partial_token_sort_ratio(token, valid_term)
#                 if score > 80:
#                     return True
                    
#         return False
        
#     except Exception as e:
#         print(f"Error processing token: {str(e)}")
#         return False
    

# def is_vi_match(x):     # Virgin islands (usa) 'VI'
#     try:
#         x = str(x)
#         tokens = []
#         for token in x.split():
#             cleaned_token = ''.join(c for c in token if c.isalnum()).upper()
#             if cleaned_token:
#                 tokens.append(cleaned_token)
        
#         valid_terms = ['VIRGIN']
        
#         for token in tokens:
#             if token in valid_terms:
#                 return True
        
#         for token in tokens:
#             for valid_term in valid_terms:
#                 score = fuzz.partial_token_sort_ratio(token, valid_term)
#                 if score > 80:
#                     return True
                    
#         return False
        
#     except Exception as e:
#         print(f"Error processing token: {str(e)}")
#         return False


# def is_gr_match(x):     # Greece 'GR'
#     try:
#         x = str(x)
#         tokens = []
#         for token in x.split():
#             cleaned_token = ''.join(c for c in token if c.isalnum()).upper()
#             if cleaned_token:
#                 tokens.append(cleaned_token)
        
#         valid_terms = ['GREECE', 'ATHENS']
        
#         for token in tokens:
#             if token in valid_terms:
#                 return True
        
#         for token in tokens:
#             for valid_term in valid_terms:
#                 score = fuzz.partial_token_sort_ratio(token, valid_term)
#                 if score > 80:
#                     return True
                    
#         return False
        
#     except Exception as e:
#         print(f"Error processing token: {str(e)}")
#         return False

# def is_jp_match(x):     # Japan 'JP'
#     try:
#         x = str(x)
#         tokens = []
#         for token in x.split():
#             cleaned_token = ''.join(c for c in token if c.isalnum()).upper()
#             if cleaned_token:
#                 tokens.append(cleaned_token)
        
#         valid_terms = ['JAPAN', 'TOKYO']
        
#         for token in tokens:
#             if token in valid_terms:
#                 return True
        
#         for token in tokens:
#             for valid_term in valid_terms:
#                 score = fuzz.partial_token_sort_ratio(token, valid_term)
#                 if score > 80:
#                     return True
                    
#         return False
        
#     except Exception as e:
#         print(f"Error processing token: {str(e)}")
#         return False
    

# def is_br_match(x):     # Brazil 'BR'
#     try:
#         x = str(x)
#         tokens = []
#         for token in x.split():
#             cleaned_token = ''.join(c for c in token if c.isalnum()).upper()
#             if cleaned_token:
#                 tokens.append(cleaned_token)
        
#         valid_terms = ['BRAZIL','BRASILIA', 'BRASIL']
        
#         for token in tokens:
#             if token in valid_terms:
#                 return True
        
#         for token in tokens:
#             for valid_term in valid_terms:
#                 score = fuzz.partial_token_sort_ratio(token, valid_term)
#                 if score > 80:
#                     return True
                    
#         return False
        
#     except Exception as e:
#         print(f"Error processing token: {str(e)}")
#         return False


# def is_hu_match(x):     # Hungary 'HU'
#     try:
#         x = str(x)
#         tokens = []
#         for token in x.split():
#             cleaned_token = ''.join(c for c in token if c.isalnum()).upper()
#             if cleaned_token:
#                 tokens.append(cleaned_token)
        
#         valid_terms = ['HUNGARY','BUDAPEST']
        
#         for token in tokens:
#             if token in valid_terms:
#                 return True
        
#         for token in tokens:
#             for valid_term in valid_terms:
#                 score = fuzz.partial_token_sort_ratio(token, valid_term)
#                 if score > 80:
#                     return True
                    
#         return False
        
#     except Exception as e:
#         print(f"Error processing token: {str(e)}")
#         return False
    

# def is_lu_match(x):     # Luxembourg 'LU'
#     try:
#         x = str(x)
#         tokens = []
#         for token in x.split():
#             cleaned_token = ''.join(c for c in token if c.isalnum()).upper()
#             if cleaned_token:
#                 tokens.append(cleaned_token)
        
#         valid_terms = ['LUXEMBOURG','LUXEMBOURG CITY']
        
#         for token in tokens:
#             if token in valid_terms:
#                 return True
        
#         for token in tokens:
#             for valid_term in valid_terms:
#                 score = fuzz.partial_token_sort_ratio(token, valid_term)
#                 if score > 80:
#                     return True
                    
#         return False
        
#     except Exception as e:
#         print(f"Error processing token: {str(e)}")
#         return False


# def is_co_match(x):     # Colombia 'CO'
#     try:
#         x = str(x)
#         tokens = []
#         for token in x.split():
#             cleaned_token = ''.join(c for c in token if c.isalnum()).upper()
#             if cleaned_token:
#                 tokens.append(cleaned_token)
        
#         valid_terms = ['COLOMBIA','BOGOTA']
        
#         for token in tokens:
#             if token in valid_terms:
#                 return True
        
#         for token in tokens:
#             for valid_term in valid_terms:
#                 score = fuzz.partial_token_sort_ratio(token, valid_term)
#                 if score > 80:
#                     return True
                    
#         return False
        
#     except Exception as e:
#         print(f"Error processing token: {str(e)}")
#         return False
    

# def is_tt_match(x):     # Trinidad and tobago 'TT'
#     try:
#         x = str(x)
#         tokens = []
#         for token in x.split():
#             cleaned_token = ''.join(c for c in token if c.isalnum()).upper()
#             if cleaned_token:
#                 tokens.append(cleaned_token)
        
#         valid_terms = ['TRINIDAD', 'TOBAGO']
        
#         for token in tokens:
#             if token in valid_terms:
#                 return True
        
#         for token in tokens:
#             for valid_term in valid_terms:
#                 score = fuzz.partial_token_sort_ratio(token, valid_term)
#                 if score > 95:
#                     return True
                    
#         return False
        
#     except Exception as e:
#         print(f"Error processing token: {str(e)}")
#         return False
    
# def is_ky_match(x):     # Kayman Islands 'KY'
#     try:
#         x = str(x)
#         tokens = []
#         for token in x.split():
#             cleaned_token = ''.join(c for c in token if c.isalnum()).upper()
#             if cleaned_token:
#                 tokens.append(cleaned_token)
        
#         valid_terms = ['CAYMAN']
        
#         for token in tokens:
#             if token in valid_terms:
#                 return True
        
#         for token in tokens:
#             for valid_term in valid_terms:
#                 score = fuzz.partial_token_sort_ratio(token, valid_term)
#                 if score > 80:
#                     return True
                    
#         return False
        
#     except Exception as e:
#         print(f"Error processing token: {str(e)}")
#         return False


# def is_cz_match(x):     # Czech Republic 'CZ'
#     try:
#         x = str(x)
#         tokens = []
#         for token in x.split():
#             cleaned_token = ''.join(c for c in token if c.isalnum()).upper()
#             if cleaned_token:
#                 tokens.append(cleaned_token)
        
#         valid_terms = ['CZECH']
        
#         for token in tokens:
#             if token in valid_terms:
#                 return True
        
#         for token in tokens:
#             for valid_term in valid_terms:
#                 score = fuzz.partial_token_sort_ratio(token, valid_term)
#                 if score > 80:
#                     return True
                    
#         return False
        
#     except Exception as e:
#         print(f"Error processing token: {str(e)}")
#         return False


# def is_lv_match(x):     # Latvia 'LV'
#     try:
#         x = str(x)
#         tokens = []
#         for token in x.split():
#             cleaned_token = ''.join(c for c in token if c.isalnum()).upper()
#             if cleaned_token:
#                 tokens.append(cleaned_token)
        
#         valid_terms = ['LATVIA']
        
#         for token in tokens:
#             if token in valid_terms:
#                 return True
        
#         for token in tokens:
#             for valid_term in valid_terms:
#                 score = fuzz.partial_token_sort_ratio(token, valid_term)
#                 if score > 80:
#                     return True
                    
#         return False
        
#     except Exception as e:
#         print(f"Error processing token: {str(e)}")
#         return False
    
# def is_pr_match(x):     # Puerto Rico 'PR'
#     try:
#         x = str(x)
#         tokens = []
#         for token in x.split():
#             cleaned_token = ''.join(c for c in token if c.isalnum()).upper()
#             if cleaned_token:
#                 tokens.append(cleaned_token)
        
#         valid_terms = ['PUERTO RICO']
        
#         for token in tokens:
#             if token in valid_terms:
#                 return True
        
#         for token in tokens:
#             for valid_term in valid_terms:
#                 score = fuzz.partial_token_sort_ratio(token, valid_term)
#                 if score > 80:
#                     return True
                    
#         return False
        
#     except Exception as e:
#         print(f"Error processing token: {str(e)}")
#         return False

# def is_rw_match(x):     # Rwanda 'RW'
#     try:
#         x = str(x)
#         tokens = []
#         for token in x.split():
#             cleaned_token = ''.join(c for c in token if c.isalnum()).upper()
#             if cleaned_token:
#                 tokens.append(cleaned_token)
        
#         valid_terms = ['RWANDA']
        
#         for token in tokens:
#             if token in valid_terms:
#                 return True
        
#         for token in tokens:
#             for valid_term in valid_terms:
#                 score = fuzz.partial_token_sort_ratio(token, valid_term)
#                 if score > 80:
#                     return True
                    
#         return False
        
#     except Exception as e:
#         print(f"Error processing token: {str(e)}")
#         return False

# def is_ae_match(x):     # United Arab Emirates 'AE'
#     try:
#         x = str(x)
#         tokens = []
#         for token in x.split():
#             cleaned_token = ''.join(c for c in token if c.isalnum()).upper()
#             if cleaned_token:
#                 tokens.append(cleaned_token)
        
#         valid_terms = ['ARAB', 'EMIRATES', 'UAE']
        
#         for token in tokens:
#             if token in valid_terms:
#                 return True
        
#         for token in tokens:
#             for valid_term in valid_terms:
#                 score = fuzz.partial_token_sort_ratio(token, valid_term)
#                 if score > 80:
#                     return True
                    
#         return False
        
#     except Exception as e:
#         print(f"Error processing token: {str(e)}")
#         return False

# def is_bd_match(x):     # Bangladesh 'BD'
#     try:
#         x = str(x)
#         tokens = []
#         for token in x.split():
#             cleaned_token = ''.join(c for c in token if c.isalnum()).upper()
#             if cleaned_token:
#                 tokens.append(cleaned_token)
        
#         valid_terms = ['BANGLADESH']
        
#         for token in tokens:
#             if token in valid_terms:
#                 return True
        
#         for token in tokens:
#             for valid_term in valid_terms:
#                 score = fuzz.partial_token_sort_ratio(token, valid_term)
#                 if score > 80:
#                     return True
                    
#         return False
        
#     except Exception as e:
#         print(f"Error processing token: {str(e)}")
#         return False

# def is_ro_match(x):     # Romania 'RO'
#     try:
#         x = str(x)
#         tokens = []
#         for token in x.split():
#             cleaned_token = ''.join(c for c in token if c.isalnum()).upper()
#             if cleaned_token:
#                 tokens.append(cleaned_token)
        
#         valid_terms = ['ROMANIA']
        
#         for token in tokens:
#             if token in valid_terms:
#                 return True
        
#         for token in tokens:
#             for valid_term in valid_terms:
#                 score = fuzz.partial_token_sort_ratio(token, valid_term)
#                 if score > 80:
#                     return True
                    
#         return False
        
#     except Exception as e:
#         print(f"Error processing token: {str(e)}")
#         return False
    
# def is_rs_match(x):     # Serbia 'RS'
#     try:
#         x = str(x)
#         tokens = []
#         for token in x.split():
#             cleaned_token = ''.join(c for c in token if c.isalnum()).upper()
#             if cleaned_token:
#                 tokens.append(cleaned_token)
        
#         valid_terms = ['SERBIA']
        
#         for token in tokens:
#             if token in valid_terms:
#                 return True
        
#         for token in tokens:
#             for valid_term in valid_terms:
#                 score = fuzz.partial_token_sort_ratio(token, valid_term)
#                 if score > 80:
#                     return True
                    
#         return False
        
#     except Exception as e:
#         print(f"Error processing token: {str(e)}")
#         return False
    
# def is_ph_match(x):     # Philippines 'PH'
#     try:
#         x = str(x)
#         tokens = []
#         for token in x.split():
#             cleaned_token = ''.join(c for c in token if c.isalnum()).upper()
#             if cleaned_token:
#                 tokens.append(cleaned_token)
        
#         valid_terms = ['PHILIPPINES']
        
#         for token in tokens:
#             if token in valid_terms:
#                 return True
        
#         for token in tokens:
#             for valid_term in valid_terms:
#                 score = fuzz.partial_token_sort_ratio(token, valid_term)
#                 if score > 80:
#                     return True
                    
#         return False
        
#     except Exception as e:
#         print(f"Error processing token: {str(e)}")
#         return False

# def is_ru_match(x):     # Russia 'RU'
#     try:
#         x = str(x)
#         tokens = []
#         for token in x.split():
#             cleaned_token = ''.join(c for c in token if c.isalnum()).upper()
#             if cleaned_token:
#                 tokens.append(cleaned_token)
        
#         valid_terms = ['RUSSIA']
        
#         for token in tokens:
#             if token in valid_terms:
#                 return True
        
#         for token in tokens:
#             for valid_term in valid_terms:
#                 score = fuzz.partial_token_sort_ratio(token, valid_term)
#                 if score > 80:
#                     return True
                    
#         return False
        
#     except Exception as e:
#         print(f"Error processing token: {str(e)}")
#         return False   

# def is_pl_match(x):     # Poland 'PL'
#     try:
#         x = str(x)
#         tokens = []
#         for token in x.split():
#             cleaned_token = ''.join(c for c in token if c.isalnum()).upper()
#             if cleaned_token:
#                 tokens.append(cleaned_token)
        
#         valid_terms = ['POLAND']
        
#         for token in tokens:
#             if token in valid_terms:
#                 return True
        
#         for token in tokens:
#             for valid_term in valid_terms:
#                 score = fuzz.partial_token_sort_ratio(token, valid_term)
#                 if score > 80:
#                     return True
                    
#         return False
        
#     except Exception as e:
#         print(f"Error processing token: {str(e)}")
#         return False 

# def is_tr_match(x):     # Turkey 'TR'
#     try:
#         x = str(x)
#         tokens = []
#         for token in x.split():
#             cleaned_token = ''.join(c for c in token if c.isalnum()).upper()
#             if cleaned_token:
#                 tokens.append(cleaned_token)
        
#         valid_terms = ['TURKEY']
        
#         for token in tokens:
#             if token in valid_terms:
#                 return True
        
#         for token in tokens:
#             for valid_term in valid_terms:
#                 score = fuzz.partial_token_sort_ratio(token, valid_term)
#                 if score > 80:
#                     return True
                    
#         return False
        
#     except Exception as e:
#         print(f"Error processing token: {str(e)}")
#         return False 


# def is_it_match(x):     # Italy 'IT'
#     try:
#         x = str(x)
#         tokens = []
#         for token in x.split():
#             cleaned_token = ''.join(c for c in token if c.isalnum()).upper()
#             if cleaned_token:
#                 tokens.append(cleaned_token)
        
#         valid_terms = ['ITALY', 'ITALIA']
        
#         for token in tokens:
#             if token in valid_terms:
#                 return True
        
#         for token in tokens:
#             for valid_term in valid_terms:
#                 score = fuzz.partial_token_sort_ratio(token, valid_term)
#                 if score > 80:
#                     return True
                    
#         return False
    
#     except Exception as e:
#         print(f"Error processing token: {str(e)}")
#         return False 

# def is_je_match(x):     # Jersey 'JE'
#     try:
#         x = str(x)
#         tokens = []
#         for token in x.split():
#             cleaned_token = ''.join(c for c in token if c.isalnum()).upper()
#             if cleaned_token:
#                 tokens.append(cleaned_token)
        
#         valid_terms = ['JERSEY']
        
#         for token in tokens:
#             if token in valid_terms:
#                 return True
        
#         for token in tokens:
#             for valid_term in valid_terms:
#                 score = fuzz.partial_token_sort_ratio(token, valid_term)
#                 if score > 80:
#                     return True
                    
#         return False
    
#     except Exception as e:
#         print(f"Error processing token: {str(e)}")
#         return False 

# def is_cn_match(x):     # China 'CN'
#     try:
#         x = str(x)
#         tokens = []
#         for token in x.split():
#             cleaned_token = ''.join(c for c in token if c.isalnum()).upper()
#             if cleaned_token:
#                 tokens.append(cleaned_token)
        
#         valid_terms = ['CHINA']
        
#         for token in tokens:
#             if token in valid_terms:
#                 return True
        
#         for token in tokens:
#             for valid_term in valid_terms:
#                 score = fuzz.partial_token_sort_ratio(token, valid_term)
#                 if score > 80:
#                     return True
                    
#         return False
    
#     except Exception as e:
#         print(f"Error processing token: {str(e)}")
#         return False 

# def is_il_match(x):     # Israel 'IL'
#     try:
#         x = str(x)
#         tokens = []
#         for token in x.split():
#             cleaned_token = ''.join(c for c in token if c.isalnum()).upper()
#             if cleaned_token:
#                 tokens.append(cleaned_token)
        
#         valid_terms = ['ISRAEL']
        
#         for token in tokens:
#             if token in valid_terms:
#                 return True
        
#         for token in tokens:
#             for valid_term in valid_terms:
#                 score = fuzz.partial_token_sort_ratio(token, valid_term)
#                 if score > 80:
#                     return True
                    
#         return False
    
#     except Exception as e:
#         print(f"Error processing token: {str(e)}")
#         return False

# def is_tw_match(x):     # Taiwan 'TW'
#     try:
#         x = str(x)
#         tokens = []
#         for token in x.split():
#             cleaned_token = ''.join(c for c in token if c.isalnum()).upper()
#             if cleaned_token:
#                 tokens.append(cleaned_token)
        
#         valid_terms = ['TAIWAN']
        
#         for token in tokens:
#             if token in valid_terms:
#                 return True
        
#         for token in tokens:
#             for valid_term in valid_terms:
#                 score = fuzz.partial_token_sort_ratio(token, valid_term)
#                 if score > 80:
#                     return True
                    
#         return False
    
#     except Exception as e:
#         print(f"Error processing token: {str(e)}")
#         return False

# def is_kh_match(x):     # Cambodia 'KH'
#     try:
#         x = str(x)
#         tokens = []
#         for token in x.split():
#             cleaned_token = ''.join(c for c in token if c.isalnum()).upper()
#             if cleaned_token:
#                 tokens.append(cleaned_token)
        
#         valid_terms = ['CAMBODIA']
        
#         for token in tokens:
#             if token in valid_terms:
#                 return True
        
#         for token in tokens:
#             for valid_term in valid_terms:
#                 score = fuzz.partial_token_sort_ratio(token, valid_term)
#                 if score > 80:
#                     return True
                    
#         return False
    
#     except Exception as e:
#         print(f"Error processing token: {str(e)}")
#         return False
    
# def is_vn_match(x):     # Vietnam 'VN'
#     try:
#         x = str(x)
#         tokens = []
#         for token in x.split():
#             cleaned_token = ''.join(c for c in token if c.isalnum()).upper()
#             if cleaned_token:
#                 tokens.append(cleaned_token)
        
#         valid_terms = ['VIETNAM']
        
#         for token in tokens:
#             if token in valid_terms:
#                 return True
        
#         for token in tokens:
#             for valid_term in valid_terms:
#                 score = fuzz.partial_token_sort_ratio(token, valid_term)
#                 if score > 80:
#                     return True
                    
#         return False
    
#     except Exception as e:
#         print(f"Error processing token: {str(e)}")
#         return False
    
# def is_sg_match(x):     # Singapore 'SG'
#     try:
#         x = str(x)
#         tokens = []
#         for token in x.split():
#             cleaned_token = ''.join(c for c in token if c.isalnum()).upper()
#             if cleaned_token:
#                 tokens.append(cleaned_token)
        
#         valid_terms = ['SINGAPORE']
        
#         for token in tokens:
#             if token in valid_terms:
#                 return True
        
#         for token in tokens:
#             for valid_term in valid_terms:
#                 score = fuzz.partial_token_sort_ratio(token, valid_term)
#                 if score > 80:
#                     return True
                    
#         return False
    
#     except Exception as e:
#         print(f"Error processing token: {str(e)}")
#         return False
    
# def is_kr_match(x):     # South Korea 'KR'
#     try:
#         x = str(x)
#         tokens = []
#         for token in x.split():
#             cleaned_token = ''.join(c for c in token if c.isalnum()).upper()
#             if cleaned_token:
#                 tokens.append(cleaned_token)
        
#         valid_terms = ['SOUTH KOREA']
        
#         for token in tokens:
#             if token in valid_terms:
#                 return True
        
#         for token in tokens:
#             for valid_term in valid_terms:
#                 score = fuzz.partial_token_sort_ratio(token, valid_term)
#                 if score > 80:
#                     return True
                    
#         return False
    
#     except Exception as e:
#         print(f"Error processing token: {str(e)}")
#         return False
    
# def is_th_match(x):     # Thailand 'TH'
#     try:
#         x = str(x)
#         tokens = []
#         for token in x.split():
#             cleaned_token = ''.join(c for c in token if c.isalnum()).upper()
#             if cleaned_token:
#                 tokens.append(cleaned_token)
        
#         valid_terms = ['THAILAND']
        
#         for token in tokens:
#             if token in valid_terms:
#                 return True
        
#         for token in tokens:
#             for valid_term in valid_terms:
#                 score = fuzz.partial_token_sort_ratio(token, valid_term)
#                 if score > 95:
#                     return True
                    
#         return False
    
#     except Exception as e:
#         print(f"Error processing token: {str(e)}")
#         return False

# def is_other_match(x):     # Not a country 'other'
#     try:
#         x = str(x)
#         tokens = []
#         for token in x.split():
#             cleaned_token = ''.join(c for c in token if c.isalnum()).upper()
#             if cleaned_token:
#                 tokens.append(cleaned_token)
        
#         valid_terms = ['CONTRACT', 'GLOBAL', 'RAISES', 'FINANCE', 'BENEFITS', 'VIRGINIA', 'REMOTE']
        
#         for token in tokens:
#             if token in valid_terms:
#                 return True
        
#         for token in tokens:
#             for valid_term in valid_terms:
#                 score = fuzz.partial_token_sort_ratio(token, valid_term)
#                 if score > 80:
#                     return True
                    
#         return False
        
#     except Exception as e:
#         print(f"Error processing token: {str(e)}")
#         return False    



def create_country_matcher(valid_terms):
    def matcher(x):
        try:
            x = str(x)
            tokens = []
            for token in x.split():
                cleaned_token = ''.join(c for c in token if c.isalnum()).upper()
                if cleaned_token:
                    tokens.append(cleaned_token)
            
            # Exact matches
            for token in tokens:
                if token in valid_terms:
                    return True
            
            # Fuzzy matches
            for token in tokens:
                for valid_term in valid_terms:
                    score = fuzz.partial_token_sort_ratio(token, valid_term)
                    if score > 95:
                        return True
            
            return False
        
        except Exception as e:
            print(f"Error processing token: {str(e)}")
            return False
    
    return matcher


if __name__ == "__main__":
    create_country_matcher()
#     is_us_match()
#     is_ca_match()
#     is_nl_match()
#     is_uk_match()
#     is_af_match()
#     is_nz_match()
#     is_ar_match()
#     is_sp_match()
#     is_fr_match()
#     is_fl_match()
#     is_de_match()
#     is_ie_match()
#     is_in_match()
#     is_isa_match()
#     is_dk_match()
#     is_ch_match()
#     is_bm_match()
#     is_my_match()
#     is_mx_match()
#     is_za_match()
#     is_se_match()
#     is_hk_match()
#     is_kw_match()
#     is_no_match()
#     is_lk_match()
#     is_other_match()
#     is_gr_match()
#     is_jp_match()
#     is_br_match()
#     is_hu_match()
#     is_lu_match()
#     is_co_match()
#     is_tt_match()
#     is_vi_match()
#     is_ky_match()
#     is_lv_match()
#     is_pr_match()
#     is_rw_match()
#     is_ae_match()
#     is_bd_match()
#     is_ro_match()
#     is_rs_match()
#     is_ph_match()
#     is_ru_match()
#     is_pl_match()
#     is_tr_match()
#     is_it_match()
#     is_cn_match()
#     is_tw_match()
#     is_kh_match()
#     is_vn_match()
#     is_sg_match()
#     is_kr_match()
#     is_th_match()