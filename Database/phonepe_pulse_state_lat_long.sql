-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: phonepe_pulse
-- ------------------------------------------------------
-- Server version	8.0.32

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
-- Table structure for table `state_lat_long`
--

DROP TABLE IF EXISTS `state_lat_long`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `state_lat_long` (
  `State` varchar(50) NOT NULL,
  `Latitude` float NOT NULL,
  `Longitude` float NOT NULL,
  `Region` varchar(50) NOT NULL,
  PRIMARY KEY (`State`,`Latitude`,`Longitude`,`Region`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `state_lat_long`
--

LOCK TABLES `state_lat_long` WRITE;
/*!40000 ALTER TABLE `state_lat_long` DISABLE KEYS */;
INSERT INTO `state_lat_long` VALUES ('Andaman and Nicobar Islands',12.6112,92.8317,'Southern Region'),('Andhra Pradesh',15.9241,80.1864,'Southern Region'),('Arunachal Pradesh',28.0938,94.5921,'North-Eastern Region'),('Assam',26.4074,93.2551,'North-Eastern Region'),('Bihar',25.6441,85.9065,'Eastern Region'),('Chandigarh',30.7298,76.7841,'Northern Region'),('Chhattisgarh',21.6637,81.8406,'Central Region'),('Dadra and Nagar Haveli and Daman and Diu',20.7182,70.9324,'Western Region'),('Delhi',28.6274,77.1717,'Northern Region'),('Goa',15.3005,74.0855,'Southern Region'),('Gujarat',22.385,71.7453,'Western Region'),('Haryana',29,76,'Northern Region'),('Himachal Pradesh',31.8168,77.3493,'Northern Region'),('Jammu and Kashmir',33.6649,75.163,'Northern Region'),('Jharkhand',23.456,85.2557,'Eastern Region'),('Karnataka',14.5204,75.7224,'Southern Region'),('Kerala',10.3529,76.512,'Southern Region'),('Ladakh',33.9456,77.6569,'Northern Region'),('Lakshadweep',10.8132,73.6805,'Southern Region'),('Madhya Pradesh',23.8143,77.5341,'Central Region'),('Maharashtra',18.9068,75.6742,'Western Region'),('Manipur',24.7209,93.9229,'North-Eastern Region'),('Meghalaya',25.5379,91.2999,'North-Eastern Region'),('Mizoram',23.2146,92.8688,'North-Eastern Region'),('Nagaland',26.1631,94.5885,'North-Eastern Region'),('Odisha',20.5431,84.6897,'Eastern Region'),('Puducherry',10.9156,79.8069,'Southern Region'),('Punjab',30.9293,75.5005,'Northern Region'),('Rajasthan',26.8106,73.7685,'Western Region'),('Tamil Nadu',10.9094,78.3665,'Southern Region'),('Telangana',17.8496,79.1152,'Southern Region'),('Tripura',23.7751,91.7025,'North-Eastern Region'),('Uttar Pradesh',27.1303,80.8597,'Central Region'),('Uttarakhand',30.0417,79.0897,'Northern Region'),('West Bengal',22.9965,87.6856,'Eastern Region');
/*!40000 ALTER TABLE `state_lat_long` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-27  3:35:35
