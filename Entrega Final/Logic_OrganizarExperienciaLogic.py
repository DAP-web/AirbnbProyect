from Core_dx_logic import Logic
from Objects_ExperienciaResidenciaObj import ExperienciaResidenciaObj
from Objects_ExperienciasObj import ExperienciaObj

class OrganizarExperienciaLogic(Logic):
        def __init__(self):
            super().__init__("experiencia")
        self.idName = "idExp"
        self.vistaName = "organizarexperiencias"

        def getOrganizarExperiencia(self):
            experienciaList = super().getAllRows(self.tableName)
            experienciaObjList = []
            for experiencia in experienciaList:
                newExperiencia = self.creatExperienciaObj(experiencia)
                experienciaObjList.append(newExperiencia)
            return experienciaObjList

        def OrganizarExperienciaObj(self, OexperienciaDic):
            OexperienciaObj = OrganizarExperienciaObj(
            OexperienciaDic["NombreAnfitrion"],
            OexperienciaDic["TituloExperiencia"],
            OexperienciaDic["TipoDeExperiencia"],
            OexperienciaDic["Ubicacion"],
            OexperienciaDic["Descripcion"],
            OexperienciaDic["Idioma"],
            OexperienciaDic["PublicoObjetivo"],
            OexperienciaDic["Organizacion"],
            OexperienciaDic["AnfitrionExp"],
            OexperienciaDic["ElementosANecesitar"],
            OexperienciaDic["PrecioIndividual"],
            OexperienciaDic["Fecha"],
            OexperienciaDic["IdTematica"],
            OexperienciaDic["idExp"]
            )
            return OexperienciaObj

            def insertOrganizarExperiencia(self, host, ExperienceTitle, TypeExperience, Location, 
                Descrption, Idiom, PublicObject, Organization, hostExperience, NeedElements, 
                precio, fecha, idTematic):
                    database = self.database
                    sql = f"""INSERT INTO airbnb.experiencia
                    (NombreAnfitrion,
                    TituloExperiencia,
                    TipoDeExperiencia,
                    Ubicacion,
                    Descripcion,
                    Idioma,
                    PublicoObjetivo,
                    Organizacion,
                    AnfitrionExp,
                    ElementosANecesitar,
                    PrecioIndividual,
                    Fecha,
                    IdTematica)
                    VALUES 
                    ('{host}',
                    '{ExperienceTitle}',
                    {TypeExperience},
                    '{Location}',
                    '{Descrption}',
                    '{Idiom}',
                    '{PublicObject}',
                    '{Organization}',
                    '{hostExperience}',
                    '{NeedElements}',
                    {precio},
                    '{fecha}',
                    {idTematic});"""
                    rows = database.executeNonQueryRows(sql)
                    return rows
            def updateOrganizarExperienciaBD(self, id, host, ExperienceTitle, TypeExperience, Location,
            Descrption, Idiom, PublicObject, Organization, hostExperience, NeedElements,
            precio, fecha, idTematic):
                database = self.database
                sql = f"""UPDATE airbnb.experiencia SET
                NombreAnfitrion = '{host}', TituloExperiencia = '{ExperienceTitle}',
                TipoDeExperiencia = {TypeExperience}, Ubicacion = '{Location}',
                Descripcion = '{Descrption}', Idioma = '{Idiom}',
                PublicoObjetivo = '{PublicObject}', Organizacion = '{Organization}',
                AnfitrionExp = '{hostExperience}', ElementosANecesitar = '{NeedElements}',
                PrecioIndividual = {precio}, Fecha = '{fecha}', IdTematica ={idTematic}
                WHERE idExp = {id};"""
                rows = database.executeNonQueryRows(sql)
                return rows
            def traerIDOrganizarExperiencia(self, host, ExperienceTitle, TypeExperience, Location,
            Descrption, Idiom, PublicObject, Organization, hostExperience, NeedElements,
            precio, fecha, idTematic):
                database = self.database
                sql = f"""SELECT idExp
                FROM experiencia
                WHERE NombreAnfitrion = '{host}' AND TituloExperiencia = '{ExperienceTitle}' AND
                TipoDeExperiencia = {TypeExperience} AND Ubicacion = '{Location}' AND
                Descripcion = '{Descrption}' AND Idioma = '{Idiom}' AND
                PublicoObjetivo = '{PublicObject}' AND Organizacion = '{Organization}' AND
                AnfitrionExp = '{hostExperience}' AND ElementosANecesitar = '{NeedElements}' AND
                PrecioIndividual = {precio} AND Fecha = '{fecha}' AND IdTematica ={idTematic};"""
                id = database.executeQueryOneRow(sql)
                return id["idExp"]

            def deleteOrganizarExperienciaDB(self, idExp):
                super().deleteRowById(self.idName, idExp, self.tableName)

            def printOrganizarEXperencia():
                database = self.database
                sql = f"""
                SELECT Idioma
                FROM `airbnb`.`experiencia`; """
