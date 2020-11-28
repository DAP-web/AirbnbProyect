from Direcciones_BE import direccionesBE
from DB_Direcciones_BE import direccionesDB

def direccionesAdmin():
    direccionesbe=direccionesBE()
    direccionesdb=direccionesDB()
    print("Inicializando la app de Airbnb Direcciones")
    while True:
        Menu = """\nElija una de las siguientes opciones:
        0-Salir de la app
        1-Recuperar todas las Direcciones
        2-Ingresar una nueva Direccion
        3-Actualizar Direccion
        4-Eliminar Direccion\n"""
        print("-"*100)
        print(Menu)
        print("-"*100)
        option = int(input("Opción: "))

        if option == 0:
            print("\nDeteniendo la aplicación de Airbnb Direcciones")
            direccionesdb.connection.close()
            break
        if option == 1:
            direccionesbe.getAllDirections()
        if option == 2:
            direccionesbe.addDirection()
        if option == 3:
            direccionesbe.updateDirection()
        if option == 4:
            direccionesbe.deleteDirection()

direccionesAdmin()