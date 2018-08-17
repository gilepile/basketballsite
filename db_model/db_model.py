# importing flask module
from flask_sqlalchemy import SQLAlchemy

from  config import flask_config



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


class NBA_Teams(db.Model):
    __tablename__ = "nba_teams"

    index = db.Column(db.Integer, primary_key=True)
    teamId = db.Column(db.Integer)
    fullName = db.Column(db.String(40))
    nickname = db.Column(db.String(40))
    tricode = db.Column(db.String(40))



class Teams_player_played_for(db.Model):
    __tablename__ = "teams_player_played_for"

    index = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer)
    current_team_id = db.Column(db.Integer)
    past_team_id = db.Column(db.Integer)
    seasonStart = db.Column(db.Integer)
    seasonEnd = db.Column(db.Integer)
