ALTER TABLE `airbnb`.`experiencia` 
ADD COLUMN `Fecha` DATETIME NOT NULL AFTER `PrecioIndividual`;

ALTER TABLE `airbnb`.`experiencia` 
DROP COLUMN `Estado`;


/*Modificando la vista de facturasexperiencias*/
USE `airbnb`;
CREATE 
     OR REPLACE ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `facturaexperiencias` AS
    SELECT 
        `factura`.`idFactura` AS `idFactura`,
        `factura`.`IdExp` AS `IdExp`,
        `experiencia`.`PrecioIndividual` AS `PrecioIndividual`,
        `experiencia`.`Fecha` as `Fecha`,
        CONCAT(`clientes`.`Nombre`,
                ' ',
                `clientes`.`Apellido`) AS `Cliente`,
        `clientes`.`NumeroTelefonico` AS `NumeroTelefonico`,
        `factura`.`IVA` AS `IVA`,
        `factura`.`Subtotal` AS `Subtotal`,
        `factura`.`Cupon` AS `Cupon`
    FROM
        ((`clientes`
        JOIN `factura` ON ((`clientes`.`idClientes` = `factura`.`IdCliente`)))
        JOIN `experiencia` ON ((`factura`.`IdExp` = `experiencia`.`idExp`)))
    WHERE
        (`factura`.`IdResidencia` IS NULL);


USE `airbnb`;
CREATE 
     OR REPLACE ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `experiencias` AS
    SELECT 
		`experiencia`.`idExp` as `idExp`,
        `experiencia`.`NombreAnfitrion` AS `NombreAnfitrion`,
        `experiencia`.`TituloExperiencia` AS `TituloExperiencia`,
        `experiencia`.`TipoDeExperiencia` AS `TipoDeExperiencia`,
        `experiencia`.`Ubicacion` AS `Ubicacion`,
        `experiencia`.`Descripcion` AS `Descripcion`,
        `experiencia`.`Idioma` AS `Idioma`,
        `experiencia`.`PublicoObjetivo` AS `PublicoObjetivo`,
        `experiencia`.`Organizacion` AS `Organizacion`,
        `experiencia`.`AnfitrionExp` AS `AnfitrionExp`,
        `experiencia`.`ElementosANecesitar` AS `ElementosANecesitar`,
        `experiencia`.`PrecioIndividual` AS `Precio`,
        `experiencia`.`Fecha` AS `Fecha`,
        `experiencia`.`PrecioIndividual` AS `PrecioIndividual`,
        `tematica`.`NombreTematica` AS `NombreTematica`
    FROM
        (`experiencia`
        JOIN `tematica` ON ((`experiencia`.`IdTematica` = `tematica`.`idTematica`)));

USE `airbnb`;
CREATE 
     OR REPLACE ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `experiencias` AS
    SELECT 
        `experiencia`.`idExp` AS `idExp`,
        `experiencia`.`NombreAnfitrion` AS `NombreAnfitrion`,
        `experiencia`.`TituloExperiencia` AS `TituloExperiencia`,
        `experiencia`.`TipoDeExperiencia` AS `TipoDeExperiencia`,
        `experiencia`.`Ubicacion` AS `Ubicacion`,
        `experiencia`.`Descripcion` AS `Descripcion`,
        `experiencia`.`Idioma` AS `Idioma`,
        `experiencia`.`PublicoObjetivo` AS `PublicoObjetivo`,
        `experiencia`.`Organizacion` AS `Organizacion`,
        `experiencia`.`AnfitrionExp` AS `AnfitrionExp`,
        `experiencia`.`ElementosANecesitar` AS `ElementosANecesitar`,
        `experiencia`.`PrecioIndividual` AS `Precio`,
        `experiencia`.`Fecha` AS `Fecha`,
        `tematica`.`NombreTematica` AS `NombreTematica`
    FROM
        (`experiencia`
        JOIN `tematica` ON ((`experiencia`.`IdTematica` = `tematica`.`idTematica`)));
