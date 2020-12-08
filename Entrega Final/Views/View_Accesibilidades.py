from prettytable import PrettyTable
from Logic_AccesibilidadLogic import AccesibilidadLogic
# from DB_Residencia_BE import ResidenciaDB

class accesibilidadesBE:
    def __init__(self):
        self.dbaccesibilidades=AccesibilidadLogic()
        
    def getAllAccesibilidades(self):
        result = self.dbaccesibilidades.getAccesibilidades()

        table = PrettyTable()
        table.field_names = ["IdAccesibilidades","NombreAccesibilidad","DescripcionAccesibilidad"]

        for accesibilidad in result:
            table.add_row([
                accesibilidad.idAccesibilidades,
                accesibilidad.strNombre,
                accesibilidad.strDescripcion,
                ])

        print(table)
        table.clear()

    def agregarAccesibilidadV(self):
        print("\nAdding a new accesibilidad...")
        strNombre = input("\nNombre: ")
        strDescripcion = input("\nDescripcion: ")
        
        self.dbaccesibilidades.agregarAccesibilidad(strNombre, strDescripcion)
        idaccesibilidades=self.dbaccesibilidades.traerIDAccesibilidad(strNombre,strDescripcion)

        print(f"\nSu accesibilidad se ha agendado con éxito. Su número de accesibilidad es {idaccesibilidades}\n")
        self.getAllAccesibilidades()

    def modificarAccesibilidad(self):
        print("\nUpdating a booking...")
        id = int(input("\nID de la accesibilidad a modificar: "))

        accesibilidad = self.dbaccesibilidades.buscarAccesibilidadU(id)

        update = int(input("¿Actualizar Nombre de la Accesibilidad? 0-No - 1-Sí "))
        if update == 1:
            print(f"Nombre: {accesibilidad.strNombre}")
            strNombre = input("Nombre: ")
        else:
            strNombre = accesibilidad.strNombre

        update = int(input("¿Actualizar descripcion de la accesibilidad? 0-No - 1-Sí "))
        if update == 1:
            print(f"Descripcion de Accesibilidad Vieja: {accesibilidad.strDescripcion}")
            strDescripcion = input("Nueva Descripcion de accesibilidad: ")
        else:
            strDescripcion = accesibilidad.strDescripcion

        self.dbaccesibilidades.actualizarAccesibilidad(id,strNombre, strDescripcion)
        print("\nLos cambios se han efectuado con éxito.")

    def eliminarAccesibilidad(self):
        print("Cancelando accesibilidad...")
        id = int(input("ID de accesibilidad único: "))

        self.dbaccesibilidades.cancelarAccesibilidad(id)