#log history of bets placed
import pandas as pd
from model import *

betsdf_columns = ["Date", "Home Score", "Away Score", "Total"]
betsdf = pd.DataFrame(columns = betsdf_columns)

'''
def saveBet(home_acr, away_acr, home_score, away_score, total):
    date = input("Enter game date(dd/mm/yy): ")
    home_score_string = home_acr + ": " + home_score
    away_score_string = away_acr + ": " + away_score
'''





game_func(home_input="LA Dodgers", home_input_acr="LAD", home_input_starter="", away_input="Colorado", away_input_acr="COL", away_input_starter="Kyle Freeland")


#def removeLastBet():
