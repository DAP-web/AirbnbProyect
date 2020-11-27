from Desc_Accesibilidad_BE import desc_AccesibilidadBE
from DB_Desc_Accesibilidad_BE import Desc_AccesibilidadDB

def desc_accesibilidadAppAdmin():
    desc_accesibilidadbe=desc_AccesibilidadBE()
    desc_accesibilidaddb = Desc_AccesibilidadDB()
    print("Inicializando la app de Airbnb Residencia")
    while True:
        Menu = """\nElija una de las siguientes opciones:
        0-Salir de la app
        1-Recuperar todos las descripciones
        2-Ingresar una nueva descripción
        3-Actualizar una descripción
        4-Eliminar descripción\n"""
        print("-" * 100)
        print(Menu)
        print("-" * 100)
        option = int(input("Opción: "))

        if option == 0:
            print("\nDeteniendo la aplicación de Airbnb Residencia")
            desc_accesibilidaddb.connection.close()
            break
        if option == 1:
            desc_accesibilidadbe.getAllResidencias()
        if option == 2:
            desc_accesibilidadbe.addResidencia()
        if option == 3:
            desc_accesibilidadbe.updateResidencia()
        if option == 4:
            desc_accesibilidadbe.deleteResidencia()

desc_accesibilidadAppAdmin()