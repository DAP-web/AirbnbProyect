from ExperienciaResidencia_BE import ExperienciaResidenciasBE
from DB_ExperienciasResidencias_BE import ExperienciasResidencialesBD


def ExperienciaresidenciasAppAdmin():
    experenciaresidenciabe = ExperienciaResidenciasBE()
    experienciaresidenciadb = ExperienciasResidencialesBD()
    print("Inicializando la app de Airbnb Experiencias de Residencia")
    while True:
        Menu = """\nElija una de las siguientes opciones:
        0-Salir de la app
        1-Recuperar todos las experiencias de residencias
        2-Ingresar una nueva experiencia de residencia
        3-Actualizar una experiencia de residencia
        4-Eliminarexperencia de residencia\n"""
        print("-" * 100)
        print(Menu)
        print("-" * 100)
        option = int(input("Opción: "))

        if option == 0:
            print("\nDeteniendo la aplicación de Airbnb Residencia")
            experienciaresidenciadb.connection.close()
            break
        if option == 1:
            experenciaresidenciabe.getAllExperienciasResidencias()
        if option == 2:
            experenciaresidenciabe.addExperienciaResidencia()
        if option == 3:
            experenciaresidenciabe.updateExperienciaResidencia()
        if option == 4:
            experenciaresidenciabe.deleteExperienciaResidencia()


ExperienciaresidenciasAppAdmin()