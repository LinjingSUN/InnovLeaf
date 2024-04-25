/*
SQLyog Ultimate v10.00 Beta1
MySQL - 8.0.27 : Database - innovleaf
*********************************************************************
*/


/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`innovleaf` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `innovleaf`;

-- Use a specific database or create a new one
-- DROP DATABASE IF EXISTS `reading_db`;
-- CREATE DATABASE `reading_db`;
-- USE `reading_db`;

-- Table creation for storing user details
CREATE TABLE `users` (
    `user_id` INT AUTO_INCREMENT PRIMARY KEY,
    `age` INT,
    `gender` ENUM('male', 'female', 'other'),
    `language_level` VARCHAR(50)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Table for storing user preferences
CREATE TABLE `preferences` (
    `preference_id` INT AUTO_INCREMENT PRIMARY KEY,
    `user_id` INT,
    `description_avoid` VARCHAR(255),
    `objectives_achieved` TEXT,
    `progress_areas` TEXT,
    `story_requirements` TEXT,
    `story_type` VARCHAR(50),
    `favourite_stories` TEXT,
    `favourite_characters` TEXT,
    `story_topics` VARCHAR(255),
    `reading_voice_type` VARCHAR(50),
    `color_preferences` VARCHAR(50),
    `reading_habit` VARCHAR(100),
    FOREIGN KEY (`user_id`) REFERENCES `users`(`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Table for storing book details
CREATE TABLE `books` (
    `book_id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(100),
    `description` TEXT,
    `create_time` date DEFAULT NULL,
    `cover_image_url` VARCHAR(255)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Table for storing pages of the books
CREATE TABLE `pages` (
    `page_id` INT AUTO_INCREMENT PRIMARY KEY,
    `book_id` INT,
    `page_number` INT,
    `sentence` TEXT,
    `image_url` VARCHAR(255),
    INDEX `book_id_index` (`book_id`),
    CONSTRAINT `fk_pages_books` FOREIGN KEY (`book_id`) REFERENCES `books`(`book_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Table for tracking user progress
CREATE TABLE `progress` (
    `progress_id` INT AUTO_INCREMENT PRIMARY KEY,
    `user_id` INT,
    `book_id` INT,
    `last_page_read` INT,
    FOREIGN KEY (`user_id`) REFERENCES `users`(`user_id`),
    FOREIGN KEY (`book_id`) REFERENCES `books`(`book_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Optionally, indexes can be created to improve query performance on frequently accessed columns
CREATE INDEX `idx_users_age` ON `users`(`age`);
CREATE INDEX `idx_preferences_type` ON `preferences`(`story_type`);
CREATE INDEX `idx_books_name` ON `books`(`name`);
CREATE INDEX `idx_progress_last_read` ON `progress`(`last_page_read`);


/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
