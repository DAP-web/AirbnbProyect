import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    passwd="12345",
    db="airbnb",
    cursorclass=pymysql.cursors.DictCursor,
)

def getReservas():
    result = {}
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM airbnb.reservas;"
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        pass
    return result

def agendarReserva(idcliente,idresidencia,strFechaLlegada,strFechaRetirada,
                    intAdultos,intNinhos,intBebes,intTipoPago):
    try:
        with connection.cursor() as cursor:
            sql = f"""INSERT INTO `airbnb`.`reservaciones`
            (`IdCliente`,
            `IdResidencia`,
            `FechaLlegada`,
            `FechaRetirada`,
            `Adultos`,
            `Ninhos`,
            `Bebes`,
            `TipoPago`)
            VALUES
            ({idcliente},
            {idresidencia},
            '{strFechaLlegada}',
            '{strFechaRetirada}',
            {intAdultos},
            {intNinhos},
            {intBebes},
            {intTipoPago});"""
            cursor.execute(sql)
            connection.commit()
    finally:
        pass

#Metodo para buscar una reserva para actualizarla
def buscarReservaU(idReserva):
    reserva = {}
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT * FROM airbnb.reservaciones WHERE IdReserva={idReserva};"
            cursor.execute(sql)
            reserva = cursor.fetchone()
    finally:
        pass
    return reserva

def actualizarReserva(id,strFechaLlegada,strFechaRetirada,
                    intAdultos,intNinhos,intBebes,intTipoPago):
    try:
        with connection.cursor() as cursor:
            sql = f"""UPDATE `airbnb`.`reservaciones`
            SET
            FechaLlegada = '{strFechaLlegada}',
            FechaRetirada = '{strFechaRetirada}',
            Adultos = {intAdultos},
            Ninhos = {intNinhos},
            Bebes = {intBebes},
            TipoPago = {intTipoPago}
            WHERE IdReserva = {id};
            """
            cursor.execute(sql)
            connection.commit()
    finally:
        pass

#Metodo para buscar una reserva visible
def buscarReservaV(idReserva):
    reserva = {}
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT * FROM airbnb.reservas WHERE IdReserva={idReserva};"
            cursor.execute(sql)
            reserva = cursor.fetchone()
    finally:
        pass
    return reserva

def traerIDReserva(idcliente,idresidencia,strFechaLlegada,strFechaRetirada,
                    intAdultos,intNinhos,intBebes,intTipoPago):
    idreserva = 0
    try:
        with connection.cursor() as cursor:
            sql = f"""SELECT IdReserva
            FROM reservaciones
            WHERE IdCliente={idcliente} AND IdResidencia={idresidencia} AND FechaLlegada='{strFechaLlegada}' 
            AND FechaRetirada='{strFechaRetirada}' AND Adultos={intAdultos} AND Ninhos={intNinhos} 
            AND Bebes={intBebes} AND TipoPago={intTipoPago};
            """
            cursor.execute(sql)
            idreserva = cursor.fetchone()
    finally:
        pass
    return idreserva["IdReserva"]

def cancelarReserva(idReserva):
    try:
        with connection.cursor() as cursor:
            sql = f"DELETE FROM `airbnb`.`reservaciones` WHERE IdReserva={idReserva};"
            cursor.execute(sql)
            connection.commit()
    finally:
        pass
    
def chequeoCancelacion(idReserva):
    reserva = {}
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT IdResidencia FROM airbnb.reservas WHERE IdReserva={idReserva};"
            cursor.execute(sql)
            reserva = cursor.fetchone()
    finally:
        pass
    return reserva