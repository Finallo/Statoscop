import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import re

def team(eve):
    url = "https://www.vlr.gg/event/" + eve
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    t_p = []
    for link in soup.find_all('a', class_={'wf-module-item'}):
        t_p.append(link.get('href'))

    teams = []
    players = []

    current_team = None
    for item in t_p:
        if '/team/' in item:
            current_team = re.search(r'/team/\d+/(.+)', item)
            if current_team:
                current_team = current_team.group(1)
        else:
            player_match = re.search(r'/player/\d+/(.+)', item)
            if player_match:
                players.append(player_match.group(1))
                teams.append(current_team)

    # Créer un DataFrame
    team_player = pd.DataFrame({'Team': teams, 'Player': players})

    return team_player

def matchs(eve):
    url = "https://www.vlr.gg/event/" + eve
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    matchs = []
    for link in soup.find_all('a', class_={'bracket-item'}):
        matchs.append(link.get('href'))

    team_names = soup.find_all('div', class_={'bracket-item-team-name'})
    name = [team_name.get_text(strip=True) for team_name in team_names]
    team_scores = soup.find_all('div', class_={'bracket-item-team-score'})
    scores = [team_score.get_text(strip=True) for team_score in team_scores]

    num_mat = []
    mat = []
    for item in matchs:
        match = re.match(r'/(?P<number>\d+)/(?P<text>.+)', item)
        if match:
            num_mat.append(match.group(1))

    for link in soup.find_all('a', class_={'bracket-item'}):
        mat.append(link.get('title'))

    df = pd.DataFrame({'Numéro de match': num_mat, 'Match': mat, 'Team 1': name[::2], 'Score Team 1': scores[::2],
                       'Team 2': name[1::2], 'Score Team 2': scores[1::2]})

    return df