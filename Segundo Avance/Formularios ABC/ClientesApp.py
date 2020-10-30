from DB_ClientesView import (
    connection,
    getAllClients,
    addClient,
    updateClient,
    deleteClient
)

print("Inicializando la app de Airbnb Clientes")
while True:
    Menu = """\nElija una de las siguientes opciones:
    0-Salir de la app
    1- Recuperar todos los clientes
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