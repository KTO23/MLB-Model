from bs4 import BeautifulSoup
import requests
import pandas as pd


#old url - table in html not working
#url2 = 'https://razzball.com/mlbpitchingstats/'
#page2 = requests.get(url2)
#soup2 = BeautifulSoup(page2.text, features="html.parser")

def game_log_giants_func():
    url = 'https://www.baseball-reference.com/teams/SFG/2024-schedule-scores.shtml#all_results'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, features='html.parser')

    #sorts html to find the table titles - used to put into our dataframe
    game_table = soup.find_all('table')[0]
    labels = game_table.find_all('th')
    #labels = game_table.find_all('th')
    column_titles = [title.text for title in labels[1:21]]
    #print(column_titles)
    column_titles[1] = "past/future"
    column_titles[3] = "H/A"
    pastgamesdf = pd.DataFrame(columns=column_titles)
    column_titles[5] = "starttime"
    futuregamesdf = pd.DataFrame(columns=column_titles[:6])


    game_table_rows = game_table.find_all('tr')
    # Loop through the rows and exclude ones with a certain class
    for row in game_table_rows:
        # Exclude rows with the class 'exclude-class'
        if 'thead' in row.get('class', []):
            continue  # Skip this row if it has the class 'exclude-class'
        else:
            col_data = row.find_all('td')[:20]  # Get the first 20 columns of data
            if col_data:  # Only process if the row has <td> elements (not header rows)
                row_text = [data.text for data in col_data]
                if(row_text[1] == 'preview'): #this is a future game
                    futuregamesdf.loc[len(futuregamesdf)] = row_text[:6]
                else:
                    pastgamesdf.loc[len(pastgamesdf)] = row_text
   
    print(pastgamesdf)

    return pastgamesdf

game_log_giants_func()