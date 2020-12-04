

class Logic:
    def __init__(self, tableName=None):
        self.database = None
        self.tableName = tableName
        self.__createDatabase()

    def __createDatabase(self):
        if self.database is None:
            self.database = DatabaseX()

    def getAllRows(self, tableName):
        database = self.database
        sql = f"SELECT * FROM `{database.database}`.`{tableName}`;"
        rowList = database.executeQueryRows(sql)
        return rowList

    def getRowById(self, idName,id, tableName):
        database = self.database
        sql = f"SELECT * FROM `{database.database}`.`{tableName}` WHERE {idName}={id};"
        rowDict = database.executeQueryOneRow(sql)
        return rowDict

    def deleteRowById(self, id, tableName):
        database = self.database
        sql = f"DELETE FROM `{database.database}`.`{tableName}` WHERE id = {id};"
        rows = database.executeNonQueryRows(sql)
        return rows
