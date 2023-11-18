-- ----------------------------------------------------------------------------
-- MySQL Workbench Migration
-- Migrated Schemata: banking
-- Source Schemata: banking
-- Created: Tue Feb  1 16:46:06 2022
-- Workbench Version: 8.0.27
-- ----------------------------------------------------------------------------

SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------------------------------------------------------
-- Schema banking
-- ----------------------------------------------------------------------------
DROP SCHEMA IF EXISTS `atm` ;
CREATE SCHEMA IF NOT EXISTS `atm` ;

-- ----------------------------------------------------------------------------
-- Table atm.clients_data
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `atm`.`clients_data` (
  `Name` VARCHAR(40) NOT NULL,
  `PIN` INT NULL DEFAULT NULL,
  `Balance` INT NULL DEFAULT NULL,
  PRIMARY KEY (`Name`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;
SET FOREIGN_KEY_CHECKS = 1;

INSERT INTO `atm`.`clients_data` VALUES ('Gatij Shakyawar',2911,5000);