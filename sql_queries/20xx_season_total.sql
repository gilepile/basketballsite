CREATE TABLE `flaskTutorial`.`2018_season_totals` (
  `index` INT NOT NULL AUTO_INCREMENT,
  `player_count` INT NULL,
  `league_id` INT NULL,
  `season_id` VARCHAR(45) NOT NULL,
  `player_id` INT NOT NULL,
  `pos` VARCHAR(10) NULL,
  `first_name` VARCHAR(30) NULL,
  `last_name` VARCHAR(30) NULL,
  `team_id` INT NULL,
  `team_abbreviation` VARCHAR(45) NULL,
  `yearsPro` INT NULL,
  `player_age` INT NULL,
  `gp` INT NULL,
  `gs` INT NULL,
  `min` INT NULL,
  `fgm` INT NULL,
  `fga` INT NULL,
  `fg_pct` DECIMAL(4,3) NULL,
  `fg3m` INT NULL,
  `fg3a` INT NULL,
  `fg3_pct` DECIMAL(4,3) NULL,
  `ftm` INT NULL,
  `fta` INT NULL,
  `ft_pct` DECIMAL(4,3) NULL,
  `oreb` INT NULL,
  `dreb` INT NULL,
  `reb` INT NULL,
  `ast` INT NULL,
  `stl` INT NULL,
  `blk` INT NULL,
  `tov` INT NULL,
  `pf` INT NULL,
  `pts` INT NULL,
  PRIMARY KEY (`index`));
