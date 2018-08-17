CREATE TABLE `flaskTutorial`.`teams_player_played_for` (
  `index` INT NOT NULL AUTO_INCREMENT,
  `player_id` INT NOT NULL,
  `current_team_id` INT NOT NULL,
  `past_team_id` INT NULL,
  `seasonStart` INT NOT NULL,
  `seasonEnd` INT NOT NULL,
  PRIMARY KEY (`index`),
  UNIQUE INDEX `index_UNIQUE` (`index` ASC));
