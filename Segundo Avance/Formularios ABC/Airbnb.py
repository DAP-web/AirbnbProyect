"""
Este va a ser el main de toda la aplicación AIRBNB
"""
from Login import (
    connection,
    signin
)
from ClientesApp_FE import AppClientes
from ReservasApp_FE import reservasAdmin
from ResidenciaApp_FE import residenciasAppAdmin

def AirbnbClientes():
    print("Inicializando la app de Airbnb...")
    while True:
        Menu = """\nBienvenido a la plataforma de Airbnb
        Elija una de las siguientes opciones:
        0-Salir de la app
        1-Ingresar a mi cuenta
        2-Registrarse
        3-Buscar residencias
        4-Buscar experiencias
        5-Buscar experiencias en línea\n"""
        print("-"*100)
        print(Menu)
        print("-"*100)
        option = int(input("Opción: "))

        if option == 0:
            print("\nDeteniendo la aplicación de Airbnb...")
            connection.close()
            break
        if option == 1:
            signin()
        if option == 2:
            pass
        if option == 3:
            pass
        if option == 4:
            pass

def AirbnbAdmin():
    print("Inicializando la app de Airbnb para administradores...")
    while True:
        Menu = """\nBienvenido a la plataforma de Airbnb
        Elija una de las siguientes opciones:
        0-Salir de la app
        1-Ver Clientes
        2-Ver Reservaciones
        3-Ver Residencias
        4-Gestionar Direcciones en la BD
        5-Gestionar Ciudades en la BD
        6-Gestionar Paises en la BD
        7-Buscar experiencias en línea\n"""
        print("-"*100)
        print(Menu)
        print("-"*100)
        option = int(input("Opción: "))

        if option == 0:
            print("\nDeteniendo la aplicación de Airbnb...")
            connection.close()
            break
        if option == 1:
            AppClientes()
        if option == 2:
            reservasAdmin()
        if option == 3:
            residenciasAppAdmin()
        if option == 4:
            pass
        if option == 5:
            pass
        if option == 6:
            pass
        if option == 7:
            pass
        if option == 8:
            pass

AirbnbAdmin()