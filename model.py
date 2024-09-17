import pandas as pd

pitcher_data = pitcher_df
#create func in pitcher_data.py
team_data = team_runs_per_game_df
#create func in team_data.py

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

for row in team_data:
    if team_data[Team][row] == home_team:
        home_team_rpg = team_data['2024'][row]
        home_team_rpg_last3 = team_data['Last 3'][row]
        home_team_rpg_at_home = team_data['Home'][row]
    elif team_data[Team][row] == away_team:
        away_team_rpg = team_data['2024'][row]
        away_team_rpg_last3 = team_data['Last 3'][row]
        away_team_rpg_while_away = team_data['Away'][row]
    