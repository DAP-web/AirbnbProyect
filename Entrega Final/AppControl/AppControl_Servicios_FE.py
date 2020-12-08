from Views.View_Servicios import serviciosBE

def ServiciosAdmin():
    serviciosbe = serviciosBE()
    print("Inicializando la app de Airbnb Servicios")
    while True:
        Menu = """\nElija una de las siguientes opciones:
        0-Salir de la app
        1-Recuperar todos los servicios
        2-Ingresar un nuevo servicio
        3-Actualizar servicio
        4-Eliminar servicio\n"""
        print("-"*100)
        print(Menu)
        print("-"*100)
        option = int(input("Opción: "))

        if option == 0:
            print("\nDeteniendo la aplicación de Airbnb Servicios")
            break
        if option == 1:
            serviciosbe.getAllServices()
        if option == 2:
            serviciosbe.addService()
        if option == 3:
            serviciosbe.updateService()
        if option == 4:
            serviciosbe.deleteService()

# ServiciosAdmin()