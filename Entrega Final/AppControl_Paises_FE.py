from Logic_PaisesLogic import PaisesLogic
from View_Paises import paisesBE

def AppPaises():
    dbpais = PaisesLogic()
    bepais = paisesBE()
    print("Inicializando la app de Airbnb Paises")
    while True:
        Menu = """\nElija una de las siguientes opciones:
        0-Salir de la app
        1- Recuperar todos los paises
        2-Ingresar un nuevo país
        3-Actualizar país
        4-Eliminar país\n"""
        print("-"*100)
        print(Menu)
        print("-"*100)
        option = int(input("Opción: "))

        if option == 0:
            print("\nDeteniendo la aplicación de Airbnb Paises")
            #dbpais.connection.close()
            break
        if option == 1:
            bepais.getAllCountries()
        if option == 2:
            bepais.addCountry()
        if option == 3:
            bepais.updateCountry()
        if option == 4:
            bepais.deleteCountry()

# AppPaises()