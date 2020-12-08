from AppControl.AppControl_Accesibilidad_FE import AppAccesibilidades
from AppControl.AppControl_Calificaciones_FE import AppCalificaciones
from AppControl.AppControl_Ciudades_FE import AppCiudades
from AppControl.AppControl_Clientes_FE import AppClientes
from AppControl.AppControl_Direcciones_FE import direccionesAdmin
from AppControl.AppControl_ExperienciaResidencia_FE import ExperienciaresidenciasAppAdmin
from AppControl.AppControl_Experiencias_FE import ExperienciasAppAdmin
from AppControl.AppControl_Facturas_FE import AppFacturas
from AppControl.AppControl_Paises_FE import AppPaises
from AppControl.AppControl_Reservas_FE import reservasAdmin
from AppControl.AppControl_ResidenciaAccesibilidad_FE import AppRAccesibilidades
from AppControl.AppControl_ResidenciaServicio_FE import residenciaservicioAppAdmin
from AppControl.AppControl_Residencia_FE import residenciasAppAdmin
from AppControl.AppControl_Servicios_FE import ServiciosAdmin
from AppControl.AppControl_Tematica_FE import TematicaAppAdmin
from AppControl.BuscarExpFull import ExperienciasAppAdmin
from AppControl.AppControl_OrdenarExperiencia_FE import AppOrganizarExperiencia

class Admin:
    def __init__(self):
        pass

    def AccesibilidadesApp(self):
        AppAccesibilidades()

    def CalificacionesApp(self):
        AppCalificaciones()
    
    def CiudadesApp(self):
        AppCiudades()

    def ClientesApp(self):
        AppClientes()
    
    def DireccionesApp(self):
        direccionesAdmin()

    def expResApp(self):
        ExperienciaresidenciasAppAdmin()

    def experienciaApp(self):
        ExperienciasAppAdmin()

    def FacturasApp(self):
        AppFacturas()

    def PaisesApp(self):
        AppPaises()

    def ReservasApp(self):
        reservasAdmin()

    def AccResApp(self):
        AppRAccesibilidades()

    def ServResApp(self):
        residenciaservicioAppAdmin()

    def ResidenciaApp(self):
        residenciasAppAdmin()

    def ServiciosApp(self):
        ServiciosAdmin()

    def TematicaApp(self):
        TematicaAppAdmin()

    def buscarExpFull(self):
        ExperienciasAppAdmin()

    def organizarExperiencia(self):
        AppOrganizarExperiencia()