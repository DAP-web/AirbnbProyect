from View_Accesibilidades import accesibilidadesBE
from Core_databaseX import DatabaseX


def AppAccesibilidades():
    dbaccesibilidad = DatabaseX()
    beaccesibilidad = accesibilidadesBE()
    print("Inicializando la app de Airbnb Reservas")
    while True:
        Menu = """\nElija una de las siguientes opciones:
        0-Salir de la app
        1- Recuperar todas las accesibilidades
        2- Agregar una accesibilidad
        3- Actualizar accesibilidad
        4- Eliminar accesibilidad\n"""
        print("-"*100)
        print(Menu)
        print("-"*100)
        option = int(input("Opción: "))

        if option == 0:
            print("\nDeteniendo la aplicación de Airbnb Accesibilidades")
            # dbaccesibilidad.connection.close()
            break
        if option == 1:
            beaccesibilidad.getAllAccesibilidades()
        if option == 2:
            beaccesibilidad.agregarAccesibilidadV()
        if option == 3:
            beaccesibilidad.modificarAccesibilidad()
        if option == 4:
            beaccesibilidad.eliminarAccesibilidad()

AppAccesibilidades()