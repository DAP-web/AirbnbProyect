use airbnb;

/*Vista de reservas*/
create view reservas as
select reservaciones.IdReserva, concat(clientes.Nombre,' ',clientes.Apellido) as Cliente, 
	   clientes.NumeroTelefonico, reservaciones.IdResidencia, reservaciones.FechaLlegada, 
       reservaciones.FechaRetirada, reservaciones.Adultos, reservaciones.Ninhos,
       reservaciones.Bebes, reservaciones.TipoPago
from clientes inner join reservaciones on clientes.idClientes=reservaciones.IdCliente
			  inner join residencias on reservaciones.IdResidencia=residencias.idResidencia;