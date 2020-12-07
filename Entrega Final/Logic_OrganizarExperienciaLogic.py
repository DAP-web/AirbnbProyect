from Core_dx_logic import Logic
from Objects_ExperienciaResidenciaObj import ExperienciaResidenciaObj
from Objects_ExperienciasObj import ExperienciaObj

class OrganizarExperienciaLogic(Logic):
    
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

    def deleteExperienciaDB(self, idExp):
        super().deleteRowById(self.idName, idExp, self.tableName)
