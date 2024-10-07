-- Crear la base de datos 'sensor' si no existe
CREATE SCHEMA IF NOT EXISTS `sensor` DEFAULT CHARACTER SET latin1;

-- Usar la base de datos 'sensor'
USE `sensor`;

-- Crear la tabla 'bateria'
CREATE TABLE IF NOT EXISTS `sensor`.`bateria` (
  `idbateria` INT(11) NOT NULL AUTO_INCREMENT,
  `cargador` INT(1) NULL DEFAULT NULL,
  `carga` FLOAT NULL DEFAULT NULL,
  PRIMARY KEY (`idbateria`)
) ENGINE = InnoDB AUTO_INCREMENT = 36 DEFAULT CHARACTER SET = latin1;

-- Crear la tabla 'humedad'
CREATE TABLE IF NOT EXISTS `sensor`.`humedad` (
  `idhumedad` INT(11) NOT NULL AUTO_INCREMENT,
  `fecha` DATETIME NULL DEFAULT NULL,
  `valores` FLOAT NULL DEFAULT NULL,
  PRIMARY KEY (`idhumedad`)
) ENGINE = InnoDB AUTO_INCREMENT = 8 DEFAULT CHARACTER SET = latin1;
