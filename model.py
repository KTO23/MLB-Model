import pandas as pd
from pitcher_data import *
from team_data import *
from refresh_data import *

pitcher_data = refresh_pitcher_df()
team_data = refresh_team_data_df()


#pitcher_data = get_stored_pitcher_df()
#team_data = get_stored_team_df()


#print(pitcher_data)
print(team_data)



def game_func():
    home_team = "Arizona"
    away_team = "Boston"
    home_team_pitcher = "Chris Sale"
    away_team_pitcher = ""


    home_team_rpg = 0
    home_team_rpg_last3 = 0
    home_team_rpg_at_home = 0
    away_team_rpg = 0
    away_team_rpg_last3 = 0
    away_team_rpg_while_away = 0

    for index,row in team_data.iterrows():
        if row['Team'] == home_team:
            home_team_rpg = team_data['2024'][index]
            home_team_rpg_last3 = team_data['Last 3'][index]
            home_team_rpg_at_home = team_data['Home'][index]
        elif row['Team'] == away_team:
            away_team_rpg = team_data['2024'][index]
            away_team_rpg_last3 = team_data['Last 3'][index]
            away_team_rpg_while_away = team_data['Home'][index]
    

    home_pitcher

game_func()