use airbnb;

/*Vista de reservas*/
create view reservas as
select reservaciones.IdReserva, concat(clientes.Nombre,' ',clientes.Apellido) as Cliente, 
	   clientes.NumeroTelefonico, reservaciones.IdResidencia, reservaciones.FechaLlegada, 
       reservaciones.FechaRetirada, reservaciones.Adultos, reservaciones.Ninhos,
       reservaciones.Bebes, reservaciones.TipoPago
from clientes inner join reservaciones on clientes.idClientes=reservaciones.IdCliente
			  inner join residencias on reservaciones.IdResidencia=residencias.idResidencia;

/*Vista de Residencias y Servicios*/
create view RServicio as
select residenciaservicio.IdResidencia,servicios.NombreServicio
from residenciaservicio inner join servicios on residenciaservicio.IdServicio=servicios.idServicio;

alter view RAccesibilidades as
select accesibilidades.idAccesibilidades,residenciaaccesibilidad.IdResidencia,accesibilidades.Nombre,accesibilidades.Descripcion
from residenciaaccesibilidad
	inner join accesibilidades on residenciaaccesibilidad.IdAccesibilidad=accesibilidades.idAccesibilidades;

/*Vista de experiencias y tematicas*/
create view Experiencias as
select experiencia.NombreAnfitrion,experiencia.TituloExperiencia,experiencia.TipoDeExperiencia,experiencia.Ubicacion,experiencia.Descripcion,
		experiencia.Idioma,experiencia.PublicoObjetivo,experiencia.Organizacion,experiencia.AnfitrionExp,experiencia.ElementosANecesitar,
        experiencia.Estado,experiencia.PrecioIndividual,tematica.NombreTematica
from experiencia inner join tematica on experiencia.IdTematica=tematica.idTematica;
     
/*Vista de facturas y residencias*/
create view facturaResidencias as
select factura.idFactura,factura.IdResidencia,reservaciones.IdReserva,
	   residencias.Precio,concat(clientes.Nombre,' ',clientes.Apellido) as Cliente,
	   reservaciones.FechaRetirada as FechaEmitida,
       clientes.NumeroTelefonico,factura.IVA,factura.Subtotal,factura.Cupon
from clientes
	 inner join factura on clientes.idClientes=factura.IdCliente
     inner join residencias on factura.IdResidencia=residencias.idResidencia
     inner join reservaciones on factura.IdReserva=reservaciones.IdReserva
where factura.IdExp is null;

/*Vista de facturas y experiencias*/
create view facturaExperiencias as
select factura.idFactura,factura.IdExp,experiencia.PrecioIndividual,concat(clientes.Nombre,' ',clientes.Apellido) as Cliente,
	   clientes.NumeroTelefonico,factura.IVA,factura.Subtotal,factura.Cupon
from clientes
	 inner join factura on clientes.idClientes=factura.IdCliente
     inner join experiencia on factura.IdExp=experiencia.idExp
where factura.IdResidencia is null;