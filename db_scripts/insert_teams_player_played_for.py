from db_model import db_model

import requests

table_record = []

endpoint = "http://data.nba.net/prod/v1/2018/players.json"

resp = requests.get(endpoint)
jsondata = resp.json()

numOfPlayers = len(jsondata["league"]["standard"])
print("number of players is: ", numOfPlayers)
i = 0
rowsInserted = 0
while (i < (numOfPlayers)):
    player_id = jsondata["league"]["standard"][i]["personId"]
    firstName = jsondata["league"]["standard"][i]["firstName"]
    lastName = jsondata["league"]["standard"][i]["lastName"]
    current_team_id = jsondata["league"]["standard"][i]["teamId"]
    pastTeams = jsondata["league"]["standard"][i]["teams"]

    numberOfPastTeams = len(pastTeams)

    if (jsondata["league"]["standard"][i]['isActive']):
                pastTeamCounter = 0

                while(pastTeamCounter < numberOfPastTeams):
                   team = db_model.Teams_player_played_for(player_id=jsondata["league"]["standard"][i]["personId"],
                                                           current_team_id=jsondata["league"]["standard"][i]["personId"],
                                                           past_team_id=jsondata["league"]["standard"][i]["teams"][pastTeamCounter]["teamId"],
                                                           seasonStart=jsondata["league"]["standard"][i]["teams"][pastTeamCounter]["seasonStart"],
                                                           seasonEnd=jsondata["league"]["standard"][i]["teams"][pastTeamCounter]["seasonEnd"]
                                                           )
                   db_model.db.session.add(team)
                   db_model.db.session.commit()
                   rowsInserted += 1
                   print("inserted player : ", player_id, firstName, lastName,
                         jsondata["league"]["standard"][i]["teams"][pastTeamCounter]["teamId"],
                         jsondata["league"]["standard"][i]["teams"][pastTeamCounter]["seasonStart"],
                         jsondata["league"]["standard"][i]["teams"][pastTeamCounter]["seasonEnd"]
                         )
                   pastTeamCounter = pastTeamCounter + 1
    i = i + 1

print("Number of rows inserted: ", rowsInserted)
