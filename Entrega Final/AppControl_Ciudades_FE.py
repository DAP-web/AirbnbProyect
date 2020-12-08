from Logic_CiudadesLogic import CiudadesLogic
from View_Ciudades import ciudadesBE

def AppCiudades():
    dbciudad = CiudadesLogic()
    beciudad = ciudadesBE()
    print("Inicializando la app de Airbnb Ciudades")
    while True:
        Menu = """\nElija una de las siguientes opciones:
        0-Salir de la app
        1- Recuperar todas las ciudades
        2-Ingresar una nueva ciudad
        3-Actualizar ciudad
        4-Eliminar ciudad\n"""
        print("-"*100)
        print(Menu)
        print("-"*100)
        option = int(input("Opción: "))

        if option == 0:
            print("\nDeteniendo la aplicación de Airbnb Ciudades")
            # dbciudad.connection.close()
            break
        if option == 1:
            beciudad.getAllCities()
        if option == 2:
            beciudad.addCity()
        if option == 3:
            beciudad.updateCity()
        if option == 4:
            beciudad.deleteCity()