from Views.View_Experiencias import experienciasBE


def ExperienciasAppProceso():
    beexperiencia = experienciasBE()

    print("Inicializando la app de Airbnb Residencia")
    while True:
        Menu = """\nElija una de las siguientes opciones:
        0-Salir de la app
        1-Buscar experiencia en línea
        2-Buscar experiencia presencial\n"""
        print("-" * 100)
        print(Menu)
        print("-" * 100)
        option = int(input("Opción: "))

        if option == 0:
            print("\nDeteniendo la aplicación de Airbnb Experiencia")
            break
        if option == 1:
            beexperiencia.buscarExperienciasEnLinea()
        if option == 2:
            beexperiencia.buscarExperienciasPresenciales()

# ExperienciasAppAdmin()