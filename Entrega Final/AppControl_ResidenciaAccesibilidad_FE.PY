from View_ResidenciaAccesibilidad import raccesibilidadesBE
from Logic_ResidenciaAccesibilidadLogic import RAccesibilidadLogic


def AppRAccesibilidades():
    dbraccesibilidad = RAccesibilidadLogic()
    beraccesibilidad = raccesibilidadesBE
    print("Inicializando la app de Airbnb Reservas")
    while True:
        Menu = """\nElija una de las siguientes opciones:
        0-Salir de la app
        1- Recuperar todas las accesibilidades de residencia
        2- Agendar una accesibilidad de residencia
        3- Actualizar accesibilidad de residencia
        4- Eliminar accesibilidad de residencia\n"""
        print("-"*100)
        print(Menu)
        print("-"*100)
        option = int(input("Opción: "))

        if option == 0:
            print("\nDeteniendo la aplicación de Airbnb Accesibilidades de Residencia")
            #reservas.dbreservas.database.endConnection()
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