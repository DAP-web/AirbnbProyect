from DB_Tematica_BE import DBTematica
from Tematica_BE import TematicaBE

def AppTematica():
    dbtematica = DBTematica()
    betematica = TematicaBE()
    print("Inicializando la app de Airbnb Tematica")
    while True:
        Menu = """\nElija una de las siguientes opciones:
        0-Salir de la app
        1-Recuperar todas las tematicas
        2-Ingresar una nueva tematica
        3-Actualizar tematica
        4-Eliminar tematica\n"""
        print("-"*100)
        print(Menu)
        print("-"*100)
        option = int(input("Opción: "))

        if option == 0:
            print("\nDeteniendo la aplicación de Airbnb Tematica")
            #dbtematica.connection.close()
            break
        if option == 1:
            betematica.getAllTematicas()
        if option == 2:
            betematica.addTematica()
        if option == 3:
            betematica.updateTematica()
        if option == 4:
            betematica.deleteTematica()
            