import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import re

def matchs(eve):
    url = "https://www.vlr.gg/event/matches/" + eve + "/?series_id=all"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    t_ns = soup.find_all('div', class_={'match-item-vs-team-name'})
    team_name = [t_n.get_text(strip=True) for t_n in t_ns]

    t_ss = soup.find_all('div', class_={'match-item-vs-team-score'})
    team_score = [t_s.get_text(strip=True) for t_s in t_ss]

    all_event = soup.find_all('div', class_={'match-item-event'})
    event = [' '.join(all_e.stripped_strings) for all_e in all_event]

    matchs = []
    num_mat = []
    for link in soup.find_all('a', class_={'wf-module-item'}):
        matchs.append(link.get('href'))

    for item in matchs:
        match = re.match(r'/(?P<number>\d+)/(?P<text>.+)', item)
        if match:
            num_mat.append(match.group(1))

    df = pd.DataFrame({'Num_Match': num_mat, 'Event': event, 'Team1': team_name[::2], 'Score Team1': team_score[::2],
                       'Team2': team_name[1::2], 'Score Team2': team_score[1::2]})
    return df


def team(eve):
    df = matchs(eve)
    Teams = set(df['Team1'].unique()).union(df['Team2'].unique())
    return Teams

def stats(eve):
    url = "https://www.vlr.gg/event/stats/" + eve
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    all_td = soup.find_all('td')

    cell_content = [td.get_text(strip=True) for td in all_td]

    num_columns = 21

    table_data = [cell_content[i:i + num_columns] for i in range(0, len(cell_content), num_columns)]

    df = pd.DataFrame(table_data, columns=[f'Col{i + 1}' for i in range(num_columns)])
    df = df.drop(['Col2'], axis=1)

    return df