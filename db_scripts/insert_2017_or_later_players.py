from config import end_points
from db_model import db_model

import requests

#  this will work only for 2017-18 season or later
#  earlier seasons do not have "isActive" key
#
table_record = []

endpoint_players = end_points.players_for_season

resp_players = requests.get(endpoint_players)
jsondata_players = resp_players.json()

numOfPlayers = len(jsondata_players["league"]["standard"])
print("Number of players is: ", numOfPlayers)
global player_id

endpoint_per_game = end_points.player_stats

i = 0
rowsInserted = 0
counter = 0

while i < numOfPlayers:
    first_name = jsondata_players["league"]["standard"][i]["firstName"]
    last_name = jsondata_players["league"]["standard"][i]["lastName"]
    player_id = jsondata_players["league"]["standard"][i]["personId"]
    team_id = jsondata_players["league"]["standard"][i]["teamId"]
    if team_id != "":
        team_id = team_id
    else:
        team_id = None

    jersey = jsondata_players["league"]["standard"][i]["jersey"]
    if jersey != "":
        jersey = jersey
    else:
        jersey = None

    pos = jsondata_players["league"]["standard"][i]["pos"]

    heightFeet = jsondata_players["league"]["standard"][i]["heightFeet"]
    if heightFeet != "-":
        heightFeet = heightFeet
    else:
        heightFeet = 0

    heightInches = jsondata_players["league"]["standard"][i]["heightInches"]
    if heightInches != "-":
        heightInches = heightInches
    else:
        heightInches = 0

    heightMeters = jsondata_players["league"]["standard"][i]["heightMeters"]
    if heightMeters != "":
        heightMeters = heightMeters
    else:
        heightMeters = 0

    weightPounds = jsondata_players["league"]["standard"][i]["weightPounds"]
    if weightPounds != "":
        weightPounds = weightPounds
    else:
        weightPounds = 0

    weightKilograms = jsondata_players["league"]["standard"][i]["weightKilograms"]
    if weightKilograms != "":
        weightKilograms = weightKilograms
    else:
        weightKilograms = 0

    dateOfBirthUTC = jsondata_players["league"]["standard"][i]["dateOfBirthUTC"]
    if dateOfBirthUTC != "":
        dateOfBirthUTC = dateOfBirthUTC
    else:
        dateOfBirthUTC = None

    nbaDebutYear = jsondata_players["league"]["standard"][i]["nbaDebutYear"]
    if nbaDebutYear != "":
        nbaDebutYear = nbaDebutYear
    else:
        nbaDebutYear = 0

    yearsPro = jsondata_players["league"]["standard"][i]["yearsPro"]

    if yearsPro != "":
        yearsPro = yearsPro
    else:
        yearsPro = 0

    lastAffiliation = jsondata_players["league"]["standard"][i]["lastAffiliation"]
    country = jsondata_players["league"]["standard"][i]["country"]

    if jsondata_players["league"]["standard"][i]["isActive"]:
        player_row = db_model.players_for_20xx_season(
            player_count=counter,
            first_name=first_name,
            last_name=last_name,
            player_id=player_id,
            team_id=team_id,
            jersey=jersey,
            pos=pos,
            heightFeet=heightFeet,
            heightInches=heightInches,
            heightMeters=heightMeters,
            weightPounds=weightPounds,
            weightKilograms=weightKilograms,
            dateOfBirthUTC=dateOfBirthUTC,
            nbaDebutYear=nbaDebutYear,
            yearsPro=yearsPro,
            lastAffiliation=lastAffiliation,
            country=country
        )

        db_model.db.session.add(player_row)
        db_model.db.session.commit()
        counter += 1

        print("index: ", i,
              "For player with playerID: ", player_id, " ",
              jsondata_players["league"]["standard"][i]["firstName"],
              jsondata_players["league"]["standard"][i]["lastName"]
              )
    i += 1
