from prettytable import PrettyTable
from Core_databaseX import DatabaseX
from Logic_ExperienciasLogic import ExperienciaLogic
from View_Facturas import facturasBE
from Logic_TematicaLogic import TematicaLogic
from View_Tematica import TematicaBE

database = DatabaseX()
dbexperiencia = ExperienciaLogic()
befacturas = facturasBE()
dbtematica = TematicaLogic()
betematica = TematicaBE()

def ExperienciasPresenciales(cliente):
    result = dbexperiencia.buscarExperienciasPresenciales()

    table = PrettyTable()
    table1 = PrettyTable()

    table.field_names = ["idExp", "NombreAnfitrion", "TituloExperiencia", "TipoDeExperiencia",
    "Ubicacion", "Descripcion", "Idioma"]

    table1.field_names = ["idExp", "PublicoObjetivo", "Organizacion", "AnfitrionExp",
    "ElementosANecesitar", "Precio", "Fecha", "IdTematica"]

    for experiencia in result:
        table.add_row([
            experiencia.id,
            experiencia.host,
            experiencia.ExperienceTitle,
            experiencia.TypeExperience,
            experiencia.Location,
            experiencia.Descrption,
            experiencia.Idiom
        ])
        table1.add_row([
            experiencia.id,
            experiencia.PublicObject,
            experiencia.Organization,
            experiencia.hostExperience,
            experiencia.NeedElements,
            experiencia.precio,
            experiencia.fecha,
            experiencia.tematica
        ])

    print(table)
    table.clear()
    print(table1)
    table1.clear()

    option = int(input("¿Ver alguna experiencia en específico? (0-No||1-Sí): "))
    
    if option == 1:
        exp = int(input("Ingresa el ID de la experiencia (idExp): "))
        experiencia = dbexperiencia.searchExperienciaByIdView(exp)
        tablaexp = PrettyTable()
        tablaexp2 = PrettyTable()

        tablaexp.field_names = ["idExp", "NombreAnfitrion", "TituloExperiencia", "TipoDeExperiencia",
        "Ubicacion", "Descripcion", "Idioma"]

        tablaexp2.field_names = ["PublicoObjetivo", "Organizacion", "AnfitrionExp",
        "ElementosANecesitar", "Precio", "Fecha", "IdTematica"]

        tablaexp.add_row([
            experiencia.id,
            experiencia.host,
            experiencia.ExperienceTitle,
            experiencia.TypeExperience,
            experiencia.Location,
            experiencia.Descrption,
            experiencia.Idiom
        ])

        tablaexp2.add_row([
            experiencia.PublicObject,
            experiencia.Organization,
            experiencia.hostExperience,
            experiencia.NeedElements,
            experiencia.precio,
            experiencia.fecha,
            experiencia.tematica
        ])

        print(tablaexp)
        tablaexp.clear()
        print(tablaexp2)
        tablaexp2.clear()

        registro = int(input("Quieres registrarte para esta experiencia? (0-No||1-Sí): "))

        if registro == 1:
            befacturas.insertarFacturaExpProceso(exp, cliente.id)
