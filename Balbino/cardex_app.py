from cardex_view import (
    connection,
    getAllClients,
    addNewClient,
    updateClient,
    deleteClient,
)

while True:
    print("cardex app...")
    print("menu: ")
    print("0 - exit: ")
    print("1 - get all clients: ")
    print("2 - add a new client: ")
    print("3 - update client: ")
    print("4 - delete client: ")
    option = int(input("option: "))

    if option == 0:
        print("exit cardex app...")
        connection.close()
        break
    if option == 1:
        getAllClients()
    if option == 2:
        addNewClient()
    if option == 3:
        updateClient()
    if option == 4:
        deleteClient()
