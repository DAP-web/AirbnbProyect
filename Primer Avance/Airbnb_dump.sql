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
-- Table structure for table `accesibilidad`
--

DROP TABLE IF EXISTS `accesibilidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accesibilidad` (
  `idAccesibilidad` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) NOT NULL,
  PRIMARY KEY (`idAccesibilidad`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accesibilidad`
--

LOCK TABLES `accesibilidad` WRITE;
/*!40000 ALTER TABLE `accesibilidad` DISABLE KEYS */;
INSERT INTO `accesibilidad` VALUES (1,'Acceso al Lugar'),(2,'Facilidad de movilizacion'),(3,'Dormitorios'),(4,'Banhos'),(5,'Areas comunes'),(6,'Estacionamiento'),(7,'Equipamiento');
/*!40000 ALTER TABLE `accesibilidad` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `calificaciones`
--

LOCK TABLES `calificaciones` WRITE;
/*!40000 ALTER TABLE `calificaciones` DISABLE KEYS */;
INSERT INTO `calificaciones` VALUES (1,5,9),(2,5,10),(3,4,11);
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ciudades`
--

LOCK TABLES `ciudades` WRITE;
/*!40000 ALTER TABLE `ciudades` DISABLE KEYS */;
INSERT INTO `ciudades` VALUES (1,'Missouri',2),(2,'Hamburg',1),(3,'Misata',3);
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` VALUES (1,'Diego','Portillo','15426359','Alemania','d@p.com','lossuperheroes','superportillo'),(2,'Tammy','Portillo','62514452','Estados Unidos','t@p.com','guafguaf','tporguaf'),(3,'Angela','Ruiz','62354126','Italia','a@r.com','lasheroinas','gossi');
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `desc_accesibilidad`
--

DROP TABLE IF EXISTS `desc_accesibilidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `desc_accesibilidad` (
  `idDA` int NOT NULL AUTO_INCREMENT,
  `Descripcion` varchar(100) NOT NULL,
  `IdAccesibilidad` int NOT NULL,
  PRIMARY KEY (`idDA`),
  KEY `fk_Desc_Accesibilidad_Accesibilidad1_idx` (`IdAccesibilidad`),
  CONSTRAINT `fk_Desc_Accesibilidad_Accesibilidad1` FOREIGN KEY (`IdAccesibilidad`) REFERENCES `accesibilidad` (`idAccesibilidad`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `desc_accesibilidad`
--

LOCK TABLES `desc_accesibilidad` WRITE;
/*!40000 ALTER TABLE `desc_accesibilidad` DISABLE KEYS */;
INSERT INTO `desc_accesibilidad` VALUES (5,'No hay escaleras ni escalones para ingresar',1),(6,'Pasillos amplios',2),(7,'Cama con altura accesible',3);
/*!40000 ALTER TABLE `desc_accesibilidad` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `direcciones`
--

LOCK TABLES `direcciones` WRITE;
/*!40000 ALTER TABLE `direcciones` DISABLE KEYS */;
INSERT INTO `direcciones` VALUES (1,'La Libertad','1501','Santiago',2),(2,'Missisipy','1623','San Juan Nonualco',1),(3,'Texas','6251','San Ignacio',3);
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
  `Estado` tinyint NOT NULL,
  `IdTematica` int NOT NULL,
  PRIMARY KEY (`idExp`),
  KEY `fk_Experiencia_Tematica1_idx` (`IdTematica`),
  CONSTRAINT `fk_Experiencia_Tematica1` FOREIGN KEY (`IdTematica`) REFERENCES `tematica` (`idTematica`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `experiencia`
--

LOCK TABLES `experiencia` WRITE;
/*!40000 ALTER TABLE `experiencia` DISABLE KEYS */;
INSERT INTO `experiencia` VALUES (1,'Diego','Un viaje a las estreallas',1,'Los Angeles','Blow your mind','Aleman','Jovenes de alreededor de 20 anhos','Ninguna','Alta','Disposicion',1,1),(2,'Alejandro','Aventuras',0,'New Jersey','Blowing','Ingles','Jovenes','Sae','Media','Lapiz y hoja de papel',0,2),(3,'Jesse','LATAM',0,'Chile','Atentos','Espanhol','Todos','JJ','Alta','Oidos y disposicion',1,3);
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
-- Table structure for table `factura`
--

DROP TABLE IF EXISTS `factura`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `factura` (
  `idFactura` int NOT NULL AUTO_INCREMENT,
  `IdResidencia` int DEFAULT NULL,
  `IdCliente` int NOT NULL,
  `IdExp` int DEFAULT NULL,
  `IVA` tinyint NOT NULL,
  `Subtotal` decimal(8,2) NOT NULL,
  `Cupon` tinyint DEFAULT NULL,
  PRIMARY KEY (`idFactura`),
  KEY `fk_Factura_Residencias1_idx` (`IdResidencia`),
  KEY `fk_Factura_Clientes1_idx` (`IdCliente`),
  KEY `fk_Factura_Experiencia1_idx` (`IdExp`),
  CONSTRAINT `fk_Factura_Clientes1` FOREIGN KEY (`IdCliente`) REFERENCES `clientes` (`idClientes`),
  CONSTRAINT `fk_Factura_Experiencia1` FOREIGN KEY (`IdExp`) REFERENCES `experiencia` (`idExp`),
  CONSTRAINT `fk_Factura_Residencias1` FOREIGN KEY (`IdResidencia`) REFERENCES `residencias` (`idResidencia`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `factura`
--

LOCK TABLES `factura` WRITE;
/*!40000 ALTER TABLE `factura` DISABLE KEYS */;
INSERT INTO `factura` VALUES (1,9,1,NULL,13,288.15,0),(2,10,2,NULL,13,250.65,1),(3,11,3,NULL,13,200.00,0),(4,NULL,2,2,0,250.31,1);
/*!40000 ALTER TABLE `factura` ENABLE KEYS */;
UNLOCK TABLES;

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
  PRIMARY KEY (`idPais`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paises`
--

LOCK TABLES `paises` WRITE;
/*!40000 ALTER TABLE `paises` DISABLE KEYS */;
INSERT INTO `paises` VALUES (1,'Alemania','+15'),(2,'Estados Unidos','+1'),(3,'El Salvador','+503');
/*!40000 ALTER TABLE `paises` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservaciones`
--

LOCK TABLES `reservaciones` WRITE;
/*!40000 ALTER TABLE `reservaciones` DISABLE KEYS */;
INSERT INTO `reservaciones` VALUES (1,1,9,'05-06-2012 04:00:00','05-10-2012 04:00:00',2,0,0,0),(2,2,10,'05-06-2012 04:00:00','05-10-2012 04:00:00',1,2,0,1),(3,3,11,'05-10-2012 04:00:00','05-12-2012 04:00:00',1,0,0,0);
/*!40000 ALTER TABLE `reservaciones` ENABLE KEYS */;
UNLOCK TABLES;

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
  CONSTRAINT `fk_ResidenciaAccesibilidad_Accesibilidad1` FOREIGN KEY (`IdAccesibilidad`) REFERENCES `accesibilidad` (`idAccesibilidad`),
  CONSTRAINT `fk_ResidenciaAccesibilidad_Residencias1` FOREIGN KEY (`IdResidencia`) REFERENCES `residencias` (`idResidencia`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `residenciaaccesibilidad`
--

LOCK TABLES `residenciaaccesibilidad` WRITE;
/*!40000 ALTER TABLE `residenciaaccesibilidad` DISABLE KEYS */;
INSERT INTO `residenciaaccesibilidad` VALUES (1,1,11),(2,1,10),(3,2,9),(4,4,9),(5,5,10);
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
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `residencias`
--

LOCK TABLES `residencias` WRITE;
/*!40000 ALTER TABLE `residencias` DISABLE KEYS */;
INSERT INTO `residencias` VALUES (9,'Entera',3,3,3,1,200.00,0,0,0,0),(10,'Hotel',NULL,NULL,NULL,2,250.00,0,1,1,0),(11,'Compartida',1,1,2,1,300.00,1,0,1,1);
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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `residenciaservicio`
--

LOCK TABLES `residenciaservicio` WRITE;
/*!40000 ALTER TABLE `residenciaservicio` DISABLE KEYS */;
INSERT INTO `residenciaservicio` VALUES (1,1,9),(2,2,9),(3,3,10),(4,1,11),(5,2,11);
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `servicios`
--

LOCK TABLES `servicios` WRITE;
/*!40000 ALTER TABLE `servicios` DISABLE KEYS */;
INSERT INTO `servicios` VALUES (1,'Cocina'),(2,'Calefaccion'),(3,'Champu');
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tematica`
--

LOCK TABLES `tematica` WRITE;
/*!40000 ALTER TABLE `tematica` DISABLE KEYS */;
INSERT INTO `tematica` VALUES (1,'Bebida','Bebida'),(2,'Deportes acuaticos','DA'),(3,'Deportes en combate ','DC');
/*!40000 ALTER TABLE `tematica` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-10-06 18:52:43
