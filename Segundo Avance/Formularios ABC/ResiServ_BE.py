from prettytable import PrettyTable
from DB_ResiServ_BE import ResiServDB

class residenciaservicioBE:
    def __init__(self):
        self.resiservbd=ResiServDB()

    def getAllResidenciaServicio(self):
        result = self.resiservbd.getResidencias()

        table = PrettyTable()
        table.field_names = [
            "idRS"
            "idResidencia",
            "idServicio
        ]

        for residenciaservicio in result:
            table.add_row(
                [
                    residenciaservicio["idRS"],
                    residenciaservicio["idResidencia"],
                    residenciaservicio["idServicio"],
                ]
            )
        print(table)
        table.clear()


    def addResiServ(self):
        print("\nAñadiendo un nuevo residenciaservicio...")
        idResidencia = input("\nID de la Residencia: ")
        idServicio = input("\nID del servicio: ")

        self.resiservbd.insertResiServs(
            idResidencia,
            idServicio,
        )
        idRS = self.residenciaserviciobd.traerIDResiServ(
            idResidencia,
            idServicio,
        )

        print("\nLa residenciaservicio se ha agregado con éxito.")
        print(f"El código de la residencia es {idRS}. \n")
        self.getAllResidenciaServicio()


    def updateResiServ(self):
        print("\nActualizando la RS...")
        id = int(input("\nID de la RS a actualizar: "))

        residenciaservicio = self.residenciaserviciobd.searchResiServById(id)

        update = int(input("¿Actualizar ID de Residencia? 0-No - 1-Yes: "))
        if update == 1:
            print(f"ID de Residencia antiguo: {residenciaservicio['idResidencia']}")
            idResidencia = input("Nuevo ID de Residencia: ")
        else:
            idResidencia = residenciaservicio["idResidencia"]

        update = int(input("¿Actualizar ID de Servicio? 0-No - 1-Yes: "))
        if update == 1:
            print(f"Antigüo ID de Servicio: {residenciaservicio['idServicio']}")
            idServicio = input("Nuevo ID de Servicio: ")
        else:
            idServicio = residenciaservicio["idServicio"]

        self.residenciabd.updateResidenciaBD(
            id,
            idResidencia,
            idServicio,
        )
        print("\nLos cambios se han efectuado con éxito.")
        self.getAllResidenciaServicio()


    def deleteResidenciaServicio(self):
        print("Borrando RS...")
        id = int(input("ID de RS a eliminar: "))

        self.residenciabd.deleteResidenciaDB(id)
        print("La RS se ha removido con éxito.")
        self.getAllResidenciaServicio()
