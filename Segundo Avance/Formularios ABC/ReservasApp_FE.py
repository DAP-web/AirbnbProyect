from Reservaciones_BE import (
    connection,
    getAllReservas,
    agendarReservaV,
    modificarReserva
)

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
        connection.close()
        break
    if option == 1:
        getAllReservas()
    if option == 2:
        agendarReservaV()
    if option == 3:
        modificarReserva()
    if option == 4:
        pass