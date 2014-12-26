CREATE DATABASE  IF NOT EXISTS `cm_archieve` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `cm_archieve`;
-- MySQL dump 10.13  Distrib 5.6.14, for Win32 (x86)
--
-- Host: 125.211.221.215    Database: cm_archieve
-- ------------------------------------------------------
-- Server version	5.5.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `wenjian`
--

DROP TABLE IF EXISTS `wenjian`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `wenjian` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `aid` int(11) DEFAULT NULL,
  `LeiBie` int(11) DEFAULT NULL,
  `WenJianMing` varchar(100) DEFAULT NULL,
  `client_access` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=576 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wenjian`
--

LOCK TABLES `wenjian` WRITE;
/*!40000 ALTER TABLE `wenjian` DISABLE KEYS */;
INSERT INTO `wenjian` VALUES (473,2,9,'20140307114331343000.jpg',0),(474,2,9,'20140307114336520000.jpg',0),(475,2,9,'20140307114336886000.jpg',0),(476,2,9,'20140307114337096000.jpg',0),(477,2,9,'20140307114337354000.jpg',0),(478,2,9,'20140307114337565000.jpg',0),(479,2,9,'20140307114337705000.jpg',0),(480,2,9,'20140307114337845000.jpg',0),(481,2,9,'20140307114338018000.jpg',0),(482,2,9,'20140307114338182000.jpg',0),(483,2,9,'20140307114338310000.jpg',0),(484,2,9,'20140307114338496000.jpg',0),(485,2,9,'20140307114338964000.jpg',0),(486,2,9,'20140307114339122000.jpg',0),(487,2,9,'20140307114339294000.jpg',0),(488,2,9,'20140307114339508000.jpg',0),(489,2,9,'20140307114339648000.png',0),(490,2,9,'20140307114339892000.png',0),(491,2,9,'20140307114340142000.jpg',0),(492,2,9,'20140307114340276000.jpg',0),(493,2,9,'20140307114340609000.png',0),(494,2,9,'20140307114340744000.jpg',0),(495,2,9,'20140307114340984000.png',0),(496,2,9,'20140307114341121000.png',0),(497,2,9,'20140307114341261000.jpg',0),(498,2,9,'20140307114341408000.jpg',0),(499,2,9,'20140307114341655000.jpg',0),(500,2,9,'20140307114341803000.jpg',0),(501,1,9,'20140307114341955000.jpg',0),(502,1,9,'20140307114342079000.jpg',0),(503,1,9,'20140307114342212000.jpg',0),(504,1,9,'20140307114342361000.jpg',0),(505,1,9,'20140307114342505000.jpg',0),(506,1,9,'20140307114342650000.jpg',0),(507,1,9,'20140307114342793000.jpg',0),(508,1,9,'20140307114343050000.jpg',0),(509,1,9,'20140307114343206000.jpg',0),(510,1,9,'20140307114343338000.jpg',0),(511,1,9,'20140307114343507000.jpg',0),(512,1,9,'20140307114343709000.jpg',0),(513,1,9,'20140307114343871000.jpg',0),(514,1,9,'20140307114344003000.jpg',0),(515,1,9,'20140307114344141000.jpg',0),(516,1,9,'20140307114344278000.jpg',0),(517,1,9,'20140307114344424000.jpg',0),(518,1,9,'20140307114344573000.jpg',0),(519,1,9,'20140307114344735000.jpg',0),(520,1,9,'20140307114344981000.jpg',0),(521,1,9,'20140307114345123000.png',0),(522,39,1,'1.jpg',1),(523,39,2,'2.jpg',1),(524,39,3,'3.jpg',1),(525,39,4,'4.jpg',1),(561,39,9,'1.jpg',1),(562,39,8,'4.jpg',1),(563,39,7,'3.jpg',1),(564,39,6,'2.jpg',1),(565,39,5,'1.jpg',1),(566,39,1,'3.jpg',1),(567,39,1,'2.jpg',1),(568,41,1,'20140418100012692000.jpg',NULL),(569,41,1,'20140418101927244000.jpg',NULL),(570,41,1,'20140418102153023000.jpg',NULL),(571,41,1,'20140418102157154000.jpg',NULL),(572,41,5,'20140418102212797000.jpg',NULL),(573,41,5,'20140418102217146000.jpg',NULL),(574,39,1,'20140418102531210000.jpg',NULL),(575,39,1,'9e520155jw1e0lexmaktnj.jpg',NULL);
/*!40000 ALTER TABLE `wenjian` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-04-23 23:06:50
