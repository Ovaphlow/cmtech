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
-- Table structure for table `access_code`
--

DROP TABLE IF EXISTS `access_code`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `access_code` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `archieve_id` varchar(20) DEFAULT NULL,
  `code` varchar(10) DEFAULT NULL,
  `date` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `dangan`
--

DROP TABLE IF EXISTS `dangan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dangan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `DangAnHao` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  `ShenFenZheng` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  `XingMing` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  `XingBie` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  `ChuShengRiQi` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  `YuTuiXiuRiQi` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  `RenYuanLeiBie` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  `CunDangRiQi` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  `CunDangZhuangTai` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  `NvGuanLiGangWei` int(11) DEFAULT NULL,
  `TeShuGongZhong` int(11) DEFAULT NULL,
  `ZhuanChu` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `update_log`
--

DROP TABLE IF EXISTS `update_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `update_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(20) DEFAULT NULL,
  `ver` varchar(100) DEFAULT NULL,
  `content` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ZhangHao` varchar(100) DEFAULT NULL,
  `MiMa` varchar(20) DEFAULT NULL,
  `MingCheng` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-01-27 22:16:37
