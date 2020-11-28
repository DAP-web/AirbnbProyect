from Calificaciones_BE import calificionesBE
from DB_Calificaciones_BE import calificacionesDB


calificacionbe = calificionesBE()
calificaciondb = calificacionesDB()
#Menú para administradores
def AppCalificaciones():
    print("Inicializando la app de Airbnb Calificaciones...")
    while True:
        Menu = """\nElija una de las siguientes opciones:
        0-Salir de la app
        1-Recuperar todas las calificaciones
        2-Ingresar una nueva calificación\n"""
        print("-"*100)
        print(Menu)
        print("-"*100)
        option = int(input("Opción: "))

        if option == 0:
            print("\nDeteniendo la aplicación de Airbnb Clientes")
            #calificaciondb.connection.close()
            break
        if option == 1:
            calificacionbe.getCalificaciones()
        if option == 2:
            calificacionbe.calificar()
        if option == 3:
            pass
        if option == 4:
            pass
#AppCalificaciones()