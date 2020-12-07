from View_ResidenciaAccesibilidad import raccesibilidadesBE
from Core_databaseX import DatabaseX


def AppRAccesibilidades():
    dbraccesibilidad = DatabaseX()
    beraccesibilidad = raccesibilidadesBE()
    print("Inicializando la app de Airbnb Reservas")
    while True:
        Menu = """\nElija una de las siguientes opciones:
        0-Salir de la app
        1- Recuperar todas las accesibilidades de residencia
        2- Agregar una accesibilidad de residencia
        3- Actualizar accesibilidad de residencia
        4- Eliminar accesibilidad de residencia\n"""
        print("-"*100)
        print(Menu)
        print("-"*100)
        option = int(input("Opción: "))

        if option == 0:
            print("\nDeteniendo la aplicación de Airbnb Accesibilidades de Residencia")
            dbraccesibilidad.connection.close()
            break
        if option == 1:
            beraccesibilidad.getAllRAccesibilidades()
        if option == 2:
            beraccesibilidad.agregarRAccesibilidadV()
        if option == 3:
            beraccesibilidad.modificarRAccesibilidad()
        if option == 4:
            beraccesibilidad.cancelacionDeRAccesibilidad()

AppRAccesibilidades()