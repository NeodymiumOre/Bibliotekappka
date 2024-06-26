-- MySQL Script generated by MySQL Workbench
-- wto, 5 kwi 2022, 18:47:33
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema Library
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `Library` ;

-- -----------------------------------------------------
-- Schema Library
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Library` ;
USE `Library` ;

-- -----------------------------------------------------
-- Table `Library`.`Autorzy`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Library`.`Autorzy` ;

CREATE TABLE IF NOT EXISTS `Library`.`Autorzy` (
  `Id_autora` INT NOT NULL AUTO_INCREMENT,
  `Imię` VARCHAR(20) NOT NULL,
  `Nazwisko` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`Id_autora`),
  INDEX `Idx_Imię_Nazwisko` (`Imię` ASC, `Nazwisko` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Library`.`Książki`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Library`.`Książki` ;

CREATE TABLE IF NOT EXISTS `Library`.`Książki` (
  `Id_książki` INT NOT NULL,
  `Tytuł` VARCHAR(100) NOT NULL,
  `ISBN` VARCHAR(14) NULL,
  `Rok_wydania` YEAR(4) NULL,
  PRIMARY KEY (`Id_książki`),
  INDEX `Idx_Tytuł` (`Tytuł` ASC) VISIBLE,
  INDEX `Idx_ISBN` (`ISBN` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Library`.`Kategorie`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Library`.`Kategorie` ;

CREATE TABLE IF NOT EXISTS `Library`.`Kategorie` (
  `Id_kategorii` INT NOT NULL,
  `Nazwa_kategorii` VARCHAR(30) NOT NULL,
  PRIMARY KEY (`Id_kategorii`),
  INDEX `Idx_Nazwa_kategorii` (`Nazwa_kategorii` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Library`.`Wydawnictwa`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Library`.`Wydawnictwa` ;

CREATE TABLE IF NOT EXISTS `Library`.`Wydawnictwa` (
  `Id_wydawnictwa` INT NOT NULL AUTO_INCREMENT,
  `Nazwa_wydawnictwa` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Id_wydawnictwa`),
  INDEX `Idx_Nazwa_wydawnictwa` (`Nazwa_wydawnictwa` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Library`.`Egzemplarze`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Library`.`Egzemplarze` ;

CREATE TABLE IF NOT EXISTS `Library`.`Egzemplarze` (
  `Id_egzemplarza` INT NOT NULL,
  `Id_książki` INT NOT NULL,
  `Id_wydawnictwa` INT NOT NULL,
  `Dostępny` INT NOT NULL,
  PRIMARY KEY (`Id_egzemplarza`),
  INDEX `Idx_Id_książki` (`Id_książki` ASC) VISIBLE,
  INDEX `Idx_Id_wydawnictwa` (`Id_wydawnictwa` ASC) VISIBLE,
  INDEX `Idx_Dostępny` (`Dostępny` ASC) VISIBLE,
  CONSTRAINT `FK_Książki_IN_Egzemplarze`
    FOREIGN KEY (`Id_książki`)
    REFERENCES `Library`.`Książki` (`Id_książki`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `FK_Wydawnictwa_IN_Egzemplarze`
    FOREIGN KEY (`Id_wydawnictwa`)
    REFERENCES `Library`.`Wydawnictwa` (`Id_wydawnictwa`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Library`.`Adresy`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Library`.`Adresy` ;

CREATE TABLE IF NOT EXISTS `Library`.`Adresy` (
  `id_adresu` INT NOT NULL,
  `Miasto` VARCHAR(20) NOT NULL,
  `Kod_pocztowy` VARCHAR(7) NOT NULL,
  `Ulica` VARCHAR(30) NOT NULL,
  `Numer` INT NOT NULL,
  PRIMARY KEY (`id_adresu`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Library`.`Osoby`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Library`.`Osoby` ;

CREATE TABLE IF NOT EXISTS `Library`.`Osoby` (
  `Id_osoby` INT NOT NULL,
  `Imię` VARCHAR(20) NOT NULL,
  `Nazwisko` VARCHAR(20) NOT NULL,
  `Id_adresu` INT NOT NULL,
  `Telefon` VARCHAR(10) NOT NULL,
  `Email` VARCHAR(45) NULL,
  PRIMARY KEY (`Id_osoby`),
  INDEX `Idx_Imię_Nazwisko` (`Imię` ASC, `Nazwisko` ASC) VISIBLE,
  INDEX `Idx_Id_adresu` (`Id_adresu` ASC) VISIBLE,
  CONSTRAINT `FK_Adresy_IN_Osoby`
    FOREIGN KEY (`Id_adresu`)
    REFERENCES `Library`.`Adresy` (`id_adresu`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Library`.`Czytelnicy`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Library`.`Czytelnicy` ;

CREATE TABLE IF NOT EXISTS `Library`.`Czytelnicy` (
  `Id_karty` INT NOT NULL,
  `Id_osoby` INT NOT NULL,
  PRIMARY KEY (`Id_karty`),
  INDEX `Idx_Id_osoby` (`Id_osoby` ASC) VISIBLE,
  CONSTRAINT `FK_Osoby_IN_Czytelnicy`
    FOREIGN KEY (`Id_osoby`)
    REFERENCES `Library`.`Osoby` (`Id_osoby`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Library`.`Bibliotekarze`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Library`.`Bibliotekarze` ;

CREATE TABLE IF NOT EXISTS `Library`.`Bibliotekarze` (
  `Id_bibliotekarza` INT NOT NULL,
  `Id_osoby` INT NOT NULL,
  `Login` VARCHAR(20) NOT NULL,
  `Hasło` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`Id_bibliotekarza`),
  INDEX `Idx_Id_osoby` (`Id_osoby` ASC) VISIBLE,
  CONSTRAINT `FK_Osoby_IN_Bibliotekarze`
    FOREIGN KEY (`Id_osoby`)
    REFERENCES `Library`.`Osoby` (`Id_osoby`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Library`.`Wypożyczenia`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Library`.`Wypożyczenia` ;

CREATE TABLE IF NOT EXISTS `Library`.`Wypożyczenia` (
  `Id_wypożyczenia` INT NOT NULL,
  `Id_karty` INT NOT NULL,
  `Id_bibliotekarza` INT NOT NULL,
  `Id_egzemplarza` INT NOT NULL,
  `Data_wypożyczenia` DATE NOT NULL,
  `Termin_oddania` DATE NULL,
  PRIMARY KEY (`Id_wypożyczenia`),
  INDEX `Idx_Id_karty` (`Id_karty` ASC) VISIBLE,
  INDEX `Idx_Id_bibliotekarza` (`Id_bibliotekarza` ASC) VISIBLE,
  INDEX `Idx_Id_egzemplarza` (`Id_egzemplarza` ASC) VISIBLE,
  CONSTRAINT `FK_Egzemplarze_IN_Wypożyczenia`
    FOREIGN KEY (`Id_egzemplarza`)
    REFERENCES `Library`.`Egzemplarze` (`Id_egzemplarza`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `FK_Czytelnicy_IN_Wypożyczenia`
    FOREIGN KEY (`Id_karty`)
    REFERENCES `Library`.`Czytelnicy` (`Id_karty`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `FK_Bibliotekarze_IN_Wypożyczenia`
    FOREIGN KEY (`Id_bibliotekarza`)
    REFERENCES `Library`.`Bibliotekarze` (`Id_bibliotekarza`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Library`.`Rezerwacje`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Library`.`Rezerwacje` ;

CREATE TABLE IF NOT EXISTS `Library`.`Rezerwacje` (
  `Id_rezerwacji` INT NOT NULL,
  `Id_książki` INT NOT NULL,
  `Id_karty` INT NOT NULL,
  `Numer_w_kolejce` INT NOT NULL,
  PRIMARY KEY (`Id_rezerwacji`),
  INDEX `Idx_Id_książki` (`Id_książki` ASC) VISIBLE,
  INDEX `Idx_Id_karty` (`Id_karty` ASC) VISIBLE,
  CONSTRAINT `FK_Książki_IN_Rezerwacje`
    FOREIGN KEY (`Id_książki`)
    REFERENCES `Library`.`Książki` (`Id_książki`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `FK_Czytelnicy_IN_Rezerwacje`
    FOREIGN KEY (`Id_karty`)
    REFERENCES `Library`.`Czytelnicy` (`Id_karty`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Library`.`Książki_has_Autorzy`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Library`.`Książki_has_Autorzy` ;

CREATE TABLE IF NOT EXISTS `Library`.`Książki_has_Autorzy` (
  `Id_książki` INT NOT NULL,
  `Id_autora` INT NOT NULL,
  PRIMARY KEY (`Id_książki`, `Id_autora`),
  INDEX `Idx_Id_autora` (`Id_autora` ASC) VISIBLE,
  INDEX `Idx_Id_książki` (`Id_książki` ASC) VISIBLE,
  CONSTRAINT `FK_Książki_IN_Książki_has_Autorzy`
    FOREIGN KEY (`Id_książki`)
    REFERENCES `Library`.`Książki` (`Id_książki`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `FK_Autorzy_IN_Książki_has_Autorzy`
    FOREIGN KEY (`Id_autora`)
    REFERENCES `Library`.`Autorzy` (`Id_autora`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Library`.`Książki_has_Kategorie`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Library`.`Książki_has_Kategorie` ;

CREATE TABLE IF NOT EXISTS `Library`.`Książki_has_Kategorie` (
  `Id_książki` INT NOT NULL,
  `Id_kategorii` INT NOT NULL,
  PRIMARY KEY (`Id_książki`, `Id_kategorii`),
  INDEX `Idx_Id_kategorii` (`Id_kategorii` ASC) VISIBLE,
  INDEX `Idx_Id_książki` (`Id_książki` ASC) VISIBLE,
  CONSTRAINT `FK_Książki_IN_Książki_has_Kategorie`
    FOREIGN KEY (`Id_książki`)
    REFERENCES `Library`.`Książki` (`Id_książki`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `FK_Kategorie_IN_Książki_has_Kategorie`
    FOREIGN KEY (`Id_kategorii`)
    REFERENCES `Library`.`Kategorie` (`Id_kategorii`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

USE `Library` ;

-- -----------------------------------------------------
-- Placeholder table for view `Library`.`Wyszukaj`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Library`.`Wyszukaj` (`Tytuł` INT, `Rok_wydania` INT, `Dostępny` INT, `Imię` INT, `Nazwisko` INT);

-- -----------------------------------------------------
-- Placeholder table for view `Library`.`Zarezerwowane`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Library`.`Zarezerwowane` (`Tytuł` INT, `Numer_w_kolejce` INT, `Id_karty` INT, `Imię` INT, `Nazwisko` INT, `Email` INT);

-- -----------------------------------------------------
-- Placeholder table for view `Library`.`Wypozyczone`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Library`.`Wypozyczone` (`Tytuł` INT, `Id_egzemplarza` INT, `Data_wypożyczenia` INT, `Termin_oddania` INT, `Id_bibliotekarza` INT, `Id_karty` INT, `Imię` INT, `Nazwisko` INT, `Telefon` INT);

-- -----------------------------------------------------
-- View `Library`.`Wyszukaj`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Library`.`Wyszukaj`;
DROP VIEW IF EXISTS `Library`.`Wyszukaj` ;
USE `Library`;
CREATE  OR REPLACE VIEW `Wyszukaj` AS
SELECT K.Tytuł, K.Rok_wydania, E.Dostępny, A.Imię, A.Nazwisko
FROM Książki AS K INNER JOIN Egzemplarze AS E INNER JOIN Autorzy AS A;

-- -----------------------------------------------------
-- View `Library`.`Zarezerwowane`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Library`.`Zarezerwowane`;
DROP VIEW IF EXISTS `Library`.`Zarezerwowane` ;
USE `Library`;
CREATE  OR REPLACE VIEW `Zarezerwowane` AS
SELECT K.Tytuł, R.Numer_w_kolejce, C.Id_karty, O.Imię, O.Nazwisko, O.Email
FROM Książki AS K INNER JOIN Rezerwacje AS R INNER JOIN Czytelnicy AS C INNER JOIN Osoby AS O;

-- -----------------------------------------------------
-- View `Library`.`Wypozyczone`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Library`.`Wypozyczone`;
DROP VIEW IF EXISTS `Library`.`Wypozyczone` ;
USE `Library`;
CREATE  OR REPLACE VIEW `Wypozyczone` AS
SELECT K.Tytuł, E.Id_egzemplarza, W.Data_wypożyczenia, W.Termin_oddania, W.Id_bibliotekarza, C.Id_karty, O.Imię, O.Nazwisko, O.Telefon
FROM Książki AS K INNER JOIN Wypożyczenia AS W INNER JOIN Czytelnicy AS C INNER JOIN Osoby AS O INNER JOIN Egzemplarze AS E;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
