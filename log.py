#log history of bets placed
import pandas as pd


betsdf_columns = ["Date", "Home Score", "Away Score", "Total"]
betsdf = pd.DataFrame(columns = betsdf_columns)

def saveBet(home_acr, away_acr, home_score, away_score, total):
    date = input("Enter game date(dd/mm/yy): ")
    home_score_string = home_acr + ": " + home_score
    away_score_string = away_acr + ": " + away_score
    


def removeLastBet():
