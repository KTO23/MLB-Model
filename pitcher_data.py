from bs4 import BeautifulSoup
import requests
import pandas as pd


#old url - table in html not working
#url2 = 'https://razzball.com/mlbpitchingstats/'
#page2 = requests.get(url2)
#soup2 = BeautifulSoup(page2.text, features="html.parser")

def pitcher_data_func():
    url2 = 'https://www.fangraphs.com/leaders/major-league?pos=all&stats=pit&type=8&pageitems=2000000000&qual=0&pagenum=1'
    page2 = requests.get(url2)
    soup2 = BeautifulSoup(page2.text, features='html.parser')

    #sorts html to find the table titles - used to put into our dataframe
    pitcher_table = soup2.find_all('table')[8]
    pitcher_table_labels = pitcher_table.find('tr')
    pitcher_table_labels_new = pitcher_table_labels.find_all('th')
    pitcher_table_labels_final = [title.text for title in pitcher_table_labels_new]
    pitcher_df = pd.DataFrame(columns=pitcher_table_labels_final)

    #getting all rows of the table
    pitcher_col_data = pitcher_table.find_all('tr')
    #inserting each row data into our dataframe
    for row in pitcher_col_data[1:]:
        row_data = row.find_all('td')
        individual_row_data = [data.text for data in row_data]
        length = len(pitcher_df)
        pitcher_df.loc[length] = individual_row_data


    return pitcher_df

    #troubleshooting
    #print(pitcher_df)