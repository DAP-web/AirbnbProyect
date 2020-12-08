from prettytable import PrettyTable
from Logic.Logic_CalificacionesLogic import CalificacionesLogic

class calificionesBE:
    def __init__(self):
        self.calificiones=CalificacionesLogic()

    def getCalificaciones(self):
        result = self.calificiones.obtenerCalificaciones()

        table = PrettyTable()
        table.field_names = ["Residencia","Calificación Promedio"]

        for residencia in result:
            table.add_row([
                residencia.idresidencia,
                residencia.promedio
                ])

        print(table)
        table.clear()

    def calificar(self):
        print("\nAgregando una calificación...")
        calificacion = int(input("\nCalificación (Valor entre 0-Peor | 5-Mejor): "))

        while calificacion>5 or calificacion<0:
            print("La calificación es incorrecta. Favor ingresar un valor entre 0 y 5.")
            print("Siendo 5 el mejor y 0 lo peor.")
            calificacion = int(input("\nCalificación: "))

        residencia = input("\nResidencia ID: ")

        self.calificiones.agregarCalificacion(calificacion,residencia)

        print("\nSu calificación se ha guardado con éxito.\n")