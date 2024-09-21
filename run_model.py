#from model import *
from bs4 import BeautifulSoup
import requests
import pandas as pd

espn_to_teams_data_dict = {
    "Giants": "SF Giants",
    "Orioles": "Baltimore",
    "Diamondbacks": "Arizona",
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

espn_to_acr = {
    "Giants": "SFG",
    "Orioles": "BAL",
    "Diamondbacks": "ARI",
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
    #espn_url = "https://sports.yahoo.com/mlb/pittsburgh-pirates-cincinnati-reds-440921117/"
    #espn_url = "https://www.espn.com/mlb/game/_/gameId/401570791/pirates-reds"
    #espn_url = "https://www.foxsports.com/mlb/pittsburgh-pirates-vs-cincinnati-reds-sep-22-2024-game-boxscore-90550"
    espn_url = "https://www.espn.com/mlb/schedule/_/date/20240921"
    espn_page = requests.get(espn_url).text
    espn_soup = BeautifulSoup(espn_page, features="html.parser")

    #sorting data to find titles of table we want
    #home_team_espn = espn_soup.find('a', class_ = "ys-name Mb(4px) C(#fff)")
    #home_team_espn = espn_soup.find('a', class_ = "player-name fs-20 fs-sm-18")
    #name = home_team_espn.find("href")


    home_team_espn = espn_soup.find_all('table')
    print(home_team_espn)

    '''
    table_titles = [title.text for title in game_table_titles]

    #making dataframe with titles
    team_runs_per_game_df = pd.DataFrame (columns = table_titles)

    #sorting through table and putting data into our dataframe
    col_data = game_table.find_all('tr')
    for row in col_data[1:]:
        row_data = row.find_all('td')
        individual_row_data = [data.text for data in row_data]
        length = len(team_runs_per_game_df)
        team_runs_per_game_df.loc[length] = individual_row_data

    team_runs_per_game_df = team_runs_per_game_df.drop(['Rank'], axis=1)
    return(team_runs_per_game_df)
    '''

run_model()


#game_func(home_input="Tampa Bay", home_input_acr="TBR", home_input_starter="Tyler Alexander", away_input="Toronto", away_input_acr="TOR", away_input_starter="José Berríos")