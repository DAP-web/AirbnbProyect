from View_Accesibilidades import accesibilidadesBE
from Logic_AccesibilidadLogic import AccesibilidadLogic


def AppAccesibilidades():
    dbaccesibilidad = AccesibilidadLogic()
    beaccesibilidad = accesibilidadesBE
    print("Inicializando la app de Airbnb Accesibilidad")
    while True:
        Menu = """\nElija una de las siguientes opciones:
        0-Salir de la app
        1- Recuperar todas las accesibilidades
        2- Agendar una accesibilidad
        3- Actualizar accesibilidad
        4- Eliminar accesibilidad\n"""
        print("-"*100)
        print(Menu)
        print("-"*100)
        option = int(input("Opción: "))

        if option == 0:
            print("\nDeteniendo la aplicación de Airbnb Accesibilidades")
            
            break
        if option == 1:
            beaccesibilidad.getAllAccesibilidades()
        if option == 2:
            beaccesibilidad.agregarAccesibilidadV()
        if option == 3:
            beaccesibilidad.modificarAccesibilidad()
        if option == 4:
            beaccesibilidad.cancelacionDeAccesibilidad()

AppAccesibilidades()