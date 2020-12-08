from prettytable import PrettyTable
from Logic_ResidenciaAccesibilidadLogic import RAccesibilidadLogic

class raccesibilidadesBE:
    def __init__(self):
        self.dbraccesibilidades=RAccesibilidadLogic()
        
    def getAllRAccesibilidades(self):
        result = self.dbraccesibilidades.getRAccesibilidades()

        table = PrettyTable()
        table.field_names = ["Residencia","NombreAccesibilidad","Descripcion"]

        for raccesibilidad in result:
            table.add_row([
                raccesibilidad.idresidencia,
                raccesibilidad.nombre,
                raccesibilidad.descripcion
                ])

        print(table)
        table.clear()

    def agregarRAccesibilidadV(self):
        print("\nAdding a new residencia accesibilidad...")
        idAccesibilidad = int(input("\nAccesibilidad: "))
        idResidencia = int(input("\nResidencia: "))
        
        self.dbraccesibilidades.agregarRAccesibilidades(idAccesibilidad, idResidencia)
        idraccesibilidades=self.dbraccesibilidades.traerIDAccesibilidad(idAccesibilidad, idResidencia)

        print(f"\nSu accesibilidad de residencia se ha agregado con éxito. Su número de accesibilidad de residencia es {idraccesibilidades}\n")
        self.getAllRAccesibilidades()

    def modificarRAccesibilidad(self):
        print("\nActualizando una accesibilidad de residencia...")
        id = int(input("\nID de la accesibilidad de residencia a modificar: "))

        raccesibilidad = self.dbraccesibilidades.buscarRAccesibilidadU(id)

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
        
    def eliminarRAccesibilidad(self):
        print("Cancelando accesibilidad de residencia...")
        id = int(input("ID de accesibilidad único: "))
       
        self.dbraccesibilidades.cancelarRAccesibilidad(id)