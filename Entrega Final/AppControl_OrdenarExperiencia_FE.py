from Core_databaseX import DatabaseX
from View_Experiencias import experienciasBE
from View_ExperienciaResidencia import ExperienciaResidenciasBE

experienciabe = experienciasBE()
experienciaresidenciabe= ExperienciaResidenciasBE()
organizarExperienciadb = DatabaseX()


def AppOrganizarExperiencia():
    print("Inicializando la app de Airbnb Organizar experiencia...")
    while True:
        Menu = """\nElija una de las siguientes opciones:
        0-Salir de la app
        1-Organizar experiencia
        2-Volver al menú principal\n"""
        print("-"*100)
        print(Menu)
        print("-"*100)
        option = int(input("Opción: "))

        if option == 0:
            print("\nDeteniendo la aplicación de Airbnb Clientes")
            organizarExperienciadb.connection.close()
            break
        if option == 1:
            organizarExperienciadb.calificar()
        if option == 2:
            organizarExperienciadb.calificar()
      
AppOrganizarExperiencia()