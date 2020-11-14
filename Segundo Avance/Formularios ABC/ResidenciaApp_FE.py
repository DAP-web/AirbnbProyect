from Residencia_BE import (
    connection,
    getAllResidencias,
    addResidencia,
    updateResidencia,
    deleteResidencia,
)

print("Inicializando la app de Airbnb Residencia")
while True:
    Menu = """\nElija una de las siguientes opciones:
    0-Salir de la app
    1- Recuperar todos las residencias
    2-Ingresar una nueva residencia
    3-Actualizar residencia
    4-Eliminar residencia\n"""
    print("-" * 100)
    print(Menu)
    print("-" * 100)
    option = int(input("Opción: "))

    if option == 0:
        print("\nDeteniendo la aplicación de Airbnb Residencia")
        connection.close()
        break
    if option == 1:
        getAllResidencias()
    if option == 2:
        addResidencia()
    if option == 3:
        updateResidencia()
    if option == 4:
        deleteResidencia()