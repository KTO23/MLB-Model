from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.teamrankings.com/mlb/stat/runs-per-game'
page = requests.get(url)
soup = BeautifulSoup(page.text, features="html.parser")

runs_per_game_table = soup.find('table')
runs_per_game_table_titles = runs_per_game_table.find_all('th')
just_table_titles = [title.text for title in runs_per_game_table_titles]
#print(just_table_titles)

team_runs_per_game_df = pd.DataFrame (columns = just_table_titles)
#print(df)


col_data = runs_per_game_table.find_all('tr')

for row in col_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text for data in row_data]
    length = len(team_runs_per_game_df)
    team_runs_per_game_df.loc[length] = individual_row_data

#print(team_runs_per_game_df)

