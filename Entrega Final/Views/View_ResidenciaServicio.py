from prettytable import PrettyTable
from Logic_ResidenciasServicioLogic import ResidenciaServicioLogic


class resiservBE:
    def __init__(self):
        self.dbresiserv = ResidenciaServicioLogic()

    def getAllResidenciaServicio(self):
        result = self.dbresidenciaservicio.getResidenciaServicio()

        table = PrettyTable()
        table.field_names = [
            "idRS",
            "IdServicio",
            "IdResidencia"
        ]

        for residenciaservicio in result:
            table.add_row(
                [
                    residenciaservicio.id,
                    residenciaservicio.idServicio,
                    residencia.idResidencia,
                ]
            )

        print(table)
        table.clear()

    def addResidenciaServicio(self):
        print("\nAñadiendo una nueva RS...")
        idServicio = input("\nID de Servicio: ")
        idResidencia = input("\nID de Residencia: ")

        self.dbresiserv.insertResidenciaServicio(
            idServicio,
            idResidencia,
        )
        idResidenciaServicio = self.dbresidenciaservicio.traerIDResidenciaServicio(
            idServicio,
            idResidencia,
        )

        print("\nLa RS se ha agregado con éxito.")
        print(f"El código de la RS es {idResidenciaServicio}. \n")
        self.getAllResidenciaServicio()

    def updateResidenciaServicio(self):
        print("\nActualizando la RS...")
        id = int(input("\nID de la RS a actualizar: "))

        resiserv = self.dbresidenciaservicio.searchResidenciaServicioById(id)

        update = int(input("¿Actualizar ID de servicio? 0-No - 1-Yes: "))
        if update == 1:
            print(f"ID de servicio antigüo: {residenciaservicio.IdServicio}")
            idServicio = input("Nuevo ID de servicio: ")
        else:
            idServicio = residenciaservicio.idServicio

        update = int(input("¿Actualizar ID de residencia? 0-No - 1-Yes: "))
        if update == 1:
            print(f"Antigüo habitacion: {residenciaservicio.IdResidencia}")
            idResidencia = input("Nueva habitación: ")
        else:
            idResidencia = residenciaservicio.idResidencia


        self.dbresidenciaservicio.updateResidenciaServicioBD(
            id,
            idServicio,
            idResidencia
        )
        print("\nLos cambios se han efectuado con éxito.")
        self.getAllResidenciaServicio()

    def deleteResidenciaServicio(self):
        print("Borrando RS...")
        id = int(input("ID de RS a eliminar: "))

        self.dbresidenciaservicio.deleteResidenciaServicioDB(id)
        print("La RS se ha removido con éxito.")
        self.getAllResidenciaServicio()
