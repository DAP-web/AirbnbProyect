from Login import signin
from Core_databaseX import DatabaseX
from AppControl_Anfitrion_FE import AppAnfitrion
from View_Clientes import clientesBE
from ImportsMain import Admin

def AirbnbClientes():
    adminCliente = Admin()
    print("Inicializando la app de Airbnb...")
    while True:
        Menu = """\nBienvenido a la plataforma de Airbnb
        Elija una de las siguientes opciones:
        0-Salir de la app
        1-Ingresar a mi cuenta
        2-Registrarse como cliente
        3-Buscar residencias
        4-Buscar experiencias
        5-Ser anfitrión\n"""
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
        if option == 2:
            clientesBE().ClienteRegistro()
        if option == 3:
            pass
        if option == 4:
            adminCliente.buscarExpFull()
        if option == 5:
            AppAnfitrion()

def AirbnbAdmin():
    admin = Admin()
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
        9-Ver Accesibilidades-Residencia
        10-Ver Servicios disponibles
        11-Ver experiencias
        12-Gestionar temáticas experiencias
        13-Gestionar las residencias de las experiencias
        14-Ver Facturas App\n"""
        print("-"*100)
        print(Menu)
        print("-"*100)
        option = int(input("Opción: "))

        if option == 0:
            print("\nDeteniendo la aplicación de Airbnb...")
            DatabaseX().connection.close()
            break
        if option == 1:
            admin.ClientesApp()
        if option == 2:
            admin.ReservasApp()
        if option == 3:
            admin.ResidenciaApp()
        if option == 4:
            admin.DireccionesApp()
        if option == 5:
            admin.CiudadesApp()
        if option == 6:
            admin.PaisesApp()
        if option == 7:
            admin.CalificacionesApp()
        if option == 8:
            admin.AccesibilidadesApp()
        if option == 9:
            admin.AccResApp()
        if option == 10:
            admin.ServiciosApp()
        if option == 11:
            admin.experienciaApp()
        if option == 12:
            pass
        if option ==13:
            admin.expResApp()
        if option == 14:
            admin.FacturasApp()
        
# AirbnbAdmin()
AirbnbClientes()