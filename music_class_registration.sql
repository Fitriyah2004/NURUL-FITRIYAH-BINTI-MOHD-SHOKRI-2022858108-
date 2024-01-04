-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 04, 2024 at 11:58 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `music_class_registration`
--

-- --------------------------------------------------------

--
-- Table structure for table `class`
--

CREATE TABLE `class` (
  `student_full_name` text DEFAULT NULL,
  `student_year` int(100) DEFAULT NULL,
  `student_address` varchar(100) DEFAULT NULL,
  `student_gender` text DEFAULT NULL,
  `parent_full_name` text DEFAULT NULL,
  `parent_email` varchar(100) DEFAULT NULL,
  `student_set` varchar(100) DEFAULT NULL,
  `student_pack_quantity` int(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `class`
--

INSERT INTO `class` (`student_full_name`, `student_year`, `student_address`, `student_gender`, `parent_full_name`, `parent_email`, `student_set`, `student_pack_quantity`) VALUES
('ryan', 1, 'no 1 lorong 16 taman indah', 'Male', 'guwon', 'guwon@gmail.com', 'Package 2', 1),
('Rina Rose', 3, 'block A, flat 236, Taman Permata Jaya', 'Female', 'Hassan Bin Mail', 'sassan_mail@gmail.com', 'Package 2', 1);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
