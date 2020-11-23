from Clientes_BE import (
    connection,
    getAllClients,
    getClient,
    addClient,
    updateClient,
    actualizarCliente,
    deleteClient,
    clienteAgendaReserva
)
from ReservasApp_FE import(
    reservasClientes
)

#Menú para administradores
def AppClientes():
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
            connection.close()
            break
        if option == 1:
            getAllClients()
        if option == 2:
            addClient()
        if option == 3:
            updateClient()
        if option == 4:
            deleteClient()

#Desde el perfil de un cliente
#Se le presenta este menú
def AppClientesRegular(cliente):
    print("Inicializando la app de Airbnb Clientes")
    while True:
        Menu = """\nElija una de las siguientes opciones:
        0-Salir de la app
        1-Ver mi perfil
        2-Actualizar mi perfil
        3-Reservar
        4-Registrarme para una experiencia\n"""
        print("-"*100)
        print(Menu)
        print("-"*100)
        option = int(input("Opción: "))

        if option == 0:
            print("\nDeteniendo la aplicación de Airbnb Clientes")
            #connection.close()
            break
        if option == 1:
            getClient(cliente)
        if option == 2:
            actualizarCliente(cliente)
        if option == 3:
            reservasClientes(cliente)
        if option == 4:
            pass
#AppClientes()
            