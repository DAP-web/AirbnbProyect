from Core_databaseX import DatabaseX
from View_Facturas import facturasBE

database = DatabaseX()
facturasbe = facturasBE()

def AppFacturas():
    print("Inicializando la app de Airbnb Facturas...")
    while True:
        Menu = """\nElija una de las siguientes opciones:
        0-Salir de la app
        1-Recuperar facturas Residencias
        2-Recuperar facturas Experiencias
        3-Registrar una nueva factura de reservaciones
        4-Registrar una nueva factura de experiencias\n"""
        print("-"*100)
        print(Menu)
        print("-"*100)
        option = int(input("Opción: "))

        if option == 0:
            print("\nDeteniendo la aplicación de Airbnb Clientes")
            database.connection.close()
            break
        if option == 1:
            facturasbe.getFacturasResidencias()
        if option == 2:
            facturasbe.getFacturasExp()
        if option == 3:
            facturasbe.insertarFacturaResidencia()
        if option == 4:
            facturasbe.insertarFacturaExp()

AppFacturas()