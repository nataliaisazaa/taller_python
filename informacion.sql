-- Adminer 4.7.3 MySQL dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

DROP DATABASE IF EXISTS `nada`;
CREATE DATABASE `nada` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `nada`;

DROP TABLE IF EXISTS `informacion`;
CREATE TABLE `informacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `ataque` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `informacion` (`id`, `nombre`, `ataque`) VALUES
(1,	'Pikachu',	120),
(2,	'Raichu',	145),
(3,	'Charmander',	110),
(4,	'Bulbasaur',	124),
(5,	'Ivysaur',	141),
(6,	'Venusaur',	171);

-- 2019-09-20 17:34:21
