from Views.View_Experiencias import experienciasBE


def ExperienciasAppAdmin():
    beexperiencia = experienciasBE()

    print("Inicializando la app de Airbnb Residencia")
    while True:
        Menu = """\nElija una de las siguientes opciones:
        0-Salir de la app
        1-Recuperar todas las experiencias
        2-Ingresar una nueva experiencia
        3-Actualizar experiencia
        4-Eliminar experiencia\n"""
        print("-" * 100)
        print(Menu)
        print("-" * 100)
        option = int(input("Opción: "))

        if option == 0:
            print("\nDeteniendo la aplicación de Airbnb Experiencia")
            break
        if option == 1:
            beexperiencia.getAllExperiencias()
        if option == 2:
            beexperiencia.addExperiencia()
        if option == 3:
            beexperiencia.updateExperiencias()
        if option == 4:
            beexperiencia.deleteExperiencia()

# ExperienciasAppAdmin()
