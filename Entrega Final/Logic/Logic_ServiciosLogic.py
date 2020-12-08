from Core.Core_dx_logic import Logic
from Objects.Objects_ServiciosObj import ServiceObj

class ServiceLogic(Logic):
    def __init__(self):
        super().__init__("servicios")
        self.idName="idServicio"
    
    def getServices(self):
        serviceList= super().getAllRows(self.tableName)
        serviceObjList =[]
        for service in serviceList:
            newService = self.createServiceObj(service)
            serviceObjList.append(newService)
        return serviceObjList

    def createServiceObj(self,serviceDict):
        serviceObj = ServiceObj(
            serviceDict["NombreServicio"],
            serviceDict["idServicio"]
        )
        return serviceObj

    def insertService(self,name):
        database = self.database
        sql = f"""INSERT INTO airbnb.servicios
                (NombreServicio)
                VALUES
                ('{name}');"""
        rows = database.executeNonQueryRows(sql)
        return rows

    def searchServiceById(self,id):
        rowDict = super().getRowById(self.idName,id,self.tableName)
        newService = self.createServiceObj(rowDict)
        return newService

    def updateServiceBD(self,id,name):
        database = self.database
        sql = f"""UPDATE airbnb.servicios SET 
                NombreServicio = '{name}' 
                WHERE idServicio = {id};"""
        rows = database.executeNonQueryRows(sql)
        return rows

    def traerIDServicio(self,name):
        database = self.database
        sql = f"""SELECT idServicio
                FROM servicios
                WHERE NombreServicio = '{name}';"""
        id = database.executeQueryOneRow(sql)
        return id["idServicio"]
      
    def deleteServiceDB(self,id):
       super().deleteRowById(self.idName,id,self.tableName)

               
    
