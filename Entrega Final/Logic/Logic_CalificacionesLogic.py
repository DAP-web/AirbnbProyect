from Core.Core_dx_logic import Logic
from Objects.Objects_CalificacionesObj import CalificacionesObj
from Objects.Objects_CalificacionesViewObj import CalificacionesViewObj

class CalificacionesLogic(Logic):
    def __init__(self):
        super().__init__("calificaciones")
        self.idName = "idCalificacion"

    def obtenerCalificaciones(self):
        database=self.database
        sql = """SELECT IdResidencia,round(avg(Calificacion),2) as Promedio
        FROM calificaciones
        GROUP BY IdResidencia;"""
        calificacionesList=database.executeQueryRows(sql)
        calificacionesObjList=[]
        for calificacion in calificacionesList:
            newCalificacion = self.createCalificacionViewObj(calificacion)
            calificacionesObjList.append(newCalificacion)
        return calificacionesObjList
        
    def createCalificacionObj(self,calificacionDict):
        calificacionObj=CalificacionesObj(
            calificacionDict["Calificacion"],
            calificacionDict["IdResidencia"],
            calificacionDict["idCalificacion"]
        )
        return calificacionObj
    
    def createCalificacionViewObj(self,calificacionViewDict):
        calificacionViewObj=CalificacionesViewObj(
            calificacionViewDict["IdResidencia"],
            calificacionViewDict["Promedio"]
        )
        return calificacionViewObj

    def agregarCalificacion(self,calificacion,residencia):
        database=self.database
        sql = f"""INSERT INTO airbnb.calificaciones
        (Calificacion,
        IdResidencia)
        VALUES
        ({calificacion},
        {residencia});"""
        rows = database.executeNonQueryRows(sql)
        return rows