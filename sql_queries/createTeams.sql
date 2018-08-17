CREATE TABLE `flaskTutorial`.`teams` (
  `index` INT NOT NULL AUTO_INCREMENT,
  `teamId` INT NOT NULL,
  `tricode` VARCHAR(45) NULL,
  `fullName` VARCHAR(45) NOT NULL,
  `nickname` VARCHAR(45) NULL,
  PRIMARY KEY (`index`));