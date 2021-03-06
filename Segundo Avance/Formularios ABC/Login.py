import pymysql
from DB_Clientes_BE import DBClientes
from ClientesApp_FE import(
    AppClientes,
    AppClientesRegular
)

dbcliente = DBClientes()

connection = pymysql.connect(
    host="localhost",
    user="root",
    passwd="12345",
    db="airbnb",
    cursorclass=pymysql.cursors.DictCursor,
)

def signin():
    correo = input("Correo de usuario: ")
    pswd = input("Contraseña de acceso: ")

    cliente = dbcliente.verificarUsuario(correo,pswd)

    if cliente is None:
        print("No se pudo iniciar sesión.")
        print("Chequee los campos y vuelva a intentar.")
    else:
        print(f"Bienvenido Señor/a {cliente['Nombre']}")
        AppClientesRegular(cliente)
    

