from Reservaciones_BE import reservaciones
from Clientes_BE import clientesBE

clientebe = clientesBE()
reservas = reservaciones()

def reservasAdmin():
    print("Inicializando la app de Airbnb Reservas")
    while True:
        Menu = """\nElija una de las siguientes opciones:
        0-Salir de la app
        1- Recuperar todas las reservas
        2- Agendar una reserva
        3- Actualizar reserva
        4- Cancelar Reserva\n"""
        print("-"*100)
        print(Menu)
        print("-"*100)
        option = int(input("Opción: "))

        if option == 0:
            print("\nDeteniendo la aplicación de Airbnb Reservas")
            # reservas.connection.close()
            break
        if option == 1:
            reservas.getAllReservas()
        if option == 2:
            reservas.agendarReservaV()
        if option == 3:
            reservas.modificarReserva()
        if option == 4:
            reservas.cancelacionDeReserva()

def reservasClientes(cliente):
    print("Inicializando la app de Airbnb Reservas")
    while True:
        Menu = """\nElija una de las siguientes opciones:
        0-Salir de la app
        1- Ver mis reservas
        2- Agendar una reserva
        3- Actualizar reserva
        4- Cancelar Reserva\n"""
        print("-"*100)
        print(Menu)
        print("-"*100)
        option = int(input("Opción: "))

        if option == 0:
            print("\nDeteniendo la aplicación de Airbnb Reservas")
            break
        if option == 1:
            pass
        if option == 2:
            clientebe.clienteAgendaReserva(cliente)
        if option == 3:
            reservas.modificarReserva()
        if option == 4:
            #reservas.cancelacionDeReserva()
            pass
