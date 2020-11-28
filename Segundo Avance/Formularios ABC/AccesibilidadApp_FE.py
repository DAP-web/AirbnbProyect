from Accesiblidad_BE import accesibilidad
from DB_Accesibilidad_BE import AccesibilidadDB

def accesibilidadesAdmin():
    accesibilidadbe=accesibilidad()
    accesibilidadbd=AccesibilidadDB()
    print("Inicializando la app de Airbnb Accesibilidad")
    while True:
        Menu = """\nElija una de las siguientes opciones:
        0-Salir de la app
        1- Recuperar todos las accesibilidades
        2-Ingresar una nueva accesibilidad
        3-Actualizar accesibilidad
        4-Eliminar accesibilidad\n"""
        print("-"*100)
        print(Menu)
        print("-"*100)
        option = int(input("Opción: "))

        if option == 0:
            print("\nDeteniendo la aplicación de Airbnb Accesibilidad")
            #accesibilidadbd.connection.close()
            break
        if option == 1:
            accesibilidadbe.getAllAccessibilities()
        if option == 2:
            accesibilidadbe.addAccessibility()
        if option == 3:
            accesibilidadbe.updateAccessibility()
        if option == 4:
            accesibilidadbe.deleteAccessibility()
            
#accesibilidadesAdmin()