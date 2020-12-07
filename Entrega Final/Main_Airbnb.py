from Login import signin
from Core_databaseX import DatabaseX
from AppControl_Anfitrion_FE import AppAnfitrion

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
        5-Buscar experiencias en línea
        6-Ser anfitrión\n"""
        print("-"*100)
        print(Menu)
        print("-"*100)
        option = int(input("Opción: "))

        if option == 0:
            print("\nDeteniendo la aplicación de Airbnb...")
            DatabaseX().connection.close()
            break
        if option == 1:
            signin()
            pass
        if option == 2:
            pass
        if option == 3:
            pass
        if option == 4:
            pass
        if option == 5:
            pass
        if option == 6:
            AppAnfitrion()

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
        7-Gestionar Calificaciones
        8-Gestionar Accesibilidades
        9-Ver descripciones de accesibilidades
        10-Ver Servicios disponibles
        11-Ver experiencias
        12-Gestionar temáticas experiencias
        13-Gestionar las residencias de las experiencias\n"""
        print("-"*100)
        print(Menu)
        print("-"*100)
        option = int(input("Opción: "))

        # if option == 0:
        #     print("\nDeteniendo la aplicación de Airbnb...")
        #     #connection.close()
        #     break
        # if option == 1:
        #     #AppClientes()
        # if option == 2:
        #     #reservasAdmin()
        # if option == 3:
        #     #residenciasAppAdmin()
        # if option == 4:
        #     #direccionesAdmin()
        # if option == 5:
        #     #AppCiudades()
        # if option == 6:
        #     #AppPaises()
        # if option == 7:
        #     #AppCalificaciones()
        # if option == 8:
        #     #accesibilidadesAdmin()
        # if option == 9:
        #    # desc_accesibilidadAppAdmin()
        # if option == 10:
        #    # ServiciosAdmin()
        # if option == 11:
        #    # ExperienciasAppAdmin()
        # if option == 12:
        #   #  AppTematica()
        # if option ==13:
        #  #   ExperienciaresidenciasAppAdmin()
        
AirbnbClientes()