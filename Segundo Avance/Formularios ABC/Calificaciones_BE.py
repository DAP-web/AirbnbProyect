from prettytable import PrettyTable
from DB_Calificaciones_BE import (
    connection,
    obtenerCalificaciones,
    agregarCalificacion
)

def getCalificaciones():
    result = obtenerCalificaciones()

    table = PrettyTable()
    table.field_names = ["Residencia","Calificación Promedio"]

    for residencia in result:
        table.add_row([
            residencia["IdResidencia"],
            residencia["Promedio"]
            ])

    print(table)
    table.clear()

def calificar():
    print("\nAgregando una calificación...")
    calificacion = int(input("\nCalificación (Valor entre 0-Peor | 5-Mejor): "))

    while calificacion>5 or calificacion<0:
        print("La calificación es incorrecta. Favor ingresar un valor entre 0 y 5.")
        print("Siendo 5 el mejor y 0 lo peor.")
        calificacion = int(input("\nCalificación: "))

    residencia = input("\nResidencia ID: ")

    agregarCalificacion(calificacion,residencia)

    print("\nSu calificación se ha guardado con éxito.\n")
