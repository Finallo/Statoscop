import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import re

def stats():
    """
    This function is to have a dataframe with all stats of players.
    :return: a dataframe.
    """
    url = "https://www.vlr.gg/stats"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', class_='wf-table mod-stats mod-scroll')
    table.find_all('th')
    header = []
    for title in table.find_all('th'):
        header.append(title.get_text(strip=True))
    header.remove('Player')
    header.remove('Agents')
    #'Player', 'Team', 'Agents',
    header.insert(0, 'Player')
    header.insert(1, 'Team')
    header.insert(2, 'Agents')
    header.insert(3, '3')
    header.insert(4, '4')
    t_bodys = table.find_all('tbody')[0]
    datas = []
    for tr_tag in t_bodys.find_all('tr'):
        player_name = tr_tag.find('div', class_='text-of').text.strip()
        datas.append(player_name)
        team_name = tr_tag.find('div', class_='stats-player-country').text.strip()
        datas.append(team_name)
        agent_names = []
        img_src = [img['src'] for img in tr_tag.find_all('img')]
        for src in img_src:
            start_index = src.find('/agents/') + len('/agents/')
            end_index = src.find('.png')
            agent_name = src[start_index:end_index].capitalize()
            agent_names.append(agent_name)
        combined_agents= ' / '.join(agent_names)
        datas.append(combined_agents)
        td_tags = tr_tag.find_all('td')
        for td in td_tags:
            datas.append(td.get_text(strip=True))
    num_columns = 24
    table_data = [datas[i:i + num_columns] for i in range(0, len(datas), num_columns)]
    df = pd.DataFrame(table_data, columns=header)
    df_final = df.drop(['3', '4'], axis=1)
    return df_final