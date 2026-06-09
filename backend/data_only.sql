-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: crm_hcp
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `hcps`
--

LOCK TABLES `hcps` WRITE;
/*!40000 ALTER TABLE `hcps` DISABLE KEYS */;
INSERT INTO `hcps` VALUES (1,'Dr. Priya Sharma','Cardiologist','Apollo Hospital','Hyderabad','priya@apollo.com','9876543210'),(2,'Dr. Rahul Mehta','Oncologist','Yashoda Hospital','Hyderabad','rahul@yashoda.com','9876543211'),(3,'Dr. Anita Rao','Neurologist','KIMS Hospital','Hyderabad','anita@kims.com','9876543212'),(4,'Dr. Sanjay Gupta','Diabetologist','Care Hospital','Hyderabad','sanjay@care.com','9876543213');
/*!40000 ALTER TABLE `hcps` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `interactions`
--

LOCK TABLES `interactions` WRITE;
/*!40000 ALTER TABLE `interactions` DISABLE KEYS */;
INSERT INTO `interactions` VALUES (1,1,'Email','2026-04-17','11:50','max','heart beats','clinical data','Drug - X','Neutral','yes','no','The healthcare professional (HCP) discussed the topic of heart beats during the interaction. A positive outcome was achieved, indicated by a \"yes\" result, suggesting the HCP\'s questions or concerns were addressed. No further follow-up actions are required as a result of this interaction.','2026-04-17 11:54:51'),(2,1,'Meeting','2026-04-17','11:59','Ravi Kumar, Sales Rep','Discussed Product X efficacy data for heart failure patients, shared Phase 3 trial results, doctor showed interest in prescribing','Product X brochure, Phase 3 clinical trial PDF','Product X — 5 units','Positive','Doctor agreed to prescribe Product X for 3 new patients next week','Send detailed clinical report by email, schedule follow-up call in 2 weeks','The HCP was presented with Product X efficacy data for heart failure patients, including Phase 3 trial results, which sparked interest in prescribing the product. The doctor agreed to prescribe Product X to 3 new patients the following week, demonstrating a positive outcome from the interaction. A follow-up call is scheduled in 2 weeks, and a detailed clinical report will be sent to the doctor via email.','2026-04-17 12:01:12');
/*!40000 ALTER TABLE `interactions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-06-09 14:16:04
