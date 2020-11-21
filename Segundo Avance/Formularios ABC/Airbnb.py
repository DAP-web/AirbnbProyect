"""
Este va a ser el main de toda la aplicación AIRBNB
"""
from Login import (
    connection,
    signin
)

print("Inicializando la app de Airbnb...")
while True:
    Menu = """\nBienvenido a la plataforma de Airbnb
    Elija una de las siguientes opciones:
    0-Salir de la app
    1-Ingresar a mi cuenta
    2-Registrarse
    3-Actualizar cliente
    4-Eliminar cliente\n"""
    print("-"*100)
    print(Menu)
    print("-"*100)
    option = int(input("Opción: "))

    if option == 0:
        print("\nDeteniendo la aplicación de Airbnb...")
        connection.close()
        break
    if option == 1:
        signin()
    if option == 2:
        pass
    if option == 3:
        pass
    if option == 4:
        pass
        