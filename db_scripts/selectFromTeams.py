# importing flask module
from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, select, MetaData, Table, Column, Integer, String

# initializing a variable of Flask
app = Flask(__name__)

app.config["DEBUG"] = True

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{username}:{password}@{hostname}:{port}/{databasename}".format(
    username="root",
    password="tree",
    hostname="127.0.0.1",
    port="3306",
    databasename="flaskTutorial",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

engine = create_engine('mysql+pymysql://root:tree@localhost/flaskTutorial')


metadata = MetaData()
teams = Table('teams', metadata,
   Column('index', Integer, primary_key=True),
   Column('teamId', Integer),
   Column('tricode', String(50)),
   Column('fullname', String(50)),
   Column('nickname', String(12))
)

s = select([teams])
connection = engine.connect()

results = connection.execute(s)

for result in results:
    print(result)
    print("teamId: ", result.teamId, "fullName: ", result.fullname)
    print()







