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
-- Table structure for table `caozuo_jilu`
--

DROP TABLE IF EXISTS `caozuo_jilu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `caozuo_jilu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `yh_id` int(11) DEFAULT NULL COMMENT '用户编号',
  `CaoZuo` varchar(100) DEFAULT NULL COMMENT '操作',
  `NeiRong` varchar(100) DEFAULT NULL COMMENT '内容',
  `RiQi` varchar(100) DEFAULT NULL COMMENT '日期',
  `ShiJian` varchar(100) DEFAULT NULL COMMENT '时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `caozuo_jilu`
--

LOCK TABLES `caozuo_jilu` WRITE;
/*!40000 ALTER TABLE `caozuo_jilu` DISABLE KEYS */;
INSERT INTO `caozuo_jilu` VALUES (1,1,'批量上传','001.jpg','2013-11-07','19H58M11S'),(2,1,'批量上传','002.jpg','2013-11-07','19H58M12S'),(3,1,'批量上传','003.jpg','2013-11-07','19H58M12S'),(4,1,'批量上传','005.jpg','2013-11-07','19H58M13S'),(5,1,'批量上传','001.jpg','2013-11-08','09H53M45S'),(6,1,'批量上传','002.jpg','2013-11-08','09H53M52S'),(7,1,'修改档案信息','39','2013-11-14','11H58M11S'),(8,1,'修改档案信息','39','2013-11-14','11H59M32S'),(9,1,'修改档案信息','1','2013-11-14','12H05M11S'),(10,1,'修改档案信息','39','2013-11-14','12H05M25S'),(11,1,'添加档案信息','11288','2013-12-09','14H52M01S'),(12,1,'修改档案信息','1','2013-12-09','15H12M56S'),(13,1,'修改档案信息','1','2013-12-09','15H13M52S'),(14,1,'修改档案信息','1','2013-12-09','15H16M07S'),(15,1,'修改档案信息','1','2013-12-09','15H16M19S'),(16,1,'修改档案信息','1','2013-12-09','16H22M29S'),(17,1,'修改档案信息','1','2013-12-09','16H24M24S'),(18,1,'修改档案信息','1','2013-12-09','16H24M40S'),(19,1,'修改档案信息','8','2014-01-02','15H27M45S'),(20,1,'修改档案信息','8','2014-01-02','15H29M00S'),(21,1,'修改档案信息','1','2014-01-09','17H32M55S'),(22,1,'修改档案信息','1','2014-01-09','17H33M00S'),(23,1,'修改档案信息','1','2014-01-10','16H28M37S'),(24,1,'添加档案信息','40','2014-01-13','14H39M36S'),(25,1,'批量上传','001.jpg','2014-01-16','09H57M20S'),(26,1,'修改档案信息','39','2014-01-27','09H56M49S'),(27,1,'修改档案信息','39','2014-01-27','09H56M55S'),(28,1,'修改档案信息','39','2014-04-17','15H11M33S'),(29,1,'修改档案信息','39','2014-04-17','15H11M41S'),(30,1,'添加档案信息','40','2014-04-17','15H24M03S'),(31,1,'添加档案信息','41','2014-04-17','15H24M30S'),(32,1,'上传图片','39','2014-04-17','19H58M13S'),(33,1,'上传图片','1','2014-04-17','15H24M30S'),(34,1,'上传图片','40','2014-04-17','19H58M13S'),(35,1,'上传图片','40','2014-04-17','19H58M13S'),(36,2,'上传图片','1','2013-12-09','16H24M40S'),(37,2,'上传图片','39','2013-12-09','16H24M40S'),(38,2,'上传图片','39','2013-12-09','16H24M40S'),(39,1,'上传图片','41','2014-04-18','10H00M13S'),(40,1,'上传图片','41','2014-04-18','10H19M27S'),(41,1,'上传图片','41','2014-04-18','10H21M53S'),(42,1,'上传图片','41','2014-04-18','10H21M57S'),(43,1,'上传图片','41','2014-04-18','10H22M12S'),(44,1,'上传图片','41','2014-04-18','10H22M17S'),(45,2,'上传图片','39','2014-04-18','10H25M31S'),(46,1,'批量上传','39','2014-04-20','12H34M58S');
/*!40000 ALTER TABLE `caozuo_jilu` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-04-23 23:06:53
