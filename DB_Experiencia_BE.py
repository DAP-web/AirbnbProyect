import pymysql


class ExperienciaDB:
    def __init__(self):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            passwd="12345",
            db="airbnb",
            cursorclass=pymysql.cursors.DictCursor,
        )

    def getExperiencia(self):
        result = {}
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM airbnb.experiencia"
                cursor.execute(sql)
                result = cursor.fetchall()
        finally:
            pass
        return result

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
        try:
            with self.connection.cursor() as cursor:
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
                cursor.execute(sql)
                self.connection.commit()
        finally:
            pass

    def updateExperienciaBD(
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
        try:
            with self.connection.cursor() as cursor:
                sql = f"""UPDATE airbnb.experiencia SET
                NombreAnfitrion = ´{host}´, TituloExperiencia = ´{ExperienceTitle}´,
                TipoDeExperiencia = ´{TypeExperience}´, Ubicacion = '{Location}',
                Descripcion = ´{Descrption}´, Idioma = ´{Idiom}´,
                PublicoObjetivo = ´{PublicObject}´, Organizacion = ´{Organization}´,
                AnfitrionExp = ´{hostExperience}´, ElementosANecesitar = ´{NeedElements}´,
                Estado = ´{State}´, IdTematica =,´{idTematic}´ 
                WHERE idExp = {id};"""
                cursor.execute(sql)
                self.connection.commit()
        finally:
            pass

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
        idexperencia = 0
        try:
            with self.connection.cursor() as cursor:
                sql = f"""SELECT idExp
                FROM experiencia
                WHERE NombreAnfitrion = '{host}' AND TituloExperiencia = '{ExperienceTitle}' AND
                TipoDeExperiencia = {TypeExperience} AND Ubicacion = '{Location}' AND
                Descripcion = '{Descrption}' AND Idioma = '{Idiom}' AND
                PublicoObjetivo = '{PublicObject}' AND Organizacion = '{Organization}' AND
                AnfitrionExp = '{hostExperience}' AND ElementosANecesitar = '{NeedElements}' AND
                Estado = {State} AND IdTematica ={idTematic};"""
                cursor.execute(sql)
                idexperencia = cursor.fetchone()
        finally:
            pass
        return idexperencia["idExp"]

    def deleteExperienciaDB(self, idExp):
        try:
            with self.connection.cursor() as cursor:
                sql = f"DELETE FROM airbnb.experiencia WHERE idExp={idExp};"
                cursor.execute(sql)
                self.connection.commit()
        finally:
            pass
