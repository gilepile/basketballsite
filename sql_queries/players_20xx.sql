CREATE TABLE `flaskTutorial`.`players_for_2017-18` (
  `index` INT NOT NULL AUTO_INCREMENT,
  `player_count` INT NULL,
  `first_name` VARCHAR(30) NULL,
  `last_name` VARCHAR(30) NULL,
  `player_id` INT NOT NULL,
  `team_id` INT NULL,
  `jersey` INT NULL,
  `pos` VARCHAR(6) NULL,
  `heightFeet` VARCHAR(20) NULL,
  `heightInches` VARCHAR(20) NULL,
  `heightMeters` VARCHAR(20) NULL,
  `weightPounds` VARCHAR(20) NULL,
  `weightKilograms` VARCHAR(20) NULL,
  `dateOfBirthUTC` VARCHAR(20) NULL,
  `nbaDebutYear` INT NULL,
  `yearsPro` INT NULL,
  `lastAffiliation` VARCHAR(60) NULL,
  `country` VARCHAR(60) NULL,
  PRIMARY KEY (`index`));
