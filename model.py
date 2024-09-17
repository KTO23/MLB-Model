from bs4 import BeautifulSoup
import requests
import pandas as pd



#url2 = 'https://razzball.com/mlbpitchingstats/'
#page2 = requests.get(url2)
#soup2 = BeautifulSoup(page2.text, features="html.parser")


url2 = 'https://www.fangraphs.com/leaders/major-league?pos=all&stats=pit&type=8&pageitems=2000000000&qual=0&pagenum=1'
page2 = requests.get(url2)
soup2 = BeautifulSoup(page2.text, features='html.parser')

pitcher_table = soup2.find_all('table')[8]
pitcher_table_labels = pitcher_table.find('tr')
pitcher_table_labels_new = pitcher_table_labels.find_all('th')
pitcher_table_labels_final = [title.text for title in pitcher_table_labels_new]


pitcher_df = pd.DataFrame(columns=pitcher_table_labels_final)


pitcher_col_data = pitcher_table.find_all('tr')
for row in pitcher_col_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text for data in row_data]

    length = len(pitcher_df)
    pitcher_df.loc[length] = individual_row_data

print(pitcher_df)