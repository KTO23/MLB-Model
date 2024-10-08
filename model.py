import pandas as pd
from pitcher_data import *
from team_data import *
from refresh_data import *
import math
from logging_funcs import *

#pitcher_data = get_stored_pitcher_df()
#team_data = get_stored_team_df()


#home_starter_IP_var = -1
#away_starter_IP_var = -1

def game_func(input_pitcher_data, input_team_data, home_input, home_input_acr, home_input_starter, away_input, away_input_acr, away_input_starter, date_input):
    pitcher_data = input_pitcher_data
    team_data = input_team_data

    home_starter_IP_var = -1
    away_starter_IP_var = -1

    #setting teams and pitchers
    home_team = home_input
    home_acr = home_input_acr
    home_starter = home_input_starter
    away_team = away_input
    away_acr = away_input_acr
    away_starter = away_input_starter

    date = date_input

    #data colleted from team_data
    home_rpg = 0
    home_rpg_last3 = 0
    home_rpg_at_home = 0
    away_rpg = 0
    away_rpg_last3 = 0
    away_rpg_while_away = 0

    #finding each team within our team_data DataFrame
    for index,row in team_data.iterrows():
        if row['Team'] == home_team:
            home_rpg = team_data['2024'][index]
            home_rpg_last3 = team_data['Last 3'][index]
            home_rpg_at_home = team_data['Home'][index]
        elif row['Team'] == away_team:
            away_rpg = team_data['2024'][index]
            away_rpg_last3 = team_data['Last 3'][index]
            away_rpg_while_away = team_data['Home'][index]
    

    #starter's variables
    home_starter_era = 0
    home_starter_IP = 0
    home_starter_starts = 0
    home_starter_games = 0
    home_starter_avg_IP = 0

    away_starter_era = 0
    away_starter_IP = 0
    away_starter_starts = 0
    away_starter_games = 0
    away_starter_avg_IP = 0

    #finding the starter from the pitcher_data DataFrame
    for index,row in pitcher_data.iterrows():
        if row['Name'] == home_starter:
            #era and IP data
            home_starter_era = float(pitcher_data['ERAERA - Earned Run Average ((ER*9)/IP)'][index])
            home_starter_IP = float(pitcher_data['IPIP - Innings Pitched'][index])

            #changing innings format: 17.1 --> 17.3, 67.2 --> 67.667
            temp_IP_floored = math.floor(home_starter_IP)
            temp_IP_difference = home_starter_IP - temp_IP_floored
            extra_outs = 0
            if(round(temp_IP_difference, 1) == 0.1):
                extra_outs = 1
            elif(round(temp_IP_difference, 1) == 0.2):
                extra_outs = 2
            
            #making sure they are a true starter
            #otherwise inning estimate will not be accurate
            home_starter_starts = float(pitcher_data['GSGS - Games Started'][index])
            home_starter_games = float(pitcher_data['GG - Games Pitched'][index])
            #threshold .5? could change later
            if ((home_starter_starts / home_starter_games) <= 0.5):
                #MANUALLY ENTER:
                while((home_starter_IP_var < 0 or home_starter_IP_var > 9)):
                    home_starter_IP_var = int(input("Not a starter. Enter est IP for " + str(home_input_starter) + ": "))
                home_starter_avg_IP = home_starter_IP_var
            else:
                #result from the change of decimal formatting
                home_starter_IP = ((temp_IP_floored * 3) + extra_outs)/3
                #getting avg start length
                home_starter_avg_IP = home_starter_IP/home_starter_starts 

        elif row['Name'] == away_starter:
            #era and IP data
            away_starter_era = float(pitcher_data['ERAERA - Earned Run Average ((ER*9)/IP)'][index])
            away_starter_IP = float(pitcher_data['IPIP - Innings Pitched'][index])
            
            #changing innings format: 17.1 --> 17.3, 67.2 --> 67.667
            temp_IP_floored = math.floor(away_starter_IP)
            temp_IP_difference = away_starter_IP - temp_IP_floored
            extra_outs = 0
            if(round(temp_IP_difference, 1) == 0.1):
                extra_outs = 1
            elif(round(temp_IP_difference, 1) == 0.2):
                extra_outs = 2

            #making sure they are a true starter
            #otherwise inning estimate will not be accurate
            away_starter_starts = float(pitcher_data['GSGS - Games Started'][index])
            away_starter_games = float(pitcher_data['GG - Games Pitched'][index])
            #threshold .5? could change later
            if ((away_starter_starts / away_starter_games) <= 0.5):
                #MANUALLY ENTER:
                while((away_starter_IP_var < 0 or away_starter_IP_var > 9)):
                    away_starter_IP_var = int(input("Not a starter. Enter est IP for " + str(away_input_starter) + ": "))
                away_starter_avg_IP = away_starter_IP_var
            else:
                #result from the change of decimal formatting
                away_starter_IP = ((temp_IP_floored * 3) + extra_outs)/3
                #getting avg start length
                away_starter_avg_IP = away_starter_IP/away_starter_starts

    need_rerun = False
    if(home_starter_IP == 0):
        home_starter = input("Name not found. Another name for " + home_starter + "?: ")
        need_rerun = True

    elif(away_starter_IP == 0):
        away_starter = input("Name not found. Another name for " + away_starter + "?: ")
        need_rerun = True

    if(need_rerun):
        for index,row in pitcher_data.iterrows():
            if row['Name'] == home_starter:
                #era and IP data
                home_starter_era = float(pitcher_data['ERAERA - Earned Run Average ((ER*9)/IP)'][index])
                home_starter_IP = float(pitcher_data['IPIP - Innings Pitched'][index])

                #changing innings format: 17.1 --> 17.3, 67.2 --> 67.667
                temp_IP_floored = math.floor(home_starter_IP)
                temp_IP_difference = home_starter_IP - temp_IP_floored
                extra_outs = 0
                if(round(temp_IP_difference, 1) == 0.1):
                    extra_outs = 1
                elif(round(temp_IP_difference, 1) == 0.2):
                    extra_outs = 2
                
                #making sure they are a true starter
                #otherwise inning estimate will not be accurate
                home_starter_starts = float(pitcher_data['GSGS - Games Started'][index])
                home_starter_games = float(pitcher_data['GG - Games Pitched'][index])
                #threshold .5? could change later
                if ((home_starter_starts / home_starter_games) <= 0.5):
                    #MANUALLY ENTER:
                    while((home_starter_IP_var < 0 or home_starter_IP_var > 9)):
                        home_starter_IP_var = int(input("Not a starter. Enter est IP for " + str(home_input_starter) + ": "))
                    home_starter_avg_IP = home_starter_IP_var
                else:
                    #result from the change of decimal formatting
                    home_starter_IP = ((temp_IP_floored * 3) + extra_outs)/3
                    #getting avg start length
                    home_starter_avg_IP = home_starter_IP/home_starter_starts 

            elif row['Name'] == away_starter:
                #era and IP data
                away_starter_era = float(pitcher_data['ERAERA - Earned Run Average ((ER*9)/IP)'][index])
                away_starter_IP = float(pitcher_data['IPIP - Innings Pitched'][index])
                
                #changing innings format: 17.1 --> 17.3, 67.2 --> 67.667
                temp_IP_floored = math.floor(away_starter_IP)
                temp_IP_difference = away_starter_IP - temp_IP_floored
                extra_outs = 0
                if(round(temp_IP_difference, 1) == 0.1):
                    extra_outs = 1
                elif(round(temp_IP_difference, 1) == 0.2):
                    extra_outs = 2

                #making sure they are a true starter
                #otherwise inning estimate will not be accurate
                away_starter_starts = float(pitcher_data['GSGS - Games Started'][index])
                away_starter_games = float(pitcher_data['GG - Games Pitched'][index])
                #threshold .5? could change later
                if ((away_starter_starts / away_starter_games) <= 0.5):
                    #MANUALLY ENTER:
                    while((away_starter_IP_var < 0 or away_starter_IP_var > 9)):
                        away_starter_IP_var = int(input("Not a starter. Enter est IP for " + str(away_input_starter) + ": "))
                    away_starter_avg_IP = away_starter_IP_var
                else:
                    #result from the change of decimal formatting
                    away_starter_IP = ((temp_IP_floored * 3) + extra_outs)/3
                    #getting avg start length
                    away_starter_avg_IP = away_starter_IP/away_starter_starts
    #converting avg IP to outs
    home_starter_avg_outs = int(round(home_starter_avg_IP*3))
    away_starter_avg_outs = int(round(away_starter_avg_IP*3))


    

    #temp for calculting total number of runs allowed from bullpen of each team
    temp_home_ERA = 0
    temp_home_IP = 0
    temp_home_ER = 0
    home_bullpen_outs = 0
    home_bullpen_ER = 0

    temp_away_ERA = 0
    temp_away_IP = 0
    temp_away_ER = 0
    away_bullpen_outs = 0
    away_bullpen_ER = 0

    for index,row in pitcher_data.iterrows():
        if row['Team'] == home_acr:
            temp_games = float(pitcher_data['GG - Games Pitched'][index])
            temp_starts = float(pitcher_data['GSGS - Games Started'][index])
            percent_starts = temp_starts/temp_games
            
            if percent_starts < 0.5:
                temp_home_ERA = float(pitcher_data['ERAERA - Earned Run Average ((ER*9)/IP)'][index])
                temp_home_IP = float(pitcher_data['IPIP - Innings Pitched'][index])

                temp_IP_floored = math.floor(temp_home_IP)
                temp_IP_difference = temp_home_IP - temp_IP_floored
                extra_outs = 0
                if(round(temp_IP_difference, 1) == 0.1):
                    extra_outs = 1
                elif(round(temp_IP_difference, 1) == 0.2):
                    extra_outs = 2

                temp_outs = (temp_IP_floored * 3) + extra_outs
                
                temp_home_ER = (temp_home_ERA * temp_outs * 3)/9
                home_bullpen_ER = home_bullpen_ER + temp_home_ER
                home_bullpen_outs = home_bullpen_outs + temp_outs


        elif row['Team'] == away_acr:
            temp_games = float(pitcher_data['GG - Games Pitched'][index])
            temp_starts = float(pitcher_data['GSGS - Games Started'][index])
            percent_starts = temp_starts/temp_games
            
            if percent_starts < 0.5:
                temp_away_ERA = float(pitcher_data['ERAERA - Earned Run Average ((ER*9)/IP)'][index])
                temp_away_IP = float(pitcher_data['IPIP - Innings Pitched'][index])

                temp_IP_floored = math.floor(temp_away_IP)
                temp_IP_difference = temp_away_IP - temp_IP_floored
                extra_outs = 0
                if(round(temp_IP_difference, 1) == 0.1):
                    extra_outs = 1
                elif(round(temp_IP_difference, 1) == 0.2):
                    extra_outs = 2

                temp_outs = (temp_IP_floored * 3) + extra_outs
                
                temp_away_ER = (temp_away_ERA * temp_outs * 3)/9
                away_bullpen_ER = away_bullpen_ER + temp_away_ER
                away_bullpen_outs = away_bullpen_outs + temp_outs


    home_bullpen_outs_needed = 27 - home_starter_avg_outs
    away_bullpen_outs_needed = 27 - away_starter_avg_outs

    home_bullpen_era = home_bullpen_ER / float(home_bullpen_outs/3)
    away_bullpen_era = away_bullpen_ER / float(away_bullpen_outs/3)

    est_home_starter_runs = (home_starter_era/9) * float(home_starter_avg_outs/3)
    est_away_starter_runs = (away_starter_era/9) * float(away_starter_avg_outs/3)

    est_home_bullpen_runs = (home_bullpen_era/9) * float(home_bullpen_outs_needed/3)
    est_away_bullpen_runs = (away_bullpen_era/9) * float(away_bullpen_outs_needed/3)

    est_runs_allowed_home = est_home_starter_runs + est_home_bullpen_runs
    est_runs_allowed_away = est_away_starter_runs + est_away_bullpen_runs

    est_total_runs_allowed = est_runs_allowed_home + est_runs_allowed_away
    est_total_rpg = float(home_rpg) + float(away_rpg)

    est_home_score = (float(home_rpg) + est_runs_allowed_away)/2
    est_away_score = (float(away_rpg) + est_runs_allowed_home)/2

    averaged_amount = (est_total_runs_allowed + est_total_rpg)/2

    print()
    print()
    print()
    print(home_acr)
    print(home_starter + "      ERA: " + str(home_starter_era) + "     IP: " + str(round(home_starter_IP, 2)) + "     Games: " + str(home_starter_games) + "       Starts: " + str(home_starter_starts))
    print(home_starter + "      EST RUNS ALLOWED: " + str(round(est_home_starter_runs, 2)) + "       AVG IP: " + str(round(home_starter_avg_outs / 3, 2)) + "      AVG OUTS: " + str(home_starter_avg_outs))
    print()
    print(away_acr)
    print(away_starter + "      ERA: " + str(away_starter_era) + "     IP: " + str(round(away_starter_IP, 2)) + "     Games: " + str(away_starter_games) + "       Starts: " + str(away_starter_starts))
    print(away_starter + "      EST RUNS ALLOWED: " + str(round(est_away_starter_runs, 2)) + "       AVG IP: " + str(round(away_starter_avg_outs / 3, 2)) + "      AVG OUTS: " + str(away_starter_avg_outs))
    print()
    print(home_acr + " BULLPEN")
    print("ERA: " + str(round(home_bullpen_era, 2)) + "     IP: " + str(round(home_bullpen_outs/3, 2)))
    print("EST RUNS ALLOWED: " + str(round(est_home_bullpen_runs, 2)) + "       IP NEEDED: " + str(round(home_bullpen_outs_needed/3, 2)))
    print()
    print(away_acr +" BULLPEN")
    print("ERA: " + str(round(away_bullpen_era, 2)) + "     IP: " + str(round(away_bullpen_outs/3, 2)))
    print("EST RUNS ALLOWED: " + str(round(est_away_bullpen_runs, 2)) + "       IP NEEDED: " + str(round(away_bullpen_outs_needed/3, 2)))
    print()
    print()
    print(home_acr + " TOTALS")
    print("EST RUNS ALLOWED: " + str(round(est_runs_allowed_home, 2)))
    print("RUNS PER GAME: " + str(home_rpg))
    print()
    print(away_acr + " TOTALS")
    print("EST RUNS ALLOWED: " + str(round(est_runs_allowed_away, 2)))
    print("RUNS PER GAME: " + str(away_rpg))
    print()
    print("SCORE")
    print(home_acr + " - " + str(round((float(home_rpg) + est_runs_allowed_away)/2, 2)))
    print(away_acr + " - " + str(round((float(away_rpg) + est_runs_allowed_home)/2, 2)))
    print("DIFFERENCE: " + str(round(((float(home_rpg) + est_runs_allowed_away)/2) - ((float(away_rpg) + est_runs_allowed_home)/2), 2)))
    print("TOTAL: " + str(round(averaged_amount, 2)))
    print()
    print()
    print()


    #self, input_date, input_home_team, input_home_starter, input_home_starter_ERA, input_home_starter_est_IP, input_home_starter_est_ER, input_home_bullpen_est_ER, input_away_team, input_away_starter, , input_away_starter_ERA, input_away_starter_est_IP, input_away_starter_est_ER, input_away_bullpen_est_ER,):

    this_bet_slip = bet_slip(date, home_team, home_starter, home_starter_era, home_starter_avg_IP, est_home_starter_runs, home_bullpen_era, est_home_bullpen_runs, away_team, away_starter, away_starter_era, away_starter_avg_IP, est_away_starter_runs, away_bullpen_era, away_bullpen_ER, est_home_score, est_away_score)
    return this_bet_slip


#game_func(input_pitcher_data=pitcher_data, input_team_data=team_data, home_input="Chi Sox", home_input_acr="CHW", home_input_starter="Davis Martin", away_input="LA Angels", away_input_acr="LAA", away_input_starter="José Suarez")
