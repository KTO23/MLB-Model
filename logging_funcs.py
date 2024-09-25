#log history of bets placed
import pandas as pd
from model import *


class bet_slip():
    #when calling game_func in run_model, we can store a bet by using the information displayed in the terminal into this object
    #then create either a list of dataframe to store all this past data
    def __init__(self, input_date, input_home_team, input_home_starter, input_home_starter_ERA, input_home_starter_est_IP, input_home_starter_est_ER, input_home_bullpen_est_ER, input_away_team, input_away_starter, , input_away_starter_ERA, input_away_starter_est_IP, input_away_starter_est_ER, input_away_bullpen_est_ER,):
        self.date = input_date
        self.home_team = input_home_team
        self.home_starter = input_home_starter
        self.home_starter_era = input_home_starter_ERA
        self.home_starter_est_IP = input_home_starter_est_IP
        self.home_starter_est_ER = input_home_starter_est_ER
        self.home_bullpen_ER = input_home_bullpen_est_ER


        self.away_team = input_away_team
        self.away_starter = input_away_starter
        self.away_starter_era = input_home_starter_ERA
        self.away_starter_est_IP = input_home_starter_est_IP
        self.away_starter_est_ER = input_home_starter_est_ER
        self.away_bullpen_ER = input_home_bullpen_est_ER

        self.home_score = 0
        self.away_score = 0

    def update_result(self, input_home_score, input_away_score):
        #br link with game result data? 
        self.home_score = input_home_score
        self.away_score = input_away_score
