################## Primer Bloque

string = ["flower", "flow", "flight", "flowers"]
menu = [("pizza", 8.5), ("hamburguesa", 7.0), ("ensalada", 5.5), ("pasta", 6.0)]
pedido_cliente = ["pizza", "pasta", "sopa"]

##al ser str una palabra reservada me estaba dando problemas, así que cambié la variable a "string"

## 1
# Longitud de la Cadena Más Larga
# Crea una función que devuelva la longitud de la palabra más larga de la lista strs. Por ejemplo, en el caso de la lista dada, la función debería devolver `7`, ya que la palabra más larga es "flowers", que contiene 7 letras.

def longestChain(string):
    longest = max(string)
    print("La cadena más larga es: "+longest)
    return longest

## 2
# Longitud de la Cadena Más Larga y Más Corta
# Crea una función que devuelva tanto la longitud de la palabra más larga como la longitud de la palabra más corta de la lista `strs`. La función debe devolver ambas longitudes en una misma estructura de datos (por ejemplo, una tupla o un diccionario).
# Para la lista de ejemplo, la función debería devolver 7 como longitud máxima (por "flowers") y `4` como longitud mínima (por "flow").

def longShortChain(string):
    longest = max(string)
    shortest = min(string)
    print("La cadena más larga es: "+longest+ "\nY la más corta: "+shortest)
    return longest, shortest


## 3
# Prefijo Común Más Largo
# Escribe una función que encuentre el prefijo común más largo entre todas las palabras de la lista `strs`. El prefijo común es la parte del principio de las palabras que todas comparten. 
# Por ejemplo:
# - Para la lista `["flower", "flow", "flight"]`, el prefijo común más largo sería `"fl"`.
# - Para la lista `["madera", "madrid", "madrugar"]`, el prefijo común sería `"mad"`.
# - Si no hay ningún prefijo común, como en `["sal", "cal", "vals"]`, la función debería devolver una cadena vacía "".

def longestPrefix(string):
    if not string:
        return ""
        
    min_length = len(min(string, key=len))
    
    for i in range(min_length):
        current_char = string[0][i]
        if not all(s[i] == current_char for s in string):
            return string[0][:i]
    return string[0][:min_length]

## 4
#Usando las funciones anteriores, crea una función que escriba cada resultado en un archivo llamado `salida.txt`. El archivo debe generarse en la misma carpeta en la que estáis trabajando.
# Cada resultado debe estar en una nueva línea dentro del archivo. aquí tenéis información sobre como leer y escribir archivos en Python: https://www.freecodecamp.org/espanol/news/lectura-y-escritura-de-archivos-en-python-como-crear-leer-y-escribir-archivos/.

def createText(string):
    f = open("salida.txt", "w")
    f.write("Cadena mas larga: ")
    f.write(longestChain(string))
    f.write("\nCadena mas larga y mas corta: ")
    f.writelines(longShortChain(string))
    f.write("\nPrefijo mas largo: ")
    f.writelines(longestPrefix(string))
    f.close()

################## Segundo Bloque

# 5: 
#Dada una lista de números
# por ejemplo numlist = [1,2,3,4]
# teneis que devolver true si hay duplicados y False si no los hay 
# numlist = [1,2,3,4] devolvería False pero numlist = [1,1,2,3,4] devolvería True

def duplicateCheck():
    ##con duplicados
    num_list = [2,2,3,4] 

    ## sin duplicados
    ## num_list = [1,2,3,4]
    for i in range(len(num_list)-1):
        if num_list[i] == num_list[i+1]:
            print("true")
            return True
    print("false")
    return False

## 6
# Crear una función que tiene 2 argumentos menú y pedido_cliente
# menu = [("pizza", 8.5), ("hamburguesa", 7.0), ("ensalada", 5.5), ("pasta", 6.0)]
# pedido_cliente = ["pizza", "pasta", "sopa"]
# menú es una lista de tuplas donde el primer elemento es lo que pides y el segundo es un float que es el precio
# el pedido es una lista de lo que pides
# Teneis que devolver un ticket de compra como este donde le dais los platos que ha pedido y están en el menú y di no lo está no los añades al # ticket pero no das error
# luego das el precio total, en algo como esto
# {
#   "pizza": 8.5,
#    "pasta": 6.0
# y en la misma función también das el precio que serían 14.5
# el menú no puede tener platos repetidos.

def ticket(menu, pedido):
    precios_menu = dict(menu)

    ## Variables para total
    items_validos = []
    subtotal = 0
    
    # cada item del pedido
    for item in pedido:
        if item in precios_menu:
            precio = precios_menu[item]
            items_validos.append((item, precio))
            subtotal += precio
    
    # Suponiendo que hay impuestos a cobrar
    impuesto = subtotal * 0.21
    total = subtotal + impuesto
    
    # Print del ticket
    print("\n=== TICKET ===")
    print("Items pedidos:")
    for item, precio in items_validos:
        print(f"- {item}: ${precio:.2f}")
    print("-" * 20)
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Impuesto (21%): ${impuesto:.2f}")
    print(f"Total: ${total:.2f}")

################## Menú ejercicios

def mainMenu(string):
    menuInput = input("Escoge el ejercicio: \n(1)Cadena más larga\n(2) Cadenas más larga y más corta\n (3)Prefijo Común Más Largo\n (4)Escritura de Resultados en Archivo \n(5) Cadenas más larga y más corta\n(6) Ticket compra\n")
    menuInputInt = int(menuInput)
    if menuInputInt == 1:
        longestChain(string)
    elif menuInputInt == 2:
        longShortChain(string)
    elif menuInputInt == 3:
        print(longestPrefix(string))
    elif menuInputInt == 4:
        createText(string)
    elif menuInputInt == 5:
        duplicateCheck()
    elif menuInputInt == 6:
        ticket(menu, pedido_cliente)
    else:
        print(f'El número introducido " {menuInput} " no corresponde a ninguna operación programada, por favor, intentelo de nuevo.')
        mainMenu()


mainMenu(string) ## Inicialización aplicación



