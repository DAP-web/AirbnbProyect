from Residencia_BE import residenciasBE
from DB_Residencia_BE import ResidenciaDB
from AgregarResidenciaFull import residenciaFull

def residenciasAppAdmin():
    residenciabe=residenciasBE()
    residenciadb = ResidenciaDB()
    print("Inicializando la app de Airbnb Residencia")
    while True:
        Menu = """\nElija una de las siguientes opciones:
        0-Salir de la app
        1-Recuperar todos las residencias
        2-Ingresar una nueva residencia
        3-Actualizar residencia
        4-Eliminar residencia\n"""
        print("-" * 100)
        print(Menu)
        print("-" * 100)
        option = int(input("Opción: "))

        if option == 0:
            print("\nDeteniendo la aplicación de Airbnb Residencia")
            #residenciadb.connection.close()
            break
        if option == 1:
            residenciabe.getAllResidencias()
        if option == 2:
            #residenciabe.addResidencia()
            residenciaFull()
        if option == 3:
            residenciabe.updateResidencia()
        if option == 4:
            residenciabe.deleteResidencia()
