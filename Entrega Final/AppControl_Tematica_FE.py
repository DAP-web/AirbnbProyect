from Logic_TematicaLogic import Logic
from View_Tematica import TematicaBE


def TematicaAppAdmin():
    dbtematica = TematicaLogic()
    beTematica = TematicaBE()

    print("Inicializando la app de Airbnb Residencia")
    while True:
        Menu = """\nElija una de las siguientes opciones:
        0-Salir de la app
        1-Mostrar todas las tematicas 
        2-Ingresar una nueva tematica
        3-Actualizar una tematica 
        4-Eliminar tematica\n"""
        print("-" * 100)
        print(Menu)
        print("-" * 100)
        option = int(input("Opción: "))

        if option == 0:
            print("\nDeteniendo la aplicación de Airbnb Experiencia")
            # experienciabd.connection.close()
            break
        if option == 1:
            beexperiencia.getAllTematicas()
        if option == 2:
            beexperiencia.addTematica()
        if option == 3:
            beexperiencia.updateTematica()
        if option == 4:
            beexperiencia.deleteTematica()

TematicaAppAdmin()
