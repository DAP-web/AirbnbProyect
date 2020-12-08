from Core.Core_dx_logic import Logic
from Objects.Objects_ExperienciasObj import ExperienciaObj
from Objects.Objects_ExperienciaViewObj import ExperienciaViewObj

class ExperienciaLogic(Logic):
    def __init__(self):
        super().__init__("experiencia")
        self.idName = "idExp"
        self.vistaName = "experiencias"

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
            experienciaDic["PrecioIndividual"],
            experienciaDic["Fecha"],
            experienciaDic["IdTematica"],
            experienciaDic["idExp"]
        )
        return experienciaObj

    def creatExperienciaViewObj(self, experienciaDic):
        experienciaViewObj = ExperienciaViewObj(
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
            experienciaDic["Precio"],
            experienciaDic["Fecha"],
            experienciaDic["NombreTematica"],
            experienciaDic["idExp"]
        )
        return experienciaViewObj

    def insertExperiencia(self, host, ExperienceTitle, TypeExperience, Location, 
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

    def searchExperienciaById(self, id):
        rowDic = super().getRowById(self.idName, id, self.tableName)
        newUser = self.creatExperienciaObj(rowDic)
        return newUser

    def searchExperienciaByIdView(self, id):
        rowDic = super().getRowById(self.idName, id, self.vistaName)
        newUser = self.creatExperienciaViewObj(rowDic)
        return newUser

    def updateExperienciaBD(self, id, host, ExperienceTitle, TypeExperience, Location,
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

    def traerIDExperiencia(self, host, ExperienceTitle, TypeExperience, Location,
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

    def deleteExperienciaDB(self, idExp):
        super().deleteRowById(self.idName, idExp, self.tableName)

    def buscarExperienciasEnLinea(self):
        database = self.database
        sql = "SELECT * FROM airbnb.experiencias where TipoDeExperiencia=0;"
        experienciaList = database.executeQueryRows(sql)
        experienciaObjList = []
        for experiencia in experienciaList:
            newExperiencia = self.creatExperienciaViewObj(experiencia)
            experienciaObjList.append(newExperiencia)
        return experienciaObjList

    def buscarExperienciasPresenciales(self):
        database = self.database
        sql = "SELECT * FROM airbnb.experiencias where TipoDeExperiencia=1;"
        experienciaList = database.executeQueryRows(sql)
        experienciaObjList = []
        for experiencia in experienciaList:
            newExperiencia = self.creatExperienciaViewObj(experiencia)
            experienciaObjList.append(newExperiencia)
        return experienciaObjList