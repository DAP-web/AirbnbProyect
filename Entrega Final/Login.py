from Core.Core_databaseX import DatabaseX
from Logic.Logic_ClientLogic import ClientLogic
from AppControl.AppControl_Clientes_FE import AppClientes,AppClientesRegular

dbcliente = ClientLogic()
database = DatabaseX()

def signin():
    correo = input("Correo de usuario: ")
    pswd = input("Contraseña de acceso: ")

    cliente = dbcliente.verificarUsuario(correo,pswd)

    if cliente is None:
        print("No se pudo iniciar sesión.")
        print("Chequee los campos y vuelva a intentar.")
    else:
        print(f"Bienvenido Señor/a {cliente.name}")
        AppClientesRegular(cliente)