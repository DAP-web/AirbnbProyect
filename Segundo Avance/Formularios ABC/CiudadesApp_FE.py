from Ciudades_BE import (
    connection,
    getAllCities,
    addCity,
    updateCity,
    deleteCity
)

print("Inicializando la app de Airbnb Ciudades")
while True:
    Menu = """\nElija una de las siguientes opciones:
    0-Salir de la app
    1-Recuperar todas las ciudades
    2-Ingresar una nueva ciudad
    3-Actualizar ciudad
    4-Eliminar ciudad\n"""
    print("-"*100)
    print(Menu)
    print("-"*100)
    option = int(input("Opción: "))

    if option == 0:
        print("\nDeteniendo la aplicación de Airbnb Ciudades")
        connection.close()
        break
    if option == 1:
        getAllCities()
    if option == 2:
        addCity()
    if option == 3:
        updateCity()
    if option == 4:
        deleteCity()
