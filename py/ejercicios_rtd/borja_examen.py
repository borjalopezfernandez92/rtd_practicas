from borja_pandas import *
import pandas as pd
from borja_FreecurrencyAPI import *
from datetime import datetime,timedelta

def menuTest():
    requestTest = input("Escoge el ejercicio: \n(1)\n(2)")
    requestTestInt = int(requestTest)
    if requestTestInt == 1:
        ej1()
    elif requestTestInt == 2:
        ej2()


def ej1():
        print("Enunciado ejercicio1: \nTenéis que, usando las APIs de places y geolocation obtener los restaurantes que hay en un radio de un km de aquí (Avenida Manoteras 26, 28050 Madrid) la respuesta debe estar en un dataframe con al menos el nombre del restaurante y su dirección")


def ej2(sheet="Hoja1"):
    print("Enunciado ejercicio2: \nConectaros a la base de datos de northwind y sacad los productos de la tabla productos queremos hacer una compra de productos (northwind.Products). Esa compra está en un fichero excel, tenéis que dar el precio total de la compra en formato float.")
    print("-"*20)
    menu = input(f"Escoge la opción deseada\n (1)Crear excel\n (2)Leer compra")
    menuInt = int(menu)
    
    if menuInt == 1:    # En caso de que no tenga el excel creado lo pinto como necesito
            query = """
        SELECT * from northwind.products
        """ # Extraigo los datos de la DB

            products = search(query)

            pd.read_excel('compra.xlsx')   # Leo el excel con la compra

            with pd.ExcelWriter('compra.xlsx', mode='a', engine='openpyxl') as writer:  # Y pinto el formato de compra del excel
                book = writer.book
                if sheet in book.sheetnames:
                    del book[sheet]
                
                df_to_write = products[["product_name", "unit_price"]].copy()           # Pinto las columnas que me interesan existentes en la DB        
                df_to_write['bought_amount'] = ""                                        # Y le agrego una columna para la cantidad de productos comprados
                df_to_write.to_excel(
                    writer,
                    sheet_name=sheet,
                    index=False
                )

    elif menuInt == 2:                              # En caso de que ya tenga el excel completado, lo leo
            pd.read_excel('compra.xlsx')

            df = pd.DataFrame({                     # Creo el DataFrame a partir del excel
            'product_name': pd.read_excel('compra.xlsx')['product_name'],
            'unit_price': pd.read_excel('compra.xlsx')['unit_price'],
            'bought_amount': pd.read_excel('compra.xlsx')['bought_amount']
        })

            total_price = (df['unit_price'] * df['bought_amount']).sum()    #Calculo el precio total

            print("\nPrecio total:", total_price)                           # Y lo muestro

            df['total_price'] = df['unit_price'] * df['bought_amount']      # Muestro también el precio unitario, la cantidad comprada y el total de cada cantidad
            print("\nDetalle por producto:")
            print(df[['product_name', 'unit_price', 'bought_amount', 'total_price']])

            print("Ejercicio extra 2")
            print("-"*20)

            ##### Ejercicio extra 2
            yesterday = datetime.now() - timedelta(days=1)
            format_date = yesterday.strftime('%Y-%m-%d')
            gbpPrice = currencyHistorical(format_date, ["USD"], "GBP")
            print(f"Valor libras ->",gbpPrice)
            total_price_gbp = gbpPrice * total_price
        
            print(f"Teniendo un valor en dólares de [",round(total_price, 2),"], el valor total en libras es de [",round(total_price_gbp, 2),"]")


if __name__ == "__main__":
   menuTest()