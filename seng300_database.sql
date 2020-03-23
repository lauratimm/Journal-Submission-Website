-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 20, 2020 at 05:38 AM
-- Server version: 10.4.8-MariaDB
-- PHP Version: 7.3.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `seng300_database`
--

-- --------------------------------------------------------

--
-- Table structure for table `comment`
--

CREATE TABLE `comment` (
  `proposal_id` int(11) NOT NULL,
  `comment_text` mediumtext DEFAULT NULL,
  `reviewer_username` varchar(32) DEFAULT NULL,
  `paper_version` int(10) DEFAULT NULL COMMENT 'the version of the paper that the comment belongs to'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `paper`
--

CREATE TABLE `paper` (
  `paper_id` int(10) NOT NULL,
  `author` varchar(32) DEFAULT NULL,
  `file` blob DEFAULT NULL,
  `version` int(10) UNSIGNED DEFAULT NULL,
  `upload_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `proposal`
--

CREATE TABLE `proposal` (
  `proposal_id` int(10) NOT NULL,
  `paper_submission_author` int(10) DEFAULT NULL,
  `paper_submission_reviewer` int(10) DEFAULT NULL,
  `author` varchar(32) NOT NULL,
  `reviewer1` varchar(32) DEFAULT NULL,
  `reviewer2` varchar(32) DEFAULT NULL,
  `reviewer3` varchar(32) DEFAULT NULL,
  `status` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `username` varchar(32) NOT NULL,
  `password` varchar(45) DEFAULT NULL,
  `email_address` varchar(45) DEFAULT NULL,
  `roles` bit(4) NOT NULL COMMENT 'BIT 0: admin\nBIT 1: editor\nBIT 2: reviewer\nBIT 3: author',
  `school_id` int(8) UNSIGNED DEFAULT NULL,
  `first_name` varchar(45) DEFAULT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  `institution` varchar(45) DEFAULT NULL,
  `date_joined` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`username`, `password`, `email_address`, `roles`, `school_id`, `first_name`, `last_name`, `institution`, `date_joined`) VALUES
('admin', 'admin', 'admin@gmail.com', b'1111', NULL, NULL, NULL, NULL, NULL),
('jane.doe', 'abc', 'jane.doe', b'1111', NULL, NULL, NULL, NULL, NULL),
('john.doe', 'pass123', 'john.doe@gmail.com', b'1011', NULL, NULL, NULL, NULL, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `comment`
--
ALTER TABLE `comment`
  ADD KEY `proposal_id` (`proposal_id`),
  ADD KEY `user` (`reviewer_username`) USING BTREE;

--
-- Indexes for table `paper`
--
ALTER TABLE `paper`
  ADD PRIMARY KEY (`paper_id`),
  ADD KEY `user` (`author`);

--
-- Indexes for table `proposal`
--
ALTER TABLE `proposal`
  ADD PRIMARY KEY (`proposal_id`),
  ADD KEY `paper` (`paper_submission_author`,`paper_submission_reviewer`),
  ADD KEY `paper_reviewer` (`paper_submission_reviewer`),
  ADD KEY `author` (`author`),
  ADD KEY `reviewer1` (`reviewer1`),
  ADD KEY `reviewer3` (`reviewer3`),
  ADD KEY `reviewer2` (`reviewer2`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`username`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `comment`
--
ALTER TABLE `comment`
  ADD CONSTRAINT `proposal_id` FOREIGN KEY (`proposal_id`) REFERENCES `proposal` (`proposal_id`) ON UPDATE CASCADE;

--
-- Constraints for table `paper`
--
ALTER TABLE `paper`
  ADD CONSTRAINT `user` FOREIGN KEY (`author`) REFERENCES `user` (`username`) ON UPDATE CASCADE;

--
-- Constraints for table `proposal`
--
ALTER TABLE `proposal`
  ADD CONSTRAINT `author` FOREIGN KEY (`author`) REFERENCES `user` (`username`) ON UPDATE CASCADE,
  ADD CONSTRAINT `paper_author` FOREIGN KEY (`paper_submission_author`) REFERENCES `paper` (`paper_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `paper_reviewer` FOREIGN KEY (`paper_submission_reviewer`) REFERENCES `paper` (`paper_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `reviewer1` FOREIGN KEY (`reviewer1`) REFERENCES `user` (`username`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `reviewer2` FOREIGN KEY (`reviewer2`) REFERENCES `user` (`username`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `reviewer3` FOREIGN KEY (`reviewer3`) REFERENCES `user` (`username`) ON DELETE SET NULL ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
