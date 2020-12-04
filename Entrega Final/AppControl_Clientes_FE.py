from Logic_ClientLogic import ClientLogic

from View_Clientes import clientesBE

# from ReservasApp_FE import(
#     reservasClientes
# )

#Menú para administradores
def AppClientes():
    dbcliente = ClientLogic()
    becliente = clientesBE()
    print("Inicializando la app de Airbnb Clientes")
    while True:
        Menu = """\nElija una de las siguientes opciones:
        0-Salir de la app
        1-Recuperar todos los clientes
        2-Ingresar un nuevo cliente
        3-Actualizar cliente
        4-Eliminar cliente\n"""
        print("-"*100)
        print(Menu)
        print("-"*100)
        option = int(input("Opción: "))

        if option == 0:
            print("\nDeteniendo la aplicación de Airbnb Clientes")
            # dbcliente.connection.close()
            break
        if option == 1:
            becliente.getAllClients()
        if option == 2:
            becliente.addClient()
        if option == 3:
            becliente.updateClient()
        if option == 4:
            becliente.deleteClient()

AppClientes()
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
            