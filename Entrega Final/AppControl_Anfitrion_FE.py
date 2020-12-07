#from Logic_ClientLogic import ClientLogic

from View_Anfitrion import anfitrionBE

# from ReservasApp_FE import(
#     reservasClientes
# )

#Menú para anfitirones
class AnfitrionApp:
    def AppAnfitrion():
    beanfitrion = anfitrionBE()
    print("Inicializando la app de Airbnb Anfitriones")
    while True:
        Menu = """\nElija una de las siguientes opciones:
        0-Salir de la app
        1-Ingresar un nuevo alojamiento
        2-Actualizar alojamiento
        3-Eliminar alojamiento\n"""
        print("-"*100)
        print(Menu)
        print("-"*100)
        option = int(input("Opción: "))

            if option == 0:
                print("\nDeteniendo la aplicación de Airbnb Anfitriones")
            break
            if option == 1:
                beanfitrion.addAlojamiento()
            if option == 2:
                beanfitrion.updateAlojamiento()
            if option == 3:
                becliente.deleteAlojamiento()

    AppAnfitrion()
    #Desde el perfil de un cliente
#Se le presenta este menú

# def AppClientesRegular(cliente):
#     dbcliente = DBClientes()
#     becliente = clientesBE()
#     print("Inicializando la app de Airbnb Clientes")
#     while True:
#         Menu = """\nElija una de las siguientes opciones:
#         0-Salir de la app
#         1-Ver mi perfil
#         2-Actualizar mi perfil
#         3-Reservar
#         4-Registrarme para una experiencia\n"""
#         print("-"*100)
#         print(Menu)
#         print("-"*100)
#         option = int(input("Opción: "))

#         if option == 0:
#             print("\nDeteniendo la aplicación de Airbnb Clientes")
#             #connection.close()
#             break
#         if option == 1:
#             becliente.getClient(cliente)
#         if option == 2:
#             becliente.actualizarCliente(cliente)
#         if option == 3:
#             reservasClientes(cliente)
#         if option == 4:
#             pass

#AppClientes()
            