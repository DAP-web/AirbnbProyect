from Views.View_Anfitrion import anfitrionBE

#Menú para anfitirones

def AppAnfitrion():
    beanfitrion = anfitrionBE()
    print("Inicializando la app de Airbnb Anfitriones")
    while True:
        Menu = """\nElija una de las siguientes opciones:
        0-Salir de la app
        1-Ingresar un nuevo alojamiento
        2-Actualizar alojamiento
        3-Eliminar alojamiento\n"""
        print("-"*100)
        print(Menu)
        print("-"*100)
        option = int(input("Opción: "))
        if option == 0:
            print("\nDeteniendo la aplicación de Airbnb Anfitriones")
            break
        if option == 1:
            beanfitrion.addAlojamiento()
        if option == 2:
            beanfitrion.updateAlojamiento()
        if option == 3:
            beanfitrion.deleteAlojamiento()
# AppAnfitrion()