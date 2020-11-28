from prettytable import PrettyTable
from DB_ExperienciasResidencias_BE import ExperienciasResidencialesBD


class ExperienciaResidenciasBE:
    def __init__(self):
        self.experienciaResidenciabd = ExperienciasResidencialesBD()

    def getAllExperienciasResidencias(self):
        result = self.experienciaResidenciabd.getExperienciaResidencias()

        table = PrettyTable()
        table.field_names = [
            "idER",
            "IdExp",
            "IdResidencia",
        ]

        for ExperienciaResidencia in result:
            table.add_row(
                [
                    ExperienciaResidencia["idER"],
                    ExperienciaResidencia["IdExp"],
                    ExperienciaResidencia["IdResidencia"],
                ]
            )
        print(table)
        table.clear()

    def addExperienciaResidencia(self):
        print("\nAñadiendo una nueva experiencia de residencia...")
        IdExp = int(input("\nIngrese el ID de la experiencia: "))
        IdResidencia = int(input("\nIngrese el ID de la residencia: "))

        self.experienciaResidenciabd.insertExperienciaResidencias(
            IdExp,
            IdResidencia,
        )
        idExperienciaResidencia = (
            self.experienciaResidenciabd.traerIDExperienciaResidencia(
                IdExp,
                IdResidencia,
            )
        )

        print("\nLa residencia se ha agregado con éxito.")
        print(f"El código de la residencia es {idExperienciaResidencia}. \n")
        self.getAllResidencias()

    def updateExperienciaResidencia(self):
        print("\nActualizando la experiencia de residencia...")
        id = int(input("\nID de la experiencia de residencia a actualizar: "))

        experienciaResidencia = (
            self.experienciaResidenciabd.searchExperienciaResidenciasById(id)
        )

        update = int(input("¿Actualizar la experiencia? 0-No - 1-Yes: "))
        if update == 1:
            print(f"ID de experiencia antiguo: {experienciaResidencia['IdExp']}")
            IdExp = input("Nuevo Id de experiencia: ")
        else:
            IdExp = experienciaResidencia["IdExp"]

        update = int(input("¿Actualizar el ID de residencia? 0-No - 1-Yes: "))
        if update == 1:
            print(f"Antigüo Id Residencia: {experienciaResidencia['IdResidencia']}")
            IdResidencia = input("Nuevo Id Residencia: ")
        else:
            IdResidencia = experienciaResidencia["IdResidencia"]

        self.experienciaResidenciabd.updateExperienciaResidenciaBD(
            id, IdExp, IdResidencia
        )

        print("\nLos cambios se han efectuado con éxito.")
        self.getAllExperienciasResidencias()

    def deleteExperienciaResidencia(self):
        print("Borrando una experiencia de residencia...")
        id = int(input("ID de la experencia de residencia a eliminar: "))

        self.experienciaResidenciabd.deleteExperienciaResidenciaDB(id)
        print("La experiencia residencia se ha removido con éxito.")
        self.getAllExperienciasResidencias()
