import pandas as pd
from pitcher_data import *
from team_data import *
from refresh_data import *
import math

pitcher_data = refresh_pitcher_df()
team_data = refresh_team_data_df()


#pitcher_data = get_stored_pitcher_df()
#team_data = get_stored_team_df()


#print(pitcher_data.head())
#print(team_data)



def game_func():
    home_team = "Seattle"
    home_team_acr = "SEA"
    away_team = "NY Yankees"
    away_team_acr = "NYY"
    home_team_pitcher = "Bryan Woo"
    away_team_pitcher = "Luis Gil"


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
    

    home_pitcher_era = 0
    home_pitcher_IP = 0
    home_pitcher_starts = 0
    home_pitcher_avg_IP_per_start = 0

    away_pitcher_era = 0
    away_pitcher_IP = 0
    away_pitcher_starts = 0
    away_pitcher_avg_IP_per_start = 0

    for index,row in pitcher_data.iterrows():
        if row['Name'] == home_team_pitcher:
            home_pitcher_era = float(pitcher_data['ERAERA - Earned Run Average ((ER*9)/IP)'][index])
            home_pitcher_IP = float(pitcher_data['IPIP - Innings Pitched'][index])
            temp_IP_floored = math.floor(home_pitcher_IP)
            temp_IP_difference = home_pitcher_IP - temp_IP_floored
            extra_outs = 0
            if(temp_IP_difference == 0.1):
                extra_outs = 1
            elif(temp_IP_difference == 0.2):
                extra_outs = 2
            home_pitcher_starts = float(pitcher_data['GSGS - Games Started'][index])
            home_pitcher_IP = ((temp_IP_floored * 3) + extra_outs)/3
            home_pitcher_avg_IP_per_start = home_pitcher_IP/home_pitcher_starts
        elif row['Name'] == away_team_pitcher:
            away_pitcher_era = float(pitcher_data['ERAERA - Earned Run Average ((ER*9)/IP)'][index])
            away_pitcher_IP = float(pitcher_data['IPIP - Innings Pitched'][index])
            temp_IP_floored = math.floor(away_pitcher_IP)
            temp_IP_difference = away_pitcher_IP - temp_IP_floored
            extra_outs = 0
            if(temp_IP_difference == 0.1):
                extra_outs = 1
            elif(temp_IP_difference == 0.2):
                extra_outs = 2
            away_pitcher_starts = float(pitcher_data['GSGS - Games Started'][index])
            away_pitcher_IP = ((temp_IP_floored * 3) + extra_outs)/3
            away_pitcher_avg_IP_per_start = away_pitcher_IP/away_pitcher_starts

    home_pitcher_avg_outs_per_start = int(round(home_pitcher_avg_IP_per_start*3))
    away_pitcher_avg_outs_per_start = int(round(away_pitcher_avg_IP_per_start*3))





    temp_home_reliever_ERA = 0
    temp_home_reliever_IP = 0
    temp_home_reliever_ER = 0
    home_pitcher_relievers_outs = 0
    home_pitcher_relievers_ER = 0

    temp_away_reliever_ERA = 0
    temp_away_reliever_IP = 0
    temp_away_reliever_ER = 0
    away_pitcher_relievers_outs = 0
    away_pitcher_relievers_ER = 0

    for index,row in pitcher_data.iterrows():
        temp_pitcher_relievers_outs = 0
        temp_home_reliever_ERA = 0
        temp_home_reliever_IP = 0
        temp_home_reliever_ER = 0
        temp_away_reliever_ERA = 0
        temp_away_reliever_IP = 0
        temp_away_reliever_ER = 0

        if row['Team'] == home_team_acr:
            temp_games = float(pitcher_data['GG - Games Pitched'][index])
            temp_starts = float(pitcher_data['GSGS - Games Started'][index])
            percent_starts = temp_starts/temp_games
            
            if percent_starts < 0.5:
                temp_home_reliever_ERA = float(pitcher_data['ERAERA - Earned Run Average ((ER*9)/IP)'][index])
                temp_home_reliever_IP = float(pitcher_data['IPIP - Innings Pitched'][index])

                temp_IP_floored = math.floor(temp_home_reliever_IP)
                temp_IP_difference = temp_home_reliever_IP - temp_IP_floored
                extra_outs = 0
                if(temp_IP_difference == 0.1):
                    extra_outs = 1
                elif(temp_IP_difference == 0.2):
                    extra_outs = 2

                temp_pitcher_relievers_outs = (temp_IP_floored * 3) + extra_outs
                
                temp_home_reliever_ER = int(round(((temp_home_reliever_ERA/9) * float(home_pitcher_relievers_outs/3))))
                home_pitcher_relievers_ER = home_pitcher_relievers_ER + temp_home_reliever_ER
                home_pitcher_relievers_outs = home_pitcher_relievers_outs + temp_pitcher_relievers_outs


        elif row['Team'] == away_team_acr:
            temp_games = float(pitcher_data['GG - Games Pitched'][index])
            temp_starts = float(pitcher_data['GSGS - Games Started'][index])
            percent_starts = temp_starts/temp_games
            
            if percent_starts < 0.5:
                temp_away_reliever_ERA = float(pitcher_data['ERAERA - Earned Run Average ((ER*9)/IP)'][index])
                temp_away_reliever_IP = float(pitcher_data['IPIP - Innings Pitched'][index])

                temp_IP_floored = math.floor(temp_away_reliever_IP)
                temp_IP_difference = temp_away_reliever_IP - temp_IP_floored
                extra_outs = 0
                if(temp_IP_difference == 0.1):
                    extra_outs = 1
                elif(temp_IP_difference == 0.2):
                    extra_outs = 2

                temp_pitcher_relievers_outs = (temp_IP_floored * 3) + extra_outs
                
                temp_away_reliever_ER = int(round(((temp_away_reliever_ERA/9) * float(away_pitcher_relievers_outs/3))))
                away_pitcher_relievers_ER = away_pitcher_relievers_ER + temp_away_reliever_ER
                away_pitcher_relievers_outs = away_pitcher_relievers_outs + temp_pitcher_relievers_outs


    home_relievers_outs_needed = 27 - home_pitcher_avg_outs_per_start
    away_relievers_outs_needed = 27 - away_pitcher_avg_outs_per_start

    home_relievers_era = home_pitcher_relievers_ER / float(home_pitcher_relievers_outs/3)
    away_relievers_era = away_pitcher_relievers_ER / float(away_pitcher_relievers_outs/3)

    expected_runs_home_starter = (home_pitcher_era/9) * float(home_pitcher_avg_outs_per_start/3)
    expected_runs_away_starter = (away_pitcher_era/9) * float(away_pitcher_avg_outs_per_start/3)

    expected_runs_home_relievers = (home_relievers_era/9) * float(home_relievers_outs_needed/3)
    expected_runs_away_relievers = (away_relievers_era/9) * float(away_relievers_outs_needed/3)

    expected_home_team_runs_allowed = expected_runs_home_starter + expected_runs_home_relievers
    expected_away_team_runs_allowed = expected_runs_away_starter + expected_runs_away_relievers
    expected_total_from_runs_allowed = expected_home_team_runs_allowed + expected_away_team_runs_allowed

    expected_total_from_rpg = float(home_team_rpg) + float(away_team_rpg)

    print("Expected home team runs allowed: " + str(expected_home_team_runs_allowed))
    print("Expected away team runs allowed: " + str(expected_away_team_runs_allowed))
    print("Expected total from runs allowed: " + str(expected_total_from_runs_allowed))
    print()
    print("Home team runs per game: " + str(home_team_rpg))
    print("Away team runs per game: " + str(away_team_rpg))
    print("Expected total from runs per game: " + str(expected_total_from_rpg))


game_func()