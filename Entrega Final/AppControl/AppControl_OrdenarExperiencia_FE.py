from View_OrdenarExperiencia import organizarExperienciaBE

def AppOrganizarExperiencia():
    ordenarexperiencia = organizarExperienciaBE()
    print("Inicializando la app de Airbnb Organizar experiencia...")
    while True:
        Menu = """\nElija una de las siguientes opciones:
        0-Salir de la app
        1-Organizar una nueva experiencia
        2-Actualizar experiencia
        3-Eliminar experiencia\n"""
        print("-"*100)
        print(Menu)
        print("-"*100)
        option = int(input("Opción: "))

        if option == 0:
            print("\nDeteniendo la aplicación de Airbnb Organizar Experiencia")
            break
        if option == 1:
            ordenarexperiencia.addOrganizarExperiencia()
        if option == 2:
            ordenarexperiencia.updateOrdenarExperiencia()
        if option == 3:
            ordenarexperiencia.deleteOrganizarExperiencia()

# AppOrganizarExperiencia()
   
   
   
    
