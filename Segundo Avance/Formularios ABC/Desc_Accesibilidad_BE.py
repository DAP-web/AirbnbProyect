from prettytable import PrettyTable
from DB_Desc_Accesibilidad_BE import Desc_AccesibilidadDB

class desc_AccesibilidadBE:
    def __init__(self):
        self.desc_accesibilidadbd=Desc_AccesibilidadDB()

    def getAllDescription(self):
        result = self.desc_accesibilidadbd.getDescription()

        table = PrettyTable()
        table.field_names = [
            "idDA",
            "Descripcion",
            "IdAccesibilidad"
        ]

        for residencia in result:
            table.add_row(
                [
                    residencia["idDA"],
                    residencia["Descripcion"],
                    residencia["IdAccesibilidad"]
                ]
            )
        print(table)
        table.clear()


    def addDescription(self):
        print("\nAñadiendo una nueva descripcion...")
        Descripcion = input("\nDescripción: ")
        idAccesibilidad = input("\nid de accesibilidad: ")

        self.residenciabd.insertResidencias(
            Descripcion,
            idAccesibilidad
        )
        idDA = self.residenciabd.traerIDResidencia(
            Descripcion,
            idAccesibilidad
        )

        print("\nLa descripción se ha agregado con éxito.")
        print(f"El código de la descripción es {idDA}. \n")
        self.getAllDescription()


    def updateDescription(self):
        print("\nActualizando la descripción...")
        id = int(input("\nID de la descripción a actualizar: "))

        descripcion = self.desc_accesibilidadbd.searchDesc_AccesibilidadById(id)

        update = int(input("¿Actualizar descripción? 0-No - 1-Yes: "))
        if update == 1:
            print(f"Descripción: {descripcion['Descripcion']}")
            descripcion = input("Nueva descripción: ")
        else:
            descripcion = descripcion["Descripcion"]

        self.residenciabd.updateResidenciaBD(
            id,
            descripcion
        )
        print("\nLos cambios se han efectuado con éxito.")
        self.getAllDescription()


    def deleteDescription(self):
        print("Borrando descripciónn...")
        id = int(input("ID de descripciónn a eliminar: "))

        self.desc_accesibilidadbd.deleteDescriptionDB(id)
        print("La residencia se ha removido con éxito.")
        self.getAllDescription()