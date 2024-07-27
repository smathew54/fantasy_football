# this works well for this version, now I need to adapt it for how I'd like to do my analysis
# import the packages
from urllib.request import urlopen
import ssl
from bs4 import BeautifulSoup
import pandas as pd
import logging
import certifi
from sqlalchemy import create_engine, Column, Integer, String, Sequence


# here is the code

# https://www.pro-football-reference.com/years/2020/leaders.htm

# set the webpage available
# takes in the data from the webpage and returns it as a df

def web_scrapper(year):
    year = str(year)
    url = 'https://www.pro-football-reference.com/years/' + year + '/fantasy.htm'
    logging.debug("starting the souper")
    context = ssl.create_default_context(cafile=certifi.where())
    html = urlopen(url, context=context)
    soup = BeautifulSoup(html, features='lxml')

    # get the headers for the dataframe
    headers = [th.getText() for th in soup.findAll('tr')[1].findAll('th')]
    headers = headers[1:]

    rows = soup.findAll('tr', class_=lambda table_rows: table_rows != "thread")
    player_stats = [[td.getText() for td in rows[i].findAll('td')]
                    for i in range(len(rows))]
    player_stats = player_stats[2:]

    stats = pd.DataFrame(player_stats, columns=headers)
    stats.FantPos = stats.FantPos.astype(str)
    stats.Player = stats.Player.astype(str)
    stats.Player = stats.Player.str.strip("*+")
#    team_selector(stats)
    return stats


def write_to_database(stats, year):
    print(stats)
    stats.to_csv('stats_file.csv')
    engine = create_engine('sqlite:////Users/Shawn/application/stats.db')
    table_name = 'fantasy_football_stats_{}'.format(year)
    stats.to_sql(table_name, con=engine, if_exists='replace', index=False)


def team_selector(stats):
    # team selector
    # need to now construct a team
    print(
        '''You currently don't have any players on your team. Let's build a team. 
        You will need the players to fill the following positions 
        \n \nQB\nWR\nWR\nWR\nRB\nRB\nTE\nW/R/TE\nK\nDef''')
    abbreviated_stats = (stats[["Player", "FantPos", 'PosRank', 'OvRank', 'FDPt']])
    print(abbreviated_stats.head(15))
    print('these are the available players')
    team_dict = {}
    while len(team_dict.keys()) < 4:
        if len(team_dict) != 0:
            position = str(input('Which position would you like to draft? Select [QB, RB, TE, WR]: '))
            print(stats.loc[stats['FantPos'] == position.upper()])
            drafted_player = input('Who would you like to draft? ')
            print('You drafted {}'.format(drafted_player))
            team_dict[position.upper()] = drafted_player
            print(team_dict)
            player_df = stats.loc[stats['Player'] == drafted_player]
            team_stats_df = pd.DataFrame()
            team_stats_df = pd.concat([player_df, team_stats_df], ignore_index=True)
            # stats = stats[stats.Player != drafted_player]
        else:
            position = str(input('Which Position do you need to draft? Select [QB, RB, TE, WR]: '))
            print(stats.loc[stats['FantPos'] == position.upper()])
            drafted_player = input('Who would you like to draft? ')
            print('You drafted {}'.format(drafted_player))
            team_dict[position.upper()] = drafted_player
            print(team_dict)
            # stats = stats[stats.Player != drafted_player]
            team_stats_df = stats.loc[stats['Player'] == drafted_player]

    print(team_stats_df)


if __name__ == "__main__":
    stats = web_scrapper(2023)
    write_to_database(stats, 2023)
