from rapidfuzz import fuzz
import unicodedata

def create_country_matcher(valid_terms):
    def matcher(x):
        try:
            # Normalización de texto
            x = str(x).lower()
            x = unicodedata.normalize('NFKD', x).encode('ascii', 'ignore').decode('utf-8')
            tokens = []
            for token in x.split():
                cleaned_token = ''.join(c for c in token if c.isalnum())
                if cleaned_token:
                    tokens.append(cleaned_token)
                    
            normalized_terms = [
                unicodedata.normalize('NFKD', term.lower())
                .encode('ascii', 'ignore')
                .decode('utf-8')
                for term in valid_terms
            ]
            
            # Primero buscar coincidencias exactas
            for token in tokens:
                if token in normalized_terms:
                    return True
            
            # Si no hay coincidencia exacta, buscar coincidencias difusas
            best_score = 0
            for token in tokens:
                for valid_term in normalized_terms:
                    score = fuzz.partial_token_sort_ratio(token, valid_term)
                    best_score = max(best_score, score)
            
            return best_score > 90
            
        except Exception as e:
            print(f"Error processing token: {str(e)}")
            return False
            
    return matcher


if __name__ == "__main__":
    create_country_matcher()