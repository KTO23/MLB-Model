from bs4 import BeautifulSoup
import requests
import pandas as pd


#old url - table in html not working
#url2 = 'https://razzball.com/mlbpitchingstats/'
#page2 = requests.get(url2)
#soup2 = BeautifulSoup(page2.text, features="html.parser")

def get_current_odds_data_func():
    url = 'https://sportsbook.draftkings.com/leagues/baseball/mlb'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, features='html.parser')

    #sorts html to find the table titles - used to put into our dataframe
    games_table = soup.find_all('table')[0]
    #print(games_table)
    temp = games_table.find('tr')
    labels = temp.find_all('th')
    column_titles = [title.text for title in labels]
    column_titles[0] = "Team"
    oddsdf = pd.DataFrame(columns=column_titles)

    #print(column_titles)
    col_data = games_table.find_all('tr')

    for row in col_data:
        row_data = row.find_all('td')
        row_text = [data.text for data in row_data]
        length = len(oddsdf)
        oddsdf.loc[length] = row_text
    

    print(oddsdf)

    '''
    #getting all rows of the table
    pitcher_col_data = games_table.find_all('tr')
    #inserting each row data into our dataframe
    for row in pitcher_col_data[1:]:
        row_data = row.find_all('td')
        row_text = [data.text for data in row_data]
        length = len(pitcherdf)
        pitcherdf.loc[length] = row_text

    #print(pitcherdf)
    return pitcherdf

    #troubleshooting
    #print(pitcherdf)

def print_unqiue_pitcher_data_teams():
    pitcherdf = pitcher_data_func()
    print("Pitcher Data Unique Teams")
    print(pitcherdf['Team'].unique())

pitcher_data_func()
#print_unique_pitcher_data_teams()
'''


get_current_odds_data_func()