#from model import *
from bs4 import BeautifulSoup
import requests
import pandas as pd
from model import *

from pitcher_data import *
from team_data import *
from refresh_data import *





br_to_teams_data_dict = {
    "Giants": "SF Giants",
    "Orioles": "Baltimore",
    "D'backs": "Arizona",
    "Rockies": "Colorado",
    "White Sox": "Chi Sox",
    "Angels": "LA Angels",
    "Athletics": "Oakland",
    "Cubs": "Chi Cubs",
    "Braves": "Atlanta",
    "Reds": "Cincinnati",
    "Astros": "Houston",
    "Padres": "San Diego",
    "Dodgers": "LA Dodgers",
    "Marlins": "Miami",
    "Twins": "Minnesota",
    "Guardians": "Cleveland",
    "Red Sox": "Boston",
    "Rays": "Tampa Bay",
    "Nationals": "Washington",
    "Mets": "NY Mets",
    "Tigers": "Detroit",
    "Royals": "Kansas City",
    "Phillies": "Philadelphia",
    "Brewers": "Milwaukee",
    "Pirates": "Pittsburgh",
    "Cardinals": "St. Louis",
    "Blue Jays": "Toronto",
    "Rangers": "Texas",
    "Yankees": "NY Yankees",
    "Mariners": "Seattle",
}

br_to_acr = {
    "Giants": "SFG",
    "Orioles": "BAL",
    "D'backs": "ARI",
    "Rockies": "COL",
    "White Sox": "CHW",
    "Angels": "LAA",
    "Athletics": "OAK",
    "Cubs": "CHC",
    "Braves": "ATL",
    "Reds": "CIN",
    "Astros": "HOU",
    "Padres": "SDP",
    "Dodgers": "LAD",
    "Marlins": "MIA",
    "Twins": "MIN",
    "Guardians": "CLE",
    "Red Sox": "BOS",
    "Rays": "TBR",
    "Nationals": "WSN",
    "Mets": "NYM",
    "Tigers": "DET",
    "Royals": "KCR",
    "Phillies": "PHI",
    "Brewers": "MIL",
    "Pirates": "PIT",
    "Cardinals": "STL",
    "Blue Jays": "TOR",
    "Rangers": "TEX",
    "Yankees": "NYY",
    "Mariners": "SEA",
}


def run_model():
    br_url = "https://www.baseball-reference.com/previews/"
    page = requests.get(br_url)
    soup = BeautifulSoup(page.text, features='html.parser')

    pitcher_data = refresh_pitcher_df()
    team_data = refresh_team_data_df()


    game_tables = soup.find_all('table', class_ = "teams")
    games_done = 0

    for games in game_tables:
        teams = games.find_all('a')
        team_names = [title.text for title in teams]

        away_team = team_names[0]
        home_team = team_names[2]

        temp = soup.find_all('table')[games_done + 1]
        temp2 = temp.find_all('a')
        pitcher_names = [title.text for title in temp2]
        away_starter = pitcher_names[0]
        home_starter = pitcher_names[1]
        games_done = games_done + 2

        home_acr = br_to_acr[home_team]
        away_acr = br_to_acr[away_team]

        home_team_dict = br_to_teams_data_dict[home_team]
        away_team_dict = br_to_teams_data_dict[away_team]

        game_func(input_pitcher_data=pitcher_data, input_team_data=team_data,home_input=home_team_dict, home_input_acr=home_acr, home_input_starter=home_starter, away_input=away_team_dict, away_input_acr=away_acr, away_input_starter=away_starter)


    #print(game_tables)

run_model()


#game_func(home_input="Tampa Bay", home_input_acr="TBR", home_input_starter="Tyler Alexander", away_input="Toronto", away_input_acr="TOR", away_input_starter="José Berríos")