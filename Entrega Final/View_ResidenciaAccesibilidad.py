from prettytable import PrettyTable
from Logic_ResidenciaAccesibilidadLogic import RAccesibilidadLogic
# from DB_Residencia_BE import ResidenciaDB

class accesibilidadesBE:
    def __init__(self):
        self.dbraccesibilidades=RAccesibilidadLogic()
        

    def getAllAccesibilidades(self,):
        result = self.dbraccesibilidad.getRAccesibilidades()

        table = PrettyTable()
        table.field_names = ["IdRA","idAccesibilidad","idResidencia"]

        for raccesibilidad in result:
            table.add_row([
                raccesibilidad.idra,
                raccesibilidad.idaccesibilidad,
                raccesibilidad.idresidencia,
                ])

        print(table)
        table.clear()

    def agregarRAccesibilidadV(self):
        print("\nAdding a new residencia accesibilidad...")
        idAccesibilidad = int(input("\nAccesibilidad: "))
        idResidencia = int(input("\nResidencia: "))
        
        self.dbraccesibilidades.agregarRAccesibilidad(idAccesibilidad, idResidencia)
        idraccesibilidades=self.dbraccesibilidad.traerIDRAccesibilidad(idAccesibilidad, idResidencia)

        print(f"\nSu accesibilidad de residencia se ha agregado con éxito. Su número de reservación es {idaccesibilidades}\n")
        self.getAllRAccesibilidades()

    def modificarRAccesibilidad(self):
        print("\nUpdating a booking...")
        id = int(input("\nID de la accesibilidad de residencia a modificar: "))

        raccesibilidad = self.dbraccesibilidades.buscarRAccesibilidadV(id)

        update = int(input("¿Actualizar Accesibilidad de Residencia? 0-No - 1-Sí "))
        if update == 1:
            print(f"Accesibilidad: {raccesibilidad.idAccesibilidad}")
            idAccesibilidad = input("Accesibilidad: ")
            
        else:
            idAccesibilidad = raccesibilidad.idAccesibilidad

        update = int(input("¿Actualizar Residencia de la accesibilidad? 0-No - 1-Sí "))
        if update == 1:
            print(f"Residencia Vieja: {raccesibilidad.idResidencia}")
            idResidencia = input("Nueva Residencia: ")
            
        else:
            idResidencia = raccesibilidad.idResidencia

    
 
        self.dbraccesibilidades.actualizarRAccesibilidad(id,idAccesibilidad,idResidencia)
        print("\nLos cambios se han efectuado con éxito.")
        

    def cancelacionDeAccesibilidad(self):
        print("Cancelando accesibilidad de residencia...")
        id = int(input("ID de accesibilidad único: "))

        raccesibilidad = self.dbraccesibilidades.chequeoCancelacion(id)
       

        self.dbraccesibilidades.cancelarRAccesibilidad(id)