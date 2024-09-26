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
    '''
    #print(games_table)
    temp = games_table.find('tr')
    labels = temp.find_all('th')
    column_titles = [title.text for title in labels]
    '''
    column_titles = ["Team", "Run Line", "Run Line Juice", "Total", "Total Juice", "Moneyline"]
    oddsdf = pd.DataFrame(columns=column_titles)

    #print(column_titles)
    col_data = games_table.find_all('tr')
    #print(col_data)

    
    for row in col_data[1:]:
        team_temp = row.find('th')
        team_temp2 = team_temp.find_all('div')[7]
        team_name = [data.text for data in team_temp2]

        #run line
        run_line_data = row.find_all('div')[13]
        run_line = [data.text for data in run_line_data]

        #run line juice
        run_line_juice_data = row.find_all('div')[16]
        run_line_juice = [data.text for data in run_line_juice_data]

        #total
        total_data = row.find_all('div')[20]
        total_line_temp = [data.text for data in total_data]
        total_line = [total_line_temp[0] + total_line_temp[2]]

        #total_juice
        total_juice_data = row.find_all('div')[19]
        total_line_juice_temp = [data.text for data in total_juice_data]
        total_line_juice = [total_line_juice_temp[1]]

        #ml
        ml_data = row.find_all('div')[24]
        ml = [data.text for data in ml_data]
        
        row_data = [team_name[0], run_line[0], run_line_juice[0], total_line[0], total_line_juice[0], ml[0]]
        length = len(oddsdf)
        oddsdf.loc[length] = row_data
    

    print(oddsdf)


get_current_odds_data_func()