from bs4 import BeautifulSoup
import requests
import pandas as pd


#old url - table in html not working
#url2 = 'https://razzball.com/mlbpitchingstats/'
#page2 = requests.get(url2)
#soup2 = BeautifulSoup(page2.text, features="html.parser")

def game_log_padres_func():
    url = 'https://www.baseball-reference.com/teams/SDP/2024-schedule-scores.shtml#all_results'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, features='html.parser')

    #sorts html to find the table titles - used to put into our dataframe
    game_table = soup.find_all('table')[0]
    labels = game_table.find_all('th')
    #labels = game_table.find_all('th')
    column_titles = [title.text for title in labels[1:21]]
    #print(column_titles)
    column_titles[1] = "boxscore/preview"
    column_titles[3] = "'@ or ' '(home)"
    gamedf = pd.DataFrame(columns=column_titles)
    print(gamedf)

    print()

    game_table_data = game_table.find_all('tr')
    true_length = 0
    print(len(game_table_data))

    row_ranges = list(range(1, len(game_table_data)))

    for row in game_table_data[1:]:
        row_data = row.find_all('td')
        row_text = [data.text for data in row_data]
        length = len(pitcherdf)
        pitcherdf.loc[length] = row_text

    print(pitcherdf)
    return pitcherdf


    print(gamedf)
    return gamedf

    #troubleshooting
    #print(gamedf)

game_log_padres_func()