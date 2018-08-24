from db_model import db_model
from helpers import  request_helper

import requests

table_record = []

endpoint_players = "http://data.nba.net/prod/v1/2018/players.json"
season = "2017-18"

resp_players = requests.get(endpoint_players)
jsondata_players = resp_players.json()

numOfPlayers = len(jsondata_players["league"]["standard"])
print("Number of players is: ", numOfPlayers)
global player_id

endpoint_per_game = "https://stats.nba.com/stats/playercareerstats"

i = 0
rowsInserted = 0
counter = 0

while (i < numOfPlayers):
    player_id = jsondata_players["league"]["standard"][i]["personId"]
    first_name = jsondata_players["league"]["standard"][i]["firstName"]
    last_name = jsondata_players["league"]["standard"][i]["lastName"]
    pos = jsondata_players["league"]["standard"][i]["pos"]

    if ( len(jsondata_players["league"]["standard"][i]["yearsPro"]) > 0):
        yearsPro = jsondata_players["league"]["standard"][i]["yearsPro"]
    else:
        yearsPro = 0

    parameters_per_game = {'PerMode': "PerGame", 'playerID': player_id}

    resp_per_game = requests.get(endpoint_per_game, headers = request_helper.request_headers, params = parameters_per_game)
    if(resp_per_game.status_code == 200):
        print("index: ", i,
              "For player with playerID: ", player_id, " ",
              jsondata_players["league"]["standard"][i]["firstName"],
              jsondata_players["league"]["standard"][i]["lastName"]
              )
    jsondata_per_game = resp_per_game.json()

    results_set_length = len(jsondata_per_game["resultSets"])

    #get first result set, it should have value of "SeasonTotalsRegularSeason",
    result_set_zero_name = (jsondata_per_game["resultSets"][0]["name"])
    if(result_set_zero_name == "SeasonTotalsRegularSeason"):
        rowSet_length = len(jsondata_per_game["resultSets"][0]["rowSet"])

        if (rowSet_length > 0):

            j = 0
            season_position = 0

            while j < rowSet_length:
                if (jsondata_per_game["resultSets"][0]["rowSet"][j][1] == season):
                    season_position = j
                j += 1

            season_data_row = jsondata_per_game["resultSets"][0]["rowSet"][season_position]

            season_id_from_response = season_data_row[1]

            player_row = db_model.player_season_per_game(
                    player_count = counter,
                    league_id = season_data_row[2],
                    season_id = season_data_row[1],
                    player_id = season_data_row[0],
                    pos = pos,
                    first_name = first_name,
                    last_name = last_name,
                    team_id = season_data_row[3],
                    team_abbreviation= season_data_row[4],
                    yearsPro = yearsPro,
                    player_age = season_data_row[5],
                    gp = season_data_row[6],
                    gs = season_data_row[7],
                    min = season_data_row[8],
                    fgm = season_data_row[9],
                    fga = season_data_row[10],
                    fg_pct = season_data_row[11],
                    fg3m = season_data_row[12],
                    fg3a = season_data_row[13],
                    fg3_pct = season_data_row[14],
                    ftm = season_data_row[15],
                    fta = season_data_row[16],
                    ft_pct = season_data_row[17],
                    oreb = season_data_row[18],
                    dreb = season_data_row[19],
                    reb = season_data_row[20],
                    ast = season_data_row[21],
                    stl = season_data_row[22],
                    blk = season_data_row[23],
                    tov = season_data_row[24],
                    pf = season_data_row[25],
                    pts = season_data_row[26]
            )

            if (season_id_from_response == season):
                db_model.db.session.add(player_row)
                db_model.db.session.commit()
                counter += 1

    i = i + 1