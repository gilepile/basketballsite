# importing flask module
from flask_sqlalchemy import SQLAlchemy

from config import db_scripts_config
from config import flask_config




SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{username}:{password}@{hostname}:{port}/{databasename}".format(
    username="root",
    password="tree",
    hostname="127.0.0.1",
    port="3306",
    databasename="flaskTutorial",
)


flask_config.app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
flask_config.app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
flask_config.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(flask_config.app)

#define here for easier table creation


class NBA_Teams(db.Model):
    __tablename__ = "nba_teams"

    index = db.Column(db.Integer, primary_key=True)
    teamId = db.Column(db.Integer)
    fullName = db.Column(db.String(40))
    nickname = db.Column(db.String(40))
    tricode = db.Column(db.String(40))


class players_for_20xx_season(db.Model):
    __tablename__ = "players_for_" + db_scripts_config.season

    index = db.Column(db.Integer, primary_key=True)
    player_count = db.Column(db.Integer)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    player_id = db.Column(db.Integer)
    team_id = db.Column(db.Integer)
    jersey = db.Column(db.Integer)
    pos = db.Column(db.String(10))
    heightFeet = db.Column(db.String(20))
    heightInches = db.Column(db.String(20))
    heightMeters = db.Column(db.String(20))
    weightPounds = db.Column(db.String(20))
    weightKilograms = db.Column(db.String(20))
    dateOfBirthUTC = db.Column(db.String(30))
    nbaDebutYear = db.Column(db.Integer)
    yearsPro = db.Column(db.Integer)
    lastAffiliation = db.Column(db.String(60))
    country = db.Column(db.String(60))

class Teams_player_played_for(db.Model):
    __tablename__ = "teams_player_played_for"

    index = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer)
    current_team_id = db.Column(db.Integer)
    past_team_id = db.Column(db.Integer)
    seasonStart = db.Column(db.Integer)
    seasonEnd = db.Column(db.Integer)

class player_season_per_game(db.Model):
    __tablename__ = db_scripts_config.season_start + "_season_per_game"

    index = db.Column(db.Integer, primary_key=True)
    player_count = db.Column(db.Integer)
    league_id = db.Column(db.Integer)
    season_id = db.Column(db.String(20))
    player_id = db.Column(db.Integer)
    pos = db.Column(db.String(10))
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    team_id = db.Column(db.Integer)
    team_abbreviation = db.Column(db.String(4))
    yearsPro = db.Column(db.Integer)
    player_age = db.Column(db.Integer)
    gp = db.Column(db.Integer)
    gs = db.Column(db.Integer)
    min = db.Column(db.Float(4, 2))
    fga = db.Column(db.Float(4, 2))
    fgm = db.Column(db.Float(4, 2))
    fg_pct = db.Column(db.Float(4, 3))
    fg3m = db.Column(db.Float(4, 2))
    fg3a = db.Column(db.Float(4, 2))
    fg3_pct = db.Column(db.Float(4, 3))
    ftm = db.Column(db.Float(4, 2))
    fta = db.Column(db.Float(4, 2))
    ft_pct = db.Column(db.Float(4, 2))
    oreb = db.Column(db.Float(4, 2))
    dreb = db.Column(db.Float(4, 2))
    reb = db.Column(db.Float(4, 2))
    ast = db.Column(db.Float(4, 2))
    stl = db.Column(db.Float(4, 2))
    blk = db.Column(db.Float(4, 2))
    tov = db.Column(db.Float(4, 2))
    pf = db.Column(db.Float(4, 2))
    pts = db.Column(db.Float(4, 2))


class player_season_totals(db.Model):
    __tablename__ = db_scripts_config.season_start + "_season_totals"

    index = db.Column(db.Integer, primary_key=True)
    player_count = db.Column(db.Integer)
    league_id = db.Column(db.Integer)
    season_id = db.Column(db.String(20))
    player_id = db.Column(db.Integer)
    pos = db.Column(db.String(10))
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    team_id = db.Column(db.Integer)
    team_abbreviation = db.Column(db.String(4))
    yearsPro = db.Column(db.Integer)
    player_age = db.Column(db.Integer)
    gp = db.Column(db.Integer)
    gs = db.Column(db.Integer)
    min = db.Column(db.Integer)
    fga = db.Column(db.Integer)
    fgm = db.Column(db.Integer)
    fg_pct = db.Column(db.Float(4, 3))
    fg3m = db.Column(db.Integer)
    fg3a = db.Column(db.Integer)
    fg3_pct = db.Column(db.Float(4, 3))
    ftm = db.Column(db.Integer)
    fta = db.Column(db.Integer)
    ft_pct = db.Column(db.Float(4, 3))
    oreb = db.Column(db.Integer)
    dreb = db.Column(db.Integer)
    reb = db.Column(db.Integer)
    ast = db.Column(db.Integer)
    stl = db.Column(db.Integer)
    blk = db.Column(db.Integer)
    tov = db.Column(db.Integer)
    pf = db.Column(db.Integer)
    pts = db.Column(db.Integer)




















