from Experiencia_BE import experienciasBE
from DB_Experiencia_BE import ExperienciaDB

def ExperienciasAppAdmin():
    experienciabe = experienciasBE()
    experienciabd = ExperienciaDB()
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
            #experienciabd.connection.close()
            break
        if option == 1:
            experienciabe.getAllExperiencias()
        if option == 2:
            experienciabe.addExperiencia()
        if option == 3:
            experienciabe.updateExperiencias()
        if option == 4:
            experienciabe.deleteExperiencia()


#ExperienciasAppAdmin()
