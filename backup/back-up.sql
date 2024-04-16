CREATE DATABASE  IF NOT EXISTS `thebox_bd` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `thebox_bd`;
-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: thebox_bd
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `asistencia`
--

DROP TABLE IF EXISTS `asistencia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `asistencia` (
  `idAsistencia` int NOT NULL AUTO_INCREMENT,
  `dni` int NOT NULL,
  `asistencia` date NOT NULL,
  PRIMARY KEY (`idAsistencia`)
) ENGINE=InnoDB AUTO_INCREMENT=244 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci MAX_ROWS=1000000;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `asistencia`
--

LOCK TABLES `asistencia` WRITE;
/*!40000 ALTER TABLE `asistencia` DISABLE KEYS */;
INSERT INTO `asistencia` VALUES (227,20125487,'2024-02-27'),(228,11223344,'2024-02-27'),(229,30258963,'2024-02-27'),(230,32569858,'2024-02-27'),(231,23342423,'2024-02-27'),(232,34900111,'2024-02-27'),(233,40125478,'2024-02-27'),(234,20125487,'2024-02-27'),(235,30258963,'2024-02-28'),(236,43323232,'2024-02-28'),(237,20125487,'2024-02-28'),(238,11223344,'2024-02-28'),(239,45023654,'2024-03-12'),(240,12312354,'2024-03-14'),(241,30258963,'2024-03-14'),(242,40125478,'2024-03-14'),(243,65896523,'2024-03-14');
/*!40000 ALTER TABLE `asistencia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contabilidad`
--

DROP TABLE IF EXISTS `contabilidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contabilidad` (
  `id_concepto` int NOT NULL AUTO_INCREMENT,
  `fecha` date DEFAULT NULL,
  `concepto_debe` varchar(100) DEFAULT NULL,
  `concepto_haber` varchar(100) DEFAULT NULL,
  `debe` int DEFAULT NULL,
  `haber` int DEFAULT NULL,
  PRIMARY KEY (`id_concepto`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contabilidad`
--

LOCK TABLES `contabilidad` WRITE;
/*!40000 ALTER TABLE `contabilidad` DISABLE KEYS */;
INSERT INTO `contabilidad` VALUES (7,'2024-03-07','Retito',NULL,234242,0);
/*!40000 ALTER TABLE `contabilidad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `disciplina`
--

DROP TABLE IF EXISTS `disciplina`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `disciplina` (
  `idDisciplina` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `dni` int NOT NULL,
  `disciplina` varchar(45) NOT NULL,
  `precio` int NOT NULL,
  `fecha_pago` date NOT NULL,
  `modalidad` varchar(45) NOT NULL,
  `estado` varchar(45) NOT NULL,
  PRIMARY KEY (`idDisciplina`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `disciplina`
--

LOCK TABLES `disciplina` WRITE;
/*!40000 ALTER TABLE `disciplina` DISABLE KEYS */;
INSERT INTO `disciplina` VALUES (8,'Nicolas','Ripani',36724886,'Musculacion',5000,'2024-02-01','Efectivo','Pagado'),(9,'Marta','Gusano',65896523,'Funcional',6000,'2024-02-04','Efectivo','Pagado'),(10,'Julieta','Lopez',33669988,'Cross Funcional',6500,'2024-02-28','Efectivo','Pagado'),(11,'Manuel','Narigon',32569858,'Cardio',4500,'2024-02-03','Efectivo','Pagado'),(12,'Soledad','Kasas',28965478,'Ritmos',5000,'2024-02-07','Efectivo','Pagado'),(13,'Nicolas','Manso',20125487,'Adultos',4000,'2024-02-08','Efectivo','Pagado'),(14,'Paulina','Rajoi',30258963,'Stretching',6000,'2024-02-08','Efectivo','Pagado'),(15,'Matias','Polax',45023654,'Kids',4500,'2024-02-08','Efectivo','Pagado'),(16,'Franco ','Pepe',11223344,'Cross Funcional',6500,'2024-02-07','Transferecia','Pagado'),(17,'Nicolas','Loco',43323232,'Musculacion',5000,'2024-02-07','Transferecia','Pagado'),(18,'Melani','Jojoi',23342423,'Musculacion',5000,'2024-02-09','Transferecia','Pagado'),(19,'Caroluna','Polenr',40125478,'Gap',4000,'2024-02-10','Transferecia','Pagado'),(20,'Nicolas','Ripani',36724886,'Musculacion',5000,'2024-02-21','Efectivo','Pagado'),(21,'Soledad','Kasas',28965478,'Ritmos',5000,'2024-02-13','Efectivo','Pagado'),(22,'Melani','Jojoi',23342423,'Musculacion',5000,'2024-02-27','Transferecia','Pagado'),(23,'Paulina','Rajoi',30258963,'Stretching',6000,'2024-03-08','Efectivo','Pagado'),(24,'Soledad','Kasas',28965478,'Ritmos',5000,'2024-03-14','Efectivo','Pagado');
/*!40000 ALTER TABLE `disciplina` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `empleado`
--

DROP TABLE IF EXISTS `empleado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `empleado` (
  `id_ref` int NOT NULL AUTO_INCREMENT,
  `id_empleado` int NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `sexo` varchar(45) NOT NULL,
  `dni` varchar(45) NOT NULL,
  `horas_diaria` varchar(45) NOT NULL,
  `fecha` date NOT NULL,
  PRIMARY KEY (`id_ref`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empleado`
--

LOCK TABLES `empleado` WRITE;
/*!40000 ALTER TABLE `empleado` DISABLE KEYS */;
INSERT INTO `empleado` VALUES (3,1,'Nicolas','Ripani','Hombre','36724886','6','2024-03-05'),(5,2,'Julieta','Perico','Mujer','43243242','8','2024-03-04'),(6,2,'Julieta','Perico','Mujer','43243242','7','2024-03-05'),(7,3,'Fede','Reda','Hombre','34567890','8','2024-03-16');
/*!40000 ALTER TABLE `empleado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `profesor`
--

DROP TABLE IF EXISTS `profesor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `profesor` (
  `idProfesor` int NOT NULL AUTO_INCREMENT,
  `dni` int NOT NULL,
  `contraseña` varchar(45) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `ocupacion` varchar(45) NOT NULL,
  `sexo` varchar(45) NOT NULL,
  PRIMARY KEY (`idProfesor`)
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='				';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profesor`
--

LOCK TABLES `profesor` WRITE;
/*!40000 ALTER TABLE `profesor` DISABLE KEYS */;
INSERT INTO `profesor` VALUES (52,36724886,'456789','Sss','S','S','S'),(55,12345677,'456789hhh','Hh','L','L','L'),(56,12345677,'456789hhh','Hh','L','L','L'),(57,56985575,'h','L','L','B','A');
/*!40000 ALTER TABLE `profesor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registro_usuario`
--

DROP TABLE IF EXISTS `registro_usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `registro_usuario` (
  `idUser` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `dni` int NOT NULL,
  `sexo` varchar(45) NOT NULL,
  `edad` int NOT NULL,
  `disciplina` varchar(45) NOT NULL,
  `celular` varchar(40) NOT NULL,
  `fecha` date NOT NULL,
  PRIMARY KEY (`idUser`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registro_usuario`
--

LOCK TABLES `registro_usuario` WRITE;
/*!40000 ALTER TABLE `registro_usuario` DISABLE KEYS */;
INSERT INTO `registro_usuario` VALUES (9,'Marta','Gusano',65896523,'Mujer',25,'Funcional','3425632541','2024-02-04'),(10,'Julieta','Lopez',33669988,'Mujer',21,'Cross funcional','3425458896','2024-02-03'),(11,'Manuel','Narigon',32569858,'Hombre',22,'Cardio','3425632569','2024-02-03'),(13,'Nicolas','Manso',20125487,'Hombre',40,'Adultos','3424558888','2024-02-08'),(14,'Paulina','Rajoi',30258963,'Mujer',35,'Stretching','3425632145','2024-02-08'),(15,'Matias','Polax',45023654,'Hombre',15,'Kids','3425632145','2024-02-08'),(16,'Caroluna','Polenr',40125478,'Mujer',26,'Gap','3425632145','2024-02-10'),(17,'Franco','Pepe',11223344,'Hombre',23,'Cross funcional','3421412132','2024-02-07'),(18,'Nicolas','Loco',43323232,'Hombre',23,'Musculación','3423451211','2024-02-07'),(19,'Melani','Jojoi',23342423,'Mujer',33,'Musculación','3432442342','2024-02-09'),(20,'Jose','Garro',34900111,'Hombre',34,'Funcional','3424123321','2024-02-27'),(21,'','Hhhuh',12312354,'Mujer',45,'Musculación','3421558888','2024-03-11');
/*!40000 ALTER TABLE `registro_usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-17  1:27:16
