from pitcher_data import *
from team_data import *
import pandas as pd

stored_pitcher_df = pd.DataFrame()
stored_team_df = pd.DataFrame()

def refresh_pitcher_df():
    updated_pitcher_df = pitcher_data_func()
    stored_pitcher_df = updated_pitcher_df.copy()
    return updated_pitcher_df

def refresh_team_data_df():
    updated_team_df = team_data_func()
    stored_team_df = updated_team_df.copy()
    return updated_team_df

def get_stored_pitcher_df():
    return stored_pitcher_df

def get_stored_team_df():
    return stored_team_df