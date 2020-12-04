use airbnb;

/*Corrigiendo tabla experiencias*/
ALTER TABLE `airbnb`.`experiencia` 
ADD COLUMN `PrecioIndividual` DECIMAL(5,2) NOT NULL AFTER `Estado`;

UPDATE `airbnb`.`experiencia` SET `PrecioIndividual` = '18' WHERE (`idExp` = '1');
UPDATE `airbnb`.`experiencia` SET `PrecioIndividual` = '25' WHERE (`idExp` = '2');
UPDATE `airbnb`.`experiencia` SET `PrecioIndividual` = '13' WHERE (`idExp` = '3');

/*Corrigiendo tabla de Facturas*/
ALTER TABLE `airbnb`.`factura` 
ADD COLUMN `IdReserva` INT NULL AFTER `IdResidencia`;

ALTER TABLE `airbnb`.`factura` 
ADD INDEX `fk_Factura_Reservacion1_idx` (`IdReserva` ASC) VISIBLE;
;
ALTER TABLE `airbnb`.`factura` 
ADD CONSTRAINT `fk_Factura_Reservacion1`
  FOREIGN KEY (`IdReserva`)
  REFERENCES `airbnb`.`reservaciones` (`IdReserva`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

UPDATE `airbnb`.`factura` SET `IdReserva` = '1' WHERE (`idFactura` = '1');
UPDATE `airbnb`.`factura` SET `IdReserva` = '2' WHERE (`idFactura` = '2');
UPDATE `airbnb`.`factura` SET `IdReserva` = '3' WHERE (`idFactura` = '3');


/*Vista de reservas*/
create view reservas as
select reservaciones.IdReserva, concat(clientes.Nombre,' ',clientes.Apellido) as Cliente, 
	   clientes.NumeroTelefonico, reservaciones.IdResidencia, reservaciones.FechaLlegada, 
       reservaciones.FechaRetirada, reservaciones.Adultos, reservaciones.Ninhos,
       reservaciones.Bebes, reservaciones.TipoPago
from clientes inner join reservaciones on clientes.idClientes=reservaciones.IdCliente
			  inner join residencias on reservaciones.IdResidencia=residencias.idResidencia;
              
              
/*Vista de Ciudades y Paises*/
create view ciudadPais as
select ciudades.NombreCiudad,paises.NombrePais,paises.CodigoTelefonico
from ciudades inner join paises on ciudades.IdPais=paises.idPais;


/*Vista de Direcciones, Ciudades y Paises*/
create view direccionCompleta as
SELECT direcciones.IdDireccion,direcciones.Estado,direcciones.CodigoPostal,direcciones.Calle,ciudades.NombreCiudad,paises.NombrePais
from direcciones 
	 inner join ciudades on direcciones.IdCiudad=ciudades.idCiudad
     inner join paises on ciudades.IdPais=paises.idPais;

/*Vista de Residencias y Servicios*/
create view RServicio as
select residenciaservicio.IdResidencia,servicios.NombreServicio
from residenciaservicio inner join servicios on residenciaservicio.IdServicio=servicios.idServicio;


/*Vista de experiencias y tematicas*/
create view Experiencias as
select experiencia.NombreAnfitrion,experiencia.TituloExperiencia,experiencia.TipoDeExperiencia,experiencia.Ubicacion,experiencia.Descripcion,
		experiencia.Idioma,experiencia.PublicoObjetivo,experiencia.Organizacion,experiencia.AnfitrionExp,experiencia.ElementosANecesitar,
        experiencia.Estado,experiencia.PrecioIndividual,tematica.NombreTematica
from experiencia inner join tematica on experiencia.IdTematica=tematica.idTematica;


/*Vista de residencias y accesibilidades*/
create view RAccesibilidades as
select residenciaaccesibilidad.IdResidencia,accesibilidad.Nombre,desc_accesibilidad.Descripcion
from residenciaaccesibilidad
	 inner join accesibilidad on residenciaaccesibilidad.IdAccesibilidad=accesibilidad.idAccesibilidad
     inner join desc_accesibilidad on accesibilidad.idAccesibilidad=desc_accesibilidad.IdAccesibilidad;
     
     
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