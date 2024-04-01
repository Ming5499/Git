-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: localhost    Database: hospital
-- ------------------------------------------------------
-- Server version	8.0.23

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
-- Table structure for table `benhnhan`
--

DROP TABLE IF EXISTS `benhnhan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `benhnhan` (
  `mabn` bigint NOT NULL AUTO_INCREMENT,
  `hoten` varchar(50) DEFAULT NULL,
  `ngaysinh` date DEFAULT NULL,
  `gioitinh` bit(1) DEFAULT NULL,
  `sodienthoai` varchar(12) DEFAULT NULL,
  `diachi` varchar(50) DEFAULT NULL,
  `ngaytiepnhan` date DEFAULT NULL,
  `noidungkham` varchar(50) DEFAULT NULL,
  `makhoa` varchar(50) DEFAULT NULL,
  `doituong` bit(1) DEFAULT NULL,
  `sothebaohiem` varchar(50) DEFAULT NULL,
  `loaibaohiem` float DEFAULT NULL,
  `nhapvien` bit(1) DEFAULT NULL,
  `lydonhapvien` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`mabn`)
) ENGINE=InnoDB AUTO_INCREMENT=142 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `benhnhan`
--

LOCK TABLES `benhnhan` WRITE;
/*!40000 ALTER TABLE `benhnhan` DISABLE KEYS */;
INSERT INTO `benhnhan` VALUES (1,'Thảo Quang','2000-03-17',_binary '','1243423424','Quảng Trị','2021-04-12','Khám Mắt ','Khoa Mắt - P.02',_binary '\0','',0,_binary '','đau mắt'),(2,'Minh Nguyễn ','2000-09-07',_binary '','12412423424','Hà Nội','2020-04-12','Khám tim','Khoa Tim - P.02',_binary '','2234234',25,_binary '','Đau tim vì thất tình'),(25,'Hưng Nguyễn','2021-04-15',_binary '','','Hải Phòng','2021-04-24','Khám tinh hoàn','',_binary '\0','',0,_binary '',''),(38,'Hà Trương','1999-01-01',_binary '','145235252','Đà Nẵng','2021-04-12','Khám Tim','Khoa Tim - P.02',_binary '','112313',50,_binary '',''),(44,'Long Phan','2000-01-01',_binary '\0','3425234555','Gia Lai','2021-04-10','Khám Răng Hàm Mặt','Khoa Răng Hàm Mặt - P.01',_binary '','353453',50,_binary '','Tai nạn giao thông'),(46,'Quân Nguyễn','2000-11-28',_binary '\0','53232525','Quảng Nôm','2021-04-13','Khám Thai','Khoa Sản - P.02',_binary '\0','',0,_binary '',''),(54,'Nguyên Nguyên','2000-02-28',_binary '','2398523553','Đà Nẵng','2021-04-10','Khám Chân','Khoa Chân - P.02',_binary '','23523552',100,_binary '','Gãy Chân do đá banh :))'),(124,'Hưng ngu','2000-09-09',_binary '','092359232','Đà Nẵng','2021-04-13','Khám Thai','Khoa Sản - P.01',_binary '','23525235',50,_binary '','Đau bụng'),(126,'Thông Hà','2000-01-01',_binary '\0','124124124','Quảng Bình','2021-04-13','Khám Mắt',' Khoa Mắt - P.01',_binary '\0','',0,_binary '\0',''),(139,'nguyen van a','2000-02-02',_binary '\0','1232523535','Lâm Đồng','2021-04-14','Khám Tim','Khoa Tim - P.02',_binary '\0','',0,_binary '',''),(141,'Minh Nguyen','2000-07-09',_binary '','1244124141','Thanh Hóa','2021-04-14','Khám Tim','Khoa Tim - P.02',_binary '','12414124124',50,_binary '\0','thất tình');
/*!40000 ALTER TABLE `benhnhan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chitietmau`
--

DROP TABLE IF EXISTS `chitietmau`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chitietmau` (
  `maChiTietMau` int NOT NULL AUTO_INCREMENT,
  `giaDonVi` int DEFAULT NULL,
  PRIMARY KEY (`maChiTietMau`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chitietmau`
--

LOCK TABLES `chitietmau` WRITE;
/*!40000 ALTER TABLE `chitietmau` DISABLE KEYS */;
/*!40000 ALTER TABLE `chitietmau` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chitietphong`
--

DROP TABLE IF EXISTS `chitietphong`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chitietphong` (
  `maphong` bigint NOT NULL,
  `mabn` bigint DEFAULT NULL,
  `ngaybatdau` date DEFAULT NULL,
  `ngayketthuc` date DEFAULT NULL,
  PRIMARY KEY (`maphong`),
  CONSTRAINT `chitietphong_ibfk_1` FOREIGN KEY (`maphong`) REFERENCES `phong` (`maphong`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chitietphong`
--

LOCK TABLES `chitietphong` WRITE;
/*!40000 ALTER TABLE `chitietphong` DISABLE KEYS */;
/*!40000 ALTER TABLE `chitietphong` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chitietthuoc`
--

DROP TABLE IF EXISTS `chitietthuoc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chitietthuoc` (
  `maThuoc` bigint NOT NULL,
  `ngayCapPhat` date DEFAULT NULL,
  `soLuong` float DEFAULT NULL,
  PRIMARY KEY (`maThuoc`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chitietthuoc`
--

LOCK TABLES `chitietthuoc` WRITE;
/*!40000 ALTER TABLE `chitietthuoc` DISABLE KEYS */;
/*!40000 ALTER TABLE `chitietthuoc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `donthuoc`
--

DROP TABLE IF EXISTS `donthuoc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `donthuoc` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `thoigian` date DEFAULT NULL,
  `mabn` bigint DEFAULT NULL,
  `thuoc` varchar(100) DEFAULT NULL,
  `soluong` int DEFAULT NULL,
  `tien` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `donthuoc`
--

LOCK TABLES `donthuoc` WRITE;
/*!40000 ALTER TABLE `donthuoc` DISABLE KEYS */;
INSERT INTO `donthuoc` VALUES (1,'2021-04-12',1,'Panadol',2,100000),(2,'2021-04-06',1,'Amicakin',3,50000),(3,'2021-04-08',1,'Ferlatum',5,10000),(4,'2021-04-10',1,'Betaphin',4,20000),(5,'2021-04-13',2,'Panadol',2,20000),(6,'2021-04-13',2,'Tiffy',1,15000);
/*!40000 ALTER TABLE `donthuoc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `khoa`
--

DROP TABLE IF EXISTS `khoa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `khoa` (
  `makhoa` bigint NOT NULL AUTO_INCREMENT,
  `tenkhoa` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`makhoa`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `khoa`
--

LOCK TABLES `khoa` WRITE;
/*!40000 ALTER TABLE `khoa` DISABLE KEYS */;
INSERT INTO `khoa` VALUES (1,'A'),(2,'Tim'),(3,'Khoa Sản');
/*!40000 ALTER TABLE `khoa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mau`
--

DROP TABLE IF EXISTS `mau`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mau` (
  `maMau` varchar(50) NOT NULL,
  `nhomMau` varchar(10) DEFAULT NULL,
  `soLuong` int DEFAULT NULL,
  `chitietmau` int NOT NULL,
  PRIMARY KEY (`maMau`),
  KEY `chitietmau` (`chitietmau`),
  CONSTRAINT `mau_ibfk_1` FOREIGN KEY (`chitietmau`) REFERENCES `chitietmau` (`maChiTietMau`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mau`
--

LOCK TABLES `mau` WRITE;
/*!40000 ALTER TABLE `mau` DISABLE KEYS */;
/*!40000 ALTER TABLE `mau` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nhanvien`
--

DROP TABLE IF EXISTS `nhanvien`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nhanvien` (
  `manv` bigint NOT NULL AUTO_INCREMENT,
  `hoten` varchar(50) DEFAULT NULL,
  `makhoa` bigint NOT NULL,
  `gioitinh` bit(1) DEFAULT NULL,
  `ngaysinh` date DEFAULT NULL,
  `diachi` varchar(100) DEFAULT NULL,
  `trangthai` varchar(50) DEFAULT NULL,
  `hesoluong` float DEFAULT NULL,
  `luong` float DEFAULT NULL,
  `motathem` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`manv`),
  KEY `makhoa` (`makhoa`),
  CONSTRAINT `nhanvien_ibfk_1` FOREIGN KEY (`makhoa`) REFERENCES `khoa` (`makhoa`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nhanvien`
--

LOCK TABLES `nhanvien` WRITE;
/*!40000 ALTER TABLE `nhanvien` DISABLE KEYS */;
INSERT INTO `nhanvien` VALUES (1,'Thao',1,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(2,'Thao',1,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(3,'Thảo Quang',2,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(4,'Trần Tuấn Hưng ',3,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(5,'Thao Quang',2,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `nhanvien` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phieukhambenh`
--

DROP TABLE IF EXISTS `phieukhambenh`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `phieukhambenh` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `mabn` bigint NOT NULL,
  `manv` bigint NOT NULL,
  `chuandoan` varchar(255) DEFAULT NULL,
  `ketluan` varchar(255) DEFAULT NULL,
  `donthuoc` varchar(255) DEFAULT NULL,
  `ngaytaikham` date DEFAULT NULL,
  `cantaikham` bit(1) DEFAULT NULL,
  `ngaychidinh` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `mabn` (`mabn`),
  KEY `manv` (`manv`),
  CONSTRAINT `phieukhambenh_ibfk_1` FOREIGN KEY (`mabn`) REFERENCES `benhnhan` (`mabn`) ON DELETE CASCADE,
  CONSTRAINT `phieukhambenh_ibfk_2` FOREIGN KEY (`manv`) REFERENCES `nhanvien` (`manv`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phieukhambenh`
--

LOCK TABLES `phieukhambenh` WRITE;
/*!40000 ALTER TABLE `phieukhambenh` DISABLE KEYS */;
INSERT INTO `phieukhambenh` VALUES (1,1,1,'Ho','Cusm','Vitamin C','2021-04-14',_binary '','2021-04-12'),(2,2,3,'Đau đầu, sổ mũi','Cảm cúm','Tiffy, Vitamin C','2021-04-30',_binary '','2021-04-13'),(3,139,3,'Nhồi máu cơ tim','Suy tim','Cần một tình yêu','2021-04-30',_binary '','2021-04-14'),(4,139,5,'Ho','Cảm ','Vitamin C','2021-04-30',_binary '','2021-04-14');
/*!40000 ALTER TABLE `phieukhambenh` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phieuxetnghiem`
--

DROP TABLE IF EXISTS `phieuxetnghiem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `phieuxetnghiem` (
  `mapxn` bigint NOT NULL AUTO_INCREMENT,
  `ngaythuchien` date DEFAULT NULL,
  `manv` bigint NOT NULL,
  `mabn` bigint NOT NULL,
  PRIMARY KEY (`mapxn`),
  KEY `manv` (`manv`),
  KEY `mabn` (`mabn`),
  CONSTRAINT `phieuxetnghiem_ibfk_1` FOREIGN KEY (`manv`) REFERENCES `nhanvien` (`manv`) ON DELETE CASCADE,
  CONSTRAINT `phieuxetnghiem_ibfk_2` FOREIGN KEY (`mabn`) REFERENCES `benhnhan` (`mabn`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phieuxetnghiem`
--

LOCK TABLES `phieuxetnghiem` WRITE;
/*!40000 ALTER TABLE `phieuxetnghiem` DISABLE KEYS */;
INSERT INTO `phieuxetnghiem` VALUES (1,'2021-04-12',1,1),(2,'2021-04-12',1,2),(3,'2021-04-14',5,139);
/*!40000 ALTER TABLE `phieuxetnghiem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phong`
--

DROP TABLE IF EXISTS `phong`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `phong` (
  `maphong` bigint NOT NULL AUTO_INCREMENT,
  `makhoa` bigint NOT NULL,
  `tenphong` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`maphong`),
  KEY `makhoa` (`makhoa`),
  CONSTRAINT `phong_ibfk_1` FOREIGN KEY (`makhoa`) REFERENCES `khoa` (`makhoa`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phong`
--

LOCK TABLES `phong` WRITE;
/*!40000 ALTER TABLE `phong` DISABLE KEYS */;
/*!40000 ALTER TABLE `phong` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pxn_xn`
--

DROP TABLE IF EXISTS `pxn_xn`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pxn_xn` (
  `mapxn` bigint NOT NULL,
  `maxn` bigint NOT NULL,
  `ketqua` int DEFAULT NULL,
  `ghichu` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`mapxn`,`maxn`),
  KEY `maxn` (`maxn`),
  CONSTRAINT `pxn_xn_ibfk_1` FOREIGN KEY (`mapxn`) REFERENCES `phieuxetnghiem` (`mapxn`) ON DELETE CASCADE,
  CONSTRAINT `pxn_xn_ibfk_2` FOREIGN KEY (`maxn`) REFERENCES `xetnghiem` (`maxn`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pxn_xn`
--

LOCK TABLES `pxn_xn` WRITE;
/*!40000 ALTER TABLE `pxn_xn` DISABLE KEYS */;
INSERT INTO `pxn_xn` VALUES (1,1,2,'khong'),(1,2,2,'khong'),(2,1,1,'khong'),(3,1,2,'khong'),(3,2,1,'khong');
/*!40000 ALTER TABLE `pxn_xn` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `taikhoan`
--

DROP TABLE IF EXISTS `taikhoan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `taikhoan` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(30) DEFAULT NULL,
  `password` text,
  `manv` bigint NOT NULL,
  `role` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `manv` (`manv`),
  CONSTRAINT `taikhoan_ibfk_1` FOREIGN KEY (`manv`) REFERENCES `nhanvien` (`manv`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `taikhoan`
--

LOCK TABLES `taikhoan` WRITE;
/*!40000 ALTER TABLE `taikhoan` DISABLE KEYS */;
INSERT INTO `taikhoan` VALUES (1,'bacsi','$2a$10$ZZ8ZSK6VMSIsXiSeELP5hOytkKto91TfZ4EbkUdhqI0WcCYQhVILa',1,'ROLE_BACSI'),(2,'yvu','$2a$10$vSCuw9NeqMYoBA3dzOF2EO3P.xYwh/DF5g2h12DKA7QSlb2XjF/wu',2,'ROLE_YVU'),(3,'thaoquang','$2a$10$o8QUTd5pwvfAdYKeILEM3OgHeWy2eLBMOMYo6Sy1Y4TfrS.tLkizG',3,'ROLE_BACSI'),(4,'hungngu','$2a$10$uw973EamUVy8XWggZ13QVu.uH9QeSroxdPWj300dG9tnTi32SjPRG',4,'ROLE_YVU'),(5,'thaokudo','$2a$10$cFtkDG7/DcBpIpWZZgWL0O1gSnzDMR95B6S9TthrUfY454sLIi43a',5,'ROLE_BACSI');
/*!40000 ALTER TABLE `taikhoan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `thuoc`
--

DROP TABLE IF EXISTS `thuoc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `thuoc` (
  `maThuoc` bigint NOT NULL AUTO_INCREMENT,
  `tenThuoc` varchar(50) DEFAULT NULL,
  `donGia` float DEFAULT NULL,
  `donVi` float DEFAULT NULL,
  `nhaCungCap` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`maThuoc`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `thuoc`
--

LOCK TABLES `thuoc` WRITE;
/*!40000 ALTER TABLE `thuoc` DISABLE KEYS */;
/*!40000 ALTER TABLE `thuoc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `xetnghiem`
--

DROP TABLE IF EXISTS `xetnghiem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `xetnghiem` (
  `maxn` bigint NOT NULL AUTO_INCREMENT,
  `tenxn` varchar(50) DEFAULT NULL,
  `donvi` varchar(20) DEFAULT NULL,
  `gia` float DEFAULT NULL,
  PRIMARY KEY (`maxn`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `xetnghiem`
--

LOCK TABLES `xetnghiem` WRITE;
/*!40000 ALTER TABLE `xetnghiem` DISABLE KEYS */;
INSERT INTO `xetnghiem` VALUES (1,'Glucose','mmol/L',15000),(2,'Ure','mmol/L',10000),(3,'HDL-C','mmol/L',25000),(4,'LDL-C','mmol/L',30000),(5,'Creamin','gmol/L',12000),(6,'Albumin','mmol/L',20000),(7,'Melamin','gmol/L',17000);
/*!40000 ALTER TABLE `xetnghiem` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-04-14 10:10:02
