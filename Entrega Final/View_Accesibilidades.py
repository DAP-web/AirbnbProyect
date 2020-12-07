from prettytable import PrettyTable
from Logic_AccesibilidadLogic import AccesibilidadLogic
# from DB_Residencia_BE import ResidenciaDB

class accesibilidadesBE:
    def __init__(self):
        self.dbaccesibilidades=AccesibilidadLogic()
        

    def getAllAccesibilidades(self,):
        result = self.dbaccesibilidad.getAccesibilidades()

        table = PrettyTable()
        table.field_names = ["IdAccesibilidades","NombreAccesibilidad","DescripcionAccesibilidad"]

        for accesibilidad in result:
            table.add_row([
                accesibilidad.idaccesibilidades,
                accesibilidad.nombre,
                accesibilidad.descripcion,
                ])

        print(table)
        table.clear()

    def agregarAccesibilidadV(self):
        print("\nAdding a new accesibilidad...")
        strNombre = int(input("\nNombre: "))
        strDescripcion = int(input("\nDescripcion: "))
        
        self.dbaccesibilidades.agregarAccesibilidad(strNombre, strDescripcion)
        idaccesibilidades=self.dbaccesibilidad.traerIDAccesibilidad(strNombre,strDescripcion)

        print(f"\nSu accesibilidad se ha agendado con éxito. Su número de reservación es {idaccesibilidades}\n")
        self.getAllAccesibilidades()

    def modificarAccesibilidad(self):
        print("\nUpdating a booking...")
        id = int(input("\nID de la accesibilidad a modificar: "))

        accesibilidad = self.dbaccesibilidades.buscarAccesibilidadU(id)

        update = int(input("¿Actualizar Nombre de la Accesibilidad? 0-No - 1-Sí "))
        if update == 1:
            print(f"Nombre: {accesibilidad.Nombre}")
            strNombre = input("Nombre: ")
            
        else:
            strNombre = accesibilidad.strNombre

        update = int(input("¿Actualizar descripcion de la accesibilidad? 0-No - 1-Sí "))
        if update == 1:
            print(f"Descripcion de Accesibilidad Vieja: {accesibilidad.strNombre}")
            strDescripcion = input("Nueva Descripcion de accesibilidad: ")
            
        else:
            strDescripcion = accesibilidad.strDescripcion

    

        self.dbaccesibilidades.actualizarAccesibilidad(id,strNombre, strDescripcion)
        print("\nLos cambios se han efectuado con éxito.")
      

    def cancelacionDeAccesibilidad(self):
        print("Cancelando accesibilidad...")
        id = int(input("ID de accesibilidad único: "))

        accesibilidad = self.dbaccesibilidades.chequeoCancelacion(id)
       

        self.dbaccesibilidades.cancelarAccesibilidad(id)