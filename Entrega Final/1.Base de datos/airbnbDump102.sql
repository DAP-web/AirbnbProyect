CREATE DATABASE  IF NOT EXISTS `airbnb` /*!40100 DEFAULT CHARACTER SET utf8 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `airbnb`;
-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: localhost    Database: airbnb
-- ------------------------------------------------------
-- Server version	8.0.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `accesibilidades`
--

DROP TABLE IF EXISTS `accesibilidades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accesibilidades` (
  `idAccesibilidades` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) NOT NULL,
  `Descripcion` varchar(100) NOT NULL,
  PRIMARY KEY (`idAccesibilidades`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accesibilidades`
--

LOCK TABLES `accesibilidades` WRITE;
/*!40000 ALTER TABLE `accesibilidades` DISABLE KEYS */;
INSERT INTO `accesibilidades` VALUES (1,'Acceso al Lugar','Lugar abierto con muchas llegadas'),(2,'Facilidad de movilizacion','Hay en la casa agarraderas'),(3,'Dormitorios','Cama con altura accesible'),(4,'Banhos','Aseo Personal'),(5,'Areas comunes','No hay escaleras ni escalones para ingresar'),(6,'Estacionamiento','Pasillos amplios'),(7,'Equipamiento','Para hacer ejercicio');
/*!40000 ALTER TABLE `accesibilidades` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `calificaciones`
--

DROP TABLE IF EXISTS `calificaciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `calificaciones` (
  `idCalificacion` int NOT NULL AUTO_INCREMENT,
  `Calificacion` tinyint NOT NULL,
  `IdResidencia` int NOT NULL,
  PRIMARY KEY (`idCalificacion`),
  KEY `fk_Calificaciones_Residencias1_idx` (`IdResidencia`),
  CONSTRAINT `fk_Calificaciones_Residencias1` FOREIGN KEY (`IdResidencia`) REFERENCES `residencias` (`idResidencia`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `calificaciones`
--

LOCK TABLES `calificaciones` WRITE;
/*!40000 ALTER TABLE `calificaciones` DISABLE KEYS */;
INSERT INTO `calificaciones` VALUES (1,5,9),(2,5,10),(3,4,11),(4,2,9),(5,4,10),(6,4,12),(7,4,9),(8,3,11),(9,5,12);
/*!40000 ALTER TABLE `calificaciones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ciudades`
--

DROP TABLE IF EXISTS `ciudades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ciudades` (
  `idCiudad` int NOT NULL AUTO_INCREMENT,
  `NombreCiudad` varchar(45) NOT NULL,
  `IdPais` int NOT NULL,
  PRIMARY KEY (`idCiudad`),
  KEY `fk_Ciudades_Paises1_idx` (`IdPais`),
  CONSTRAINT `fk_Ciudades_Paises1` FOREIGN KEY (`IdPais`) REFERENCES `paises` (`idPais`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ciudades`
--

LOCK TABLES `ciudades` WRITE;
/*!40000 ALTER TABLE `ciudades` DISABLE KEYS */;
INSERT INTO `ciudades` VALUES (1,'Missouri',2),(2,'Hamburg',1),(3,'San Salvador',3),(4,'La Libertad',3),(6,'Brasilia',9),(8,'Montevideo',14),(9,'San Pedro Sula',26),(10,'Santa Cruz de Tenerife',29),(11,'Liada',30),(12,'Atenas',20),(13,'Paris',17),(14,'Oranjestad',32);
/*!40000 ALTER TABLE `ciudades` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes` (
  `idClientes` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(45) NOT NULL,
  `Apellido` varchar(45) NOT NULL,
  `NumeroTelefonico` varchar(20) NOT NULL,
  `Pais` varchar(45) NOT NULL,
  `Correo` varchar(60) NOT NULL,
  `Contrasenha` varchar(45) NOT NULL,
  `Usuario` varchar(45) NOT NULL,
  PRIMARY KEY (`idClientes`),
  UNIQUE KEY `Usuario_UNIQUE` (`Usuario`),
  UNIQUE KEY `Correo_UNIQUE` (`Correo`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` VALUES (1,'Diego','Portillo','63212542','Alemania','d@p.com','lossuperheroes','superportillo'),(2,'Tammy','Portillo','62514452','Estados Unidos','t@p.com','guafguaf','negrita'),(3,'Angela','Ruiz','62354126','Italia','a@r.com','lasheroinas','gossi'),(7,'Aaron','Ramos','15462354','Venezuela','aaron@aaron.aaron','aaron','Ejau'),(8,'James','March','54125262','Estados Unidos','j@m.com','hotel','jpatrickM'),(9,'Sheldon','Cooper','61542635','Estados Unidos','sheldon@cal.com','physics','scooper'),(12,'Victoria','Zepeda','56632248','Cuba','v@az.com','villacincos','azepeda'),(14,'Gaby','Beltran','12524263','El Salvador','g@b.com','password','gbeltran'),(15,'Giovanni','Portillo','52633541','Ecuador','g@gp.com','warzone','gplikol'),(16,'Marcela','Mata','21455263','El Salvador','m@m.com','hellomerci','merci'),(17,'Raul','Reyes','52633451','El Salvador','r@r54.com','rreyes','rrey');
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `direcciones`
--

DROP TABLE IF EXISTS `direcciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `direcciones` (
  `IdDireccion` int NOT NULL AUTO_INCREMENT,
  `Estado` varchar(45) NOT NULL,
  `CodigoPostal` varchar(45) NOT NULL,
  `Calle` varchar(45) NOT NULL,
  `IdCiudad` int NOT NULL,
  PRIMARY KEY (`IdDireccion`),
  KEY `fk_Direcciones_Ciudades1_idx` (`IdCiudad`),
  CONSTRAINT `fk_Direcciones_Ciudades1` FOREIGN KEY (`IdCiudad`) REFERENCES `ciudades` (`idCiudad`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `direcciones`
--

LOCK TABLES `direcciones` WRITE;
/*!40000 ALTER TABLE `direcciones` DISABLE KEYS */;
INSERT INTO `direcciones` VALUES (1,'Missouri','6542','Brave Street',2),(2,'Colonia','1623','6th Kirk Street',1),(3,'La Libertad','6251','San Ignacio',3),(4,'California','1632','Main Street',1),(6,'Las Bahamas','6241','Cortez Blanco',1),(9,'Pasadena','6323','Los coballos',8),(11,'San Pedro Sula','1263','Los juates',9),(12,'Calixto','1523','Las Urmillas',11),(13,'Acropolis','1523','Acropolis',12),(14,'Lux','4526','Main',13),(15,'Arubackley','5423','Main',14),(16,'jola','4521','jein',14);
/*!40000 ALTER TABLE `direcciones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `experiencia`
--

DROP TABLE IF EXISTS `experiencia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `experiencia` (
  `idExp` int NOT NULL AUTO_INCREMENT,
  `NombreAnfitrion` varchar(60) NOT NULL,
  `TituloExperiencia` varchar(50) NOT NULL,
  `TipoDeExperiencia` tinyint NOT NULL,
  `Ubicacion` varchar(50) NOT NULL,
  `Descripcion` text NOT NULL,
  `Idioma` varchar(45) NOT NULL,
  `PublicoObjetivo` text NOT NULL,
  `Organizacion` varchar(70) NOT NULL,
  `AnfitrionExp` text NOT NULL,
  `ElementosANecesitar` text NOT NULL,
  `PrecioIndividual` decimal(5,2) NOT NULL,
  `Fecha` datetime NOT NULL,
  `IdTematica` int NOT NULL,
  PRIMARY KEY (`idExp`),
  KEY `fk_Experiencia_Tematica1_idx` (`IdTematica`),
  CONSTRAINT `fk_Experiencia_Tematica1` FOREIGN KEY (`IdTematica`) REFERENCES `tematica` (`idTematica`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `experiencia`
--

LOCK TABLES `experiencia` WRITE;
/*!40000 ALTER TABLE `experiencia` DISABLE KEYS */;
INSERT INTO `experiencia` VALUES (1,'Diego','Un viaje a las estreallas',1,'Los Angeles','Blow your mind','Aleman','Jovenes de alreededor de 20 anhos','Ninguna','Alta','Disposicion',18.00,'2020-01-03 15:00:00',1),(2,'Alejandro','Aventuras',0,'New Jersey','Blowing','Ingles','Jovenes','Sae','Media','Lapiz y hoja de papel',25.00,'2020-12-24 13:00:00',2),(3,'Jesse','LATAM',0,'Chile','Atentos','Espanhol','Todos','JJ','Alta','Oidos y disposicion',13.00,'2021-01-15 08:30:00',3),(4,'Claudia','Se un lider',1,'Hamburg','Atrevete','Aleman','Jovenes','Cambridge','Alta','Disposicion',15.50,'2020-12-12 14:00:00',1),(6,'TedEx','Pensando',1,'Mi casa','Pensar hasta las estrellas','Ingles','Adultos','LLL','Alta','Cerebro',9.00,'2020-12-18 05:00:00',3),(7,'Diego Portillo','Dakiti',1,'La masetomia','Perreo hasta el suelo','Espanhol','Jovenes','Bad bunny','Alta','Trago',7.50,'2020-12-15 21:50:00',2),(9,'Tamara','Vamos a dormir',0,'2','Durmiendo','Ingles','Jovenes','Bji','Alta','disposicion',12.50,'2020-12-15 15:00:00',11),(10,'Herbalife','Por que no tomar herbshake',0,'Zoom','Beneficios del herbshake','Espanhol','Jovenes des','herbalife','medio','Agua',5.50,'2020-12-23 09:00:00',12);
/*!40000 ALTER TABLE `experiencia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `experienciaresidencia`
--

DROP TABLE IF EXISTS `experienciaresidencia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `experienciaresidencia` (
  `idER` int NOT NULL AUTO_INCREMENT,
  `IdExp` int NOT NULL,
  `IdResidencia` int NOT NULL,
  PRIMARY KEY (`idER`),
  KEY `fk_ExperienciaResidencia_Experiencia1_idx` (`IdExp`),
  KEY `fk_ExperienciaResidencia_Residencias1_idx` (`IdResidencia`),
  CONSTRAINT `fk_ExperienciaResidencia_Experiencia1` FOREIGN KEY (`IdExp`) REFERENCES `experiencia` (`idExp`),
  CONSTRAINT `fk_ExperienciaResidencia_Residencias1` FOREIGN KEY (`IdResidencia`) REFERENCES `residencias` (`idResidencia`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `experienciaresidencia`
--

LOCK TABLES `experienciaresidencia` WRITE;
/*!40000 ALTER TABLE `experienciaresidencia` DISABLE KEYS */;
INSERT INTO `experienciaresidencia` VALUES (1,1,9),(2,2,10),(3,3,11);
/*!40000 ALTER TABLE `experienciaresidencia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `experiencias`
--

DROP TABLE IF EXISTS `experiencias`;
/*!50001 DROP VIEW IF EXISTS `experiencias`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `experiencias` AS SELECT 
 1 AS `idExp`,
 1 AS `NombreAnfitrion`,
 1 AS `TituloExperiencia`,
 1 AS `TipoDeExperiencia`,
 1 AS `Ubicacion`,
 1 AS `Descripcion`,
 1 AS `Idioma`,
 1 AS `PublicoObjetivo`,
 1 AS `Organizacion`,
 1 AS `AnfitrionExp`,
 1 AS `ElementosANecesitar`,
 1 AS `Precio`,
 1 AS `Fecha`,
 1 AS `NombreTematica`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `factura`
--

DROP TABLE IF EXISTS `factura`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `factura` (
  `idFactura` int NOT NULL AUTO_INCREMENT,
  `IdResidencia` int DEFAULT NULL,
  `IdReserva` int DEFAULT NULL,
  `IdCliente` int NOT NULL,
  `IdExp` int DEFAULT NULL,
  `IVA` tinyint NOT NULL,
  `Subtotal` decimal(8,2) NOT NULL,
  `Cupon` tinyint DEFAULT NULL,
  PRIMARY KEY (`idFactura`),
  KEY `fk_Factura_Residencias1_idx` (`IdResidencia`),
  KEY `fk_Factura_Clientes1_idx` (`IdCliente`),
  KEY `fk_Factura_Experiencia1_idx` (`IdExp`),
  KEY `fk_Factura_Reservacion1_idx` (`IdReserva`),
  CONSTRAINT `fk_Factura_Clientes1` FOREIGN KEY (`IdCliente`) REFERENCES `clientes` (`idClientes`),
  CONSTRAINT `fk_Factura_Experiencia1` FOREIGN KEY (`IdExp`) REFERENCES `experiencia` (`idExp`),
  CONSTRAINT `fk_Factura_Reservacion1` FOREIGN KEY (`IdReserva`) REFERENCES `reservaciones` (`IdReserva`),
  CONSTRAINT `fk_Factura_Residencias1` FOREIGN KEY (`IdResidencia`) REFERENCES `residencias` (`idResidencia`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `factura`
--

LOCK TABLES `factura` WRITE;
/*!40000 ALTER TABLE `factura` DISABLE KEYS */;
INSERT INTO `factura` VALUES (1,9,1,1,NULL,13,288.15,0),(2,10,2,2,NULL,13,250.65,1),(4,NULL,NULL,2,2,0,250.31,1),(6,10,21,3,NULL,13,226.00,1),(7,NULL,NULL,2,2,13,29.75,0),(8,NULL,NULL,8,6,13,10.71,0),(9,NULL,NULL,1,3,13,15.47,0),(10,NULL,NULL,2,3,13,15.47,0),(11,NULL,NULL,1,3,13,15.47,0),(12,NULL,NULL,1,4,13,17.51,1),(13,11,22,1,NULL,13,339.00,1),(14,NULL,NULL,1,9,13,14.88,0),(15,12,23,2,NULL,13,294.16,1),(16,11,24,2,NULL,13,366.00,0),(17,13,25,16,NULL,13,16.95,1),(18,NULL,NULL,16,6,13,10.17,1),(19,NULL,NULL,16,3,13,15.47,0),(20,NULL,NULL,2,4,13,17.51,1);
/*!40000 ALTER TABLE `factura` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `facturaexperiencias`
--

DROP TABLE IF EXISTS `facturaexperiencias`;
/*!50001 DROP VIEW IF EXISTS `facturaexperiencias`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `facturaexperiencias` AS SELECT 
 1 AS `idFactura`,
 1 AS `IdExp`,
 1 AS `PrecioIndividual`,
 1 AS `Fecha`,
 1 AS `Cliente`,
 1 AS `NumeroTelefonico`,
 1 AS `IVA`,
 1 AS `Subtotal`,
 1 AS `Cupon`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `facturaresidencias`
--

DROP TABLE IF EXISTS `facturaresidencias`;
/*!50001 DROP VIEW IF EXISTS `facturaresidencias`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `facturaresidencias` AS SELECT 
 1 AS `idFactura`,
 1 AS `IdResidencia`,
 1 AS `IdReserva`,
 1 AS `Precio`,
 1 AS `Cliente`,
 1 AS `FechaEmitida`,
 1 AS `NumeroTelefonico`,
 1 AS `IVA`,
 1 AS `Subtotal`,
 1 AS `Cupon`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `paises`
--

DROP TABLE IF EXISTS `paises`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `paises` (
  `idPais` int NOT NULL AUTO_INCREMENT,
  `NombrePais` varchar(45) NOT NULL,
  `CodigoTelefonico` varchar(5) NOT NULL,
  PRIMARY KEY (`idPais`),
  UNIQUE KEY `NombrePais_UNIQUE` (`NombrePais`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paises`
--

LOCK TABLES `paises` WRITE;
/*!40000 ALTER TABLE `paises` DISABLE KEYS */;
INSERT INTO `paises` VALUES (1,'Alemania','+49'),(2,'Estados Unidos','+1'),(3,'El Salvador','+503'),(4,'Costa Rica','+506'),(5,'Panamá','+507'),(6,'Nicaragua','+505'),(7,'Cuba','+53'),(8,'Argentina','+54'),(9,'Brasil','+55'),(10,'Canada','+1'),(11,'Guatemala','+502'),(12,'Mexico','+52'),(13,'Puerto Rico','+1'),(14,'Uruguay','+598'),(15,'Suiza','+41'),(16,'Austria','+43'),(17,'Francia','+33'),(18,'Espanha','+34'),(19,'Finlandia','+358'),(20,'Grecia','+30'),(21,'Holanda','+31'),(22,'Italia','+39'),(24,'Chile','+56'),(26,'Honduras','+504'),(27,'Belice','+501'),(29,'Islas Canarias','+922'),(30,'Angola','+244'),(32,'Aruba','+297');
/*!40000 ALTER TABLE `paises` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `raccesibilidades`
--

DROP TABLE IF EXISTS `raccesibilidades`;
/*!50001 DROP VIEW IF EXISTS `raccesibilidades`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `raccesibilidades` AS SELECT 
 1 AS `idAccesibilidades`,
 1 AS `IdResidencia`,
 1 AS `Nombre`,
 1 AS `Descripcion`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `reservaciones`
--

DROP TABLE IF EXISTS `reservaciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservaciones` (
  `IdReserva` int NOT NULL AUTO_INCREMENT,
  `IdCliente` int NOT NULL,
  `IdResidencia` int NOT NULL,
  `FechaLlegada` varchar(50) NOT NULL,
  `FechaRetirada` varchar(50) NOT NULL,
  `Adultos` int DEFAULT NULL,
  `Ninhos` int DEFAULT NULL,
  `Bebes` int DEFAULT NULL,
  `TipoPago` tinyint NOT NULL,
  PRIMARY KEY (`IdReserva`),
  KEY `fk_Reservaciones_Clientes_idx` (`IdCliente`),
  KEY `fk_Reservaciones_Residencias1_idx` (`IdResidencia`),
  CONSTRAINT `fk_Reservaciones_Clientes` FOREIGN KEY (`IdCliente`) REFERENCES `clientes` (`idClientes`),
  CONSTRAINT `fk_Reservaciones_Residencias1` FOREIGN KEY (`IdResidencia`) REFERENCES `residencias` (`idResidencia`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservaciones`
--

LOCK TABLES `reservaciones` WRITE;
/*!40000 ALTER TABLE `reservaciones` DISABLE KEYS */;
INSERT INTO `reservaciones` VALUES (1,1,9,'05-06-2012 04:00:00','05-10-2012 04:00:00',2,0,0,0),(2,2,10,'05-06-2012 04:00:00','05-10-2012 04:00:00',1,2,3,0),(3,3,11,'05-10-2012 04:00:00','05-12-2012 04:00:00',1,0,0,0),(4,8,10,'24-11-2020 15:00:00','15-12-2020 12:00:00',1,0,0,1),(5,9,10,'16-10-2021 9:00:00','02-11-2021 12:00:00',4,0,3,0),(8,7,11,'16-01-2021 18:00','20-01-2021 17:30',4,1,0,0),(9,1,11,'15-11-2020 15:00:00','1-1-2021 9:00:00',1,0,0,0),(10,1,11,'12-12-2020 11:00','3-1-2021 14:30',2,0,0,1),(14,1,10,'6-12-2020 12:00','25-12-2020 6:00',1,0,1,1),(17,14,13,'13-12-2020 13:00','15-1-2021 7:00',2,0,0,0),(18,1,12,'23-12-2020 7:00','3-1-2021 13:00',3,2,1,0),(19,2,11,'13-12-2020 13:00','30-12-2020 13:00',2,0,0,0),(21,3,10,'13-12-2020 17:00','17-1-2021 13:00',2,1,0,1),(22,1,11,'12-12-2020 15:00','12-1-2020 13:00',1,0,1,1),(23,2,12,'15-12-2020 15:00','15-1-2021 15:00',1,0,0,1),(24,2,11,'21-2-2020 15:00','5-3-2020 16:00',1,1,0,1),(25,16,13,'15-12-2020 12:00','16-1-2021 8:00',4,2,0,0);
/*!40000 ALTER TABLE `reservaciones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `reservas`
--

DROP TABLE IF EXISTS `reservas`;
/*!50001 DROP VIEW IF EXISTS `reservas`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `reservas` AS SELECT 
 1 AS `IdReserva`,
 1 AS `Cliente`,
 1 AS `NumeroTelefonico`,
 1 AS `IdResidencia`,
 1 AS `FechaLlegada`,
 1 AS `FechaRetirada`,
 1 AS `Adultos`,
 1 AS `Ninhos`,
 1 AS `Bebes`,
 1 AS `TipoPago`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `residenciaaccesibilidad`
--

DROP TABLE IF EXISTS `residenciaaccesibilidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `residenciaaccesibilidad` (
  `idRA` int NOT NULL AUTO_INCREMENT,
  `IdAccesibilidad` int NOT NULL,
  `IdResidencia` int NOT NULL,
  PRIMARY KEY (`idRA`),
  KEY `fk_ResidenciaAccesibilidad_Accesibilidad1_idx` (`IdAccesibilidad`),
  KEY `fk_ResidenciaAccesibilidad_Residencias1_idx` (`IdResidencia`),
  CONSTRAINT `fk_ResidenciaAccesibilidad_Accesibilidad1` FOREIGN KEY (`IdAccesibilidad`) REFERENCES `accesibilidades` (`idAccesibilidades`),
  CONSTRAINT `fk_ResidenciaAccesibilidad_Residencias1` FOREIGN KEY (`IdResidencia`) REFERENCES `residencias` (`idResidencia`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `residenciaaccesibilidad`
--

LOCK TABLES `residenciaaccesibilidad` WRITE;
/*!40000 ALTER TABLE `residenciaaccesibilidad` DISABLE KEYS */;
INSERT INTO `residenciaaccesibilidad` VALUES (1,1,11),(2,1,10),(3,2,9),(4,3,10),(5,5,10);
/*!40000 ALTER TABLE `residenciaaccesibilidad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `residencias`
--

DROP TABLE IF EXISTS `residencias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `residencias` (
  `idResidencia` int NOT NULL AUTO_INCREMENT,
  `TipoAlojamiento` varchar(45) DEFAULT NULL,
  `Habitaciones` int DEFAULT NULL,
  `Banhos` int DEFAULT NULL,
  `Camas` int DEFAULT NULL,
  `IdDireccion` int NOT NULL,
  `Precio` decimal(8,2) NOT NULL,
  `FlexibilidadDeCancelacion` tinyint NOT NULL,
  `AirbnbPlus` tinyint NOT NULL,
  `Mascotas` tinyint NOT NULL,
  `Fumadores` tinyint NOT NULL,
  PRIMARY KEY (`idResidencia`),
  KEY `fk_Residencias_Direcciones1_idx` (`IdDireccion`),
  CONSTRAINT `fk_Residencias_Direcciones1` FOREIGN KEY (`IdDireccion`) REFERENCES `direcciones` (`IdDireccion`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `residencias`
--

LOCK TABLES `residencias` WRITE;
/*!40000 ALTER TABLE `residencias` DISABLE KEYS */;
INSERT INTO `residencias` VALUES (9,'Entera',3,3,3,1,200.00,0,0,0,0),(10,'Hotel',5,4,6,2,200.00,0,1,1,0),(11,'Compartida',1,1,2,1,300.00,1,0,1,1),(12,'Motel',1,1,2,3,260.32,1,1,1,0),(13,'Habitacion',1,1,2,2,15.00,1,0,0,0),(15,'Habitaciones',3,4,3,9,360.00,1,1,1,0),(18,'Habitacion',1,1,2,14,150.00,0,1,1,0),(20,'Entero',4,4,4,16,1584.26,0,1,1,0);
/*!40000 ALTER TABLE `residencias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `residenciaservicio`
--

DROP TABLE IF EXISTS `residenciaservicio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `residenciaservicio` (
  `idRS` int NOT NULL AUTO_INCREMENT,
  `IdServicio` int NOT NULL,
  `IdResidencia` int NOT NULL,
  PRIMARY KEY (`idRS`),
  KEY `fk_ResidenciaServicio_Servicios1_idx` (`IdServicio`),
  KEY `fk_ResidenciaServicio_Residencias1_idx` (`IdResidencia`),
  CONSTRAINT `fk_ResidenciaServicio_Residencias1` FOREIGN KEY (`IdResidencia`) REFERENCES `residencias` (`idResidencia`),
  CONSTRAINT `fk_ResidenciaServicio_Servicios1` FOREIGN KEY (`IdServicio`) REFERENCES `servicios` (`idServicio`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `residenciaservicio`
--

LOCK TABLES `residenciaservicio` WRITE;
/*!40000 ALTER TABLE `residenciaservicio` DISABLE KEYS */;
INSERT INTO `residenciaservicio` VALUES (1,1,9),(2,2,9),(3,3,10),(4,1,11),(5,2,11),(10,5,12),(11,8,13),(12,1,13);
/*!40000 ALTER TABLE `residenciaservicio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `servicios`
--

DROP TABLE IF EXISTS `servicios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `servicios` (
  `idServicio` int NOT NULL AUTO_INCREMENT,
  `NombreServicio` varchar(50) NOT NULL,
  PRIMARY KEY (`idServicio`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `servicios`
--

LOCK TABLES `servicios` WRITE;
/*!40000 ALTER TABLE `servicios` DISABLE KEYS */;
INSERT INTO `servicios` VALUES (1,'Cocina'),(2,'Calefaccion'),(3,'Champu'),(5,'Desayuna de la casa'),(6,'Almuerzo de la Casa'),(8,'Carro Incluido');
/*!40000 ALTER TABLE `servicios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tematica`
--

DROP TABLE IF EXISTS `tematica`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tematica` (
  `idTematica` int NOT NULL AUTO_INCREMENT,
  `NombreTematica` varchar(45) NOT NULL,
  `Descripcion` text NOT NULL,
  PRIMARY KEY (`idTematica`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tematica`
--

LOCK TABLES `tematica` WRITE;
/*!40000 ALTER TABLE `tematica` DISABLE KEYS */;
INSERT INTO `tematica` VALUES (1,'Bebida','Bebida con tokyo'),(2,'Deportes acuaticos','Agua, sudor y powerade'),(3,'Deportes en combate ','Sangre,sudor y gloria'),(6,'Hawai','Sol, playa y arena'),(7,'Halloween','Sustos, dulces y mucha diversion'),(10,'Pajama Party','Un dia para dormir y aprender'),(11,'Pensando en dormir','Vamos a dormir'),(12,'HerbForever','Todos somos herbalife');
/*!40000 ALTER TABLE `tematica` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `experiencias`
--

/*!50001 DROP VIEW IF EXISTS `experiencias`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `experiencias` AS select `experiencia`.`idExp` AS `idExp`,`experiencia`.`NombreAnfitrion` AS `NombreAnfitrion`,`experiencia`.`TituloExperiencia` AS `TituloExperiencia`,`experiencia`.`TipoDeExperiencia` AS `TipoDeExperiencia`,`experiencia`.`Ubicacion` AS `Ubicacion`,`experiencia`.`Descripcion` AS `Descripcion`,`experiencia`.`Idioma` AS `Idioma`,`experiencia`.`PublicoObjetivo` AS `PublicoObjetivo`,`experiencia`.`Organizacion` AS `Organizacion`,`experiencia`.`AnfitrionExp` AS `AnfitrionExp`,`experiencia`.`ElementosANecesitar` AS `ElementosANecesitar`,`experiencia`.`PrecioIndividual` AS `Precio`,`experiencia`.`Fecha` AS `Fecha`,`tematica`.`NombreTematica` AS `NombreTematica` from (`experiencia` join `tematica` on((`experiencia`.`IdTematica` = `tematica`.`idTematica`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `facturaexperiencias`
--

/*!50001 DROP VIEW IF EXISTS `facturaexperiencias`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `facturaexperiencias` AS select `factura`.`idFactura` AS `idFactura`,`factura`.`IdExp` AS `IdExp`,`experiencia`.`PrecioIndividual` AS `PrecioIndividual`,`experiencia`.`Fecha` AS `Fecha`,concat(`clientes`.`Nombre`,' ',`clientes`.`Apellido`) AS `Cliente`,`clientes`.`NumeroTelefonico` AS `NumeroTelefonico`,`factura`.`IVA` AS `IVA`,`factura`.`Subtotal` AS `Subtotal`,`factura`.`Cupon` AS `Cupon` from ((`clientes` join `factura` on((`clientes`.`idClientes` = `factura`.`IdCliente`))) join `experiencia` on((`factura`.`IdExp` = `experiencia`.`idExp`))) where (`factura`.`IdResidencia` is null) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `facturaresidencias`
--

/*!50001 DROP VIEW IF EXISTS `facturaresidencias`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `facturaresidencias` AS select `factura`.`idFactura` AS `idFactura`,`factura`.`IdResidencia` AS `IdResidencia`,`reservaciones`.`IdReserva` AS `IdReserva`,`residencias`.`Precio` AS `Precio`,concat(`clientes`.`Nombre`,' ',`clientes`.`Apellido`) AS `Cliente`,`reservaciones`.`FechaRetirada` AS `FechaEmitida`,`clientes`.`NumeroTelefonico` AS `NumeroTelefonico`,`factura`.`IVA` AS `IVA`,`factura`.`Subtotal` AS `Subtotal`,`factura`.`Cupon` AS `Cupon` from (((`clientes` join `factura` on((`clientes`.`idClientes` = `factura`.`IdCliente`))) join `residencias` on((`factura`.`IdResidencia` = `residencias`.`idResidencia`))) join `reservaciones` on((`factura`.`IdReserva` = `reservaciones`.`IdReserva`))) where (`factura`.`IdExp` is null) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `raccesibilidades`
--

/*!50001 DROP VIEW IF EXISTS `raccesibilidades`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `raccesibilidades` AS select `accesibilidades`.`idAccesibilidades` AS `idAccesibilidades`,`residenciaaccesibilidad`.`IdResidencia` AS `IdResidencia`,`accesibilidades`.`Nombre` AS `Nombre`,`accesibilidades`.`Descripcion` AS `Descripcion` from (`residenciaaccesibilidad` join `accesibilidades` on((`residenciaaccesibilidad`.`IdAccesibilidad` = `accesibilidades`.`idAccesibilidades`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `reservas`
--

/*!50001 DROP VIEW IF EXISTS `reservas`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `reservas` AS select `reservaciones`.`IdReserva` AS `IdReserva`,concat(`clientes`.`Nombre`,' ',`clientes`.`Apellido`) AS `Cliente`,`clientes`.`NumeroTelefonico` AS `NumeroTelefonico`,`reservaciones`.`IdResidencia` AS `IdResidencia`,`reservaciones`.`FechaLlegada` AS `FechaLlegada`,`reservaciones`.`FechaRetirada` AS `FechaRetirada`,`reservaciones`.`Adultos` AS `Adultos`,`reservaciones`.`Ninhos` AS `Ninhos`,`reservaciones`.`Bebes` AS `Bebes`,`reservaciones`.`TipoPago` AS `TipoPago` from ((`clientes` join `reservaciones` on((`clientes`.`idClientes` = `reservaciones`.`IdCliente`))) join `residencias` on((`reservaciones`.`IdResidencia` = `residencias`.`idResidencia`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-08 16:11:26
