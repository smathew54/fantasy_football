#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 19:12:50 2021

@author: Shawn
"""

import pandas as pd
import numpy as np

#bring in the dataframes from the excel
receiving = pd.read_csv("../data/Quartback_receiving.csv")
rushing = pd.read_csv('../data/Quartback_Running_data.csv')
passing = pd.read_csv('../data/Quartback_data.csv')

#do some adjusting to each of the dataframes
passing = passing.drop(['Rk'], axis = 1)

#adjusting the rushing dataframe
#rushing.drop(rushing.index[[0]])
rushing = rushing.drop(['Rk'], axis = 1)


#adjusting receiving dataframe
receiving = receiving.drop(['Rk'], axis = 1)



#double checking the dataframe and seeing how it looks
print(passing.head())
print(rushing.head())
print(receiving.head())

#create a list of all the available players in a list
def available_players():
    #get the player names for each of the different subsections
    
    #do it for the quarterbacks
    passing_players_name = passing['Player'].str.strip()
    passing_players_position = passing['Pos'].str.upper()
    
    #calculate the points
    
    passing_yards_points = passing['Yds']/10
    passing_interceptions = passing['Int'] * -2
    passing_td = passing['TD'] * 6
    passing_players = list(zip(passing_players_name, passing_players_position))
    #passing_players = passing_players_name + passing_players_position
    #print(passing_players)
    
    rushing_players_name = rushing['Player'].str.strip()
    rushing_players_position = rushing['Pos'].str.upper()
    rushing_players = list(zip(rushing_players_name, rushing_players_position))
    #print(rushing_players)
    
    #do it also for the receiving players
    receiving_players_name = receiving['Player'].str.strip()
    receiving_players_position = receiving['Pos'].str.upper()
    receiving_players = list(zip(receiving_players_name, receiving_players_position))
    
    #set it into a single column so we can pass it by
    all_players  = passing_players
    
    all_players.append(rushing_players)
    all_players.append(receiving_players)
    print(all_players)
    return(all_players)
    #all_players.append(receiving)
    #print(all_players)
    #print(passing_players_position)