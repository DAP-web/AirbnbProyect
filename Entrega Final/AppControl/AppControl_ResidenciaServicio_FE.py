from Views.View_ResidenciaServicio import resiservBE


def residenciaservicioAppAdmin():
    resiservbe = resiservBE()
    print("Inicializando la app de Airbnb RS")
    while True:
        Menu = """\nElija una de las siguientes opciones:
        0-Salir de la app
        1-Recuperar todos las RS
        2-Ingresar una nueva RS
        3-Actualizar RS
        4-Eliminar RS\n"""
        print("-" * 100)
        print(Menu)
        print("-" * 100)
        option = int(input("Opción: "))

        if option == 0:
            print("\nDeteniendo la aplicación de Airbnb RS")
            break
        if option == 1:
            resiservbe.getAllResidenciaServicio()
        if option == 2:
            resiservbe.addResidenciaServicio()
        if option == 3:
            resiservbe.updateResidenciaServicio()
        if option == 4:
            resiservbe.deleteResidenciaServicio()


# residenciaservicioAppAdmin()