from Core_dx_logic import Logic
from Objects_ExperienciasObj import ExperienciaObj


class ExperienciaLogic(Logic):
    def __init__(self):
        super().__init__("experiencia")
        self.idName = "idExp"

    def getExperiencia(self):
        experienciaList = super().getAllRows(self.tableName)
        experienciaObjList = []
        for experiencia in experienciaList:
            newExperiencia = self.creatExperienciaObj(experiencia)
            experienciaObjList.append(newExperiencia)
        return experienciaObjList

    def creatExperienciaObj(self, experienciaDic):
        experienciaObj = ExperienciaObj(
            experienciaDic["NombreAnfitrion"],
            experienciaDic["TituloExperiencia"],
            experienciaDic["TipoDeExperiencia"],
            experienciaDic["Ubicacion"],
            experienciaDic["Descripcion"],
            experienciaDic["Idioma"],
            experienciaDic["PublicoObjetivo"],
            experienciaDic["Organizacion"],
            experienciaDic["AnfitrionExp"],
            experienciaDic["ElementosANecesitar"],
            experienciaDic["Estado"],
            experienciaDic["IdTematica"],
            experienciaDic["idExp"],
        )
        return experienciaObj

    def insertExperiencia(
        self,
        host,
        ExperienceTitle,
        TypeExperience,
        Location,
        Descrption,
        Idiom,
        PublicObject,
        Organization,
        hostExperience,
        NeedElements,
        State,
        idTematic,
    ):
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
        Estado,
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
        {State},
        {idTematic});"""
        rows = database.executeNonQueryRows(sql)
        return rows

    def searchExperienciaById(self, id):
        rowDic = super().getRowById(self.idName, id, self.tableName)
        newUser = self.creatExperienciaObj(rowDic)
        return newUser

    def updateExperienciaBD(
        self,
        id,
        host,
        ExperienceTitle,
        TypeExperience,
        Location,
        Descrption,
        Idiom,
        PublicObject,
        Organization,
        hostExperience,
        NeedElements,
        State,
        idTematic,
    ):
        database = self.database
        sql = f"""UPDATE airbnb.experiencia SET
        NombreAnfitrion = '{host}', TituloExperiencia = '{ExperienceTitle}',
        TipoDeExperiencia = {TypeExperience}, Ubicacion = '{Location}',
        Descripcion = '{Descrption}', Idioma = '{Idiom}',
        PublicoObjetivo = '{PublicObject}', Organizacion = '{Organization}',
        AnfitrionExp = '{hostExperience}', ElementosANecesitar = '{NeedElements}',
        Estado = {State}, IdTematica ={idTematic}
        WHERE idExp = {id};"""
        rows = database.executeNonQueryRows(sql)
        return rows

    def traerIDExperiencia(
        self,
        host,
        ExperienceTitle,
        TypeExperience,
        Location,
        Descrption,
        Idiom,
        PublicObject,
        Organization,
        hostExperience,
        NeedElements,
        State,
        idTematic,
    ):
        database = self.database
        sql = f"""SELECT idExp
        FROM experiencia
        WHERE NombreAnfitrion = '{host}' AND TituloExperiencia = '{ExperienceTitle}' AND
        TipoDeExperiencia = {TypeExperience} AND Ubicacion = '{Location}' AND
        Descripcion = '{Descrption}' AND Idioma = '{Idiom}' AND
        PublicoObjetivo = '{PublicObject}' AND Organizacion = '{Organization}' AND
        AnfitrionExp = '{hostExperience}' AND ElementosANecesitar = '{NeedElements}' AND
        Estado = {State} AND IdTematica ={idTematic};"""
        id = database.executeQueryOneRow(sql)
        return id["idExp"]

    def deleteExperienciaDB(self, idExp):
        super().deleteRowById(self.idName, idExp, self.tableName)