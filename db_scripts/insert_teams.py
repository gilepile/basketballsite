from db_model import db_model

import requests

team = []

endpoint = "http://data.nba.net/prod/v1/2018/teams.json"

resp = requests.get(endpoint)
jsondata = resp.json()

numOfItems = len(jsondata["league"]["standard"])
print("number of items is: ", numOfItems)
i=0
numberOfTeams = 0
while (i < numOfItems):
  if jsondata["league"]["standard"][i]['isNBAFranchise']:

    team = db_model.NBA_Teams(teamId=jsondata["league"]["standard"][i]["teamId"],
                              tricode=jsondata["league"]["standard"][i]["tricode"],
                              fullName=jsondata["league"]["standard"][i]["fullName"],
                              nickname=jsondata["league"]["standard"][i]["nickname"])
    db_model.db.session.add(team)
    db_model.db.session.commit()
    print("Added: ", team.fullName)

    numberOfTeams+=1
  i = i +1

print("Number of teams added: ", numberOfTeams)


