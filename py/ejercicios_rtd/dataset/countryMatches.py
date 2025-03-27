from rapidfuzz import fuzz

def is_us_match(x):
        try:
            x = str(x)
            # Búsqueda de matches exactos
            if x.upper() in ['US', 'USA', 'UNITED STATES', 'UNITED STATES OF AMERICA']:
                return True
            
            # Si no encuentra, fuzz match
            for valid_name in ['US', 'USA', 'UNITED STATES', 'UNITED STATES OF AMERICA']:
                score = fuzz.ratio(x.upper(), valid_name)
                if score > 80:  # ajuste de threshold
                    return True
            return False
        except:
            return False
        
def is_uk_match(x):
    try:
        x=str(x)
        if x.upper() in ['UK', 'UNITED KINGDOM', 'GB', 'GREAT BRITAIN', 'BRITAIN', 'ENGLAND', 'SCOTLAND', 'WALES', 'NORTHERN IRELAND']:
            return True
        
        for valid_name in ['UK', 'UNITED KINGDOM', 'GB', 'GREAT BRITAIN', 'BRITAIN', 'ENGLAND', 'SCOTLAND', 'WALES', 'NORTHERN IRELAND']:
            score = fuzz.partial_ratio(x.upper(), valid_name)
            if score > 80:
                return True
        return False
    except:
        return False
        
def is_cad_match(x):
    try:
        x=str(x)
        if x.upper() in ['CANADA', 'CAD', 'OTTAWA', 'ONTARIO']:
            return True
        
        for valid_name in ['CANADA', 'CAD', 'OTTAWA', 'ONTARIO']:
            score = fuzz.ratio(x.upper(), valid_name)
            if score > 80:
                return True
        return False
    except:
        return False
    
def is_nl_match(x):
    try:
        x=str(x)
        if x.upper() in ['NETHERLANDS', 'NL', 'HOLLAND', 'AMSTERDAM']:
            return True
        
        for valid_name in ['NETHERLANDS', 'NL', 'HOLLAND', 'AMSTERDAM']:
            score = fuzz.ratio(x.upper(), valid_name)
            if score > 80:
                return True
        return False
    except:
        return False
    
def is_af_match(x):
    try:
        x=str(x)
        if x.upper() in ['AFGHANISTAN', 'KABUL', 'AF']:
            return True
        
        for valid_name in ['AFGHANISTAN', 'KABUL', 'AF']:
            score = fuzz.ratio(x.upper(), valid_name)
            if score > 80:
                return True
        return False
    except:
        return False
        
def is_nz_match(x):
    try:
        x=str(x)
        if x.upper() in ['NEW ZEALAND', 'AOTEAROA', 'nZ']:
            return True
        
        for valid_name in ['NEW ZEALAND', 'AOTEAROA', 'nZ']:
            score = fuzz.ratio(x.upper(), valid_name)
            if score > 80:
                return True
        return False
    except:
        return False
    

def is_ar_match(x):
    try:
        x=str(x)
        if x.upper() in ['ARGENTINA', 'AR', 'BUENOS AIRES', 'CIUDAD AUTONOMA DE BUENOS AIRES']:
            return True
        
        for valid_name in ['ARGENTINA', 'AR', 'BUENOS AIRES', 'CIUDAD AUTONOMA DE BUENOS AIRES']:
            score = fuzz.ratio(x.upper(), valid_name)
            if score > 80:
                return True
        return False
    except:
        return False

if __name__ == "__main__":
    is_us_match()
    is_cad_match()
    is_nl_match()
    is_uk_match()
    is_af_match()
    is_nz_match()
    is_ar_match()