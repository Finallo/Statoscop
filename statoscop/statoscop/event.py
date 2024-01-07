import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import re

def matchs(eve):
    """
    This function return all matchs from a tournament.
    :param eve: eve is the number of a tournament.
    :return: a dataframe.
    """
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
    """
    This function return a dictionary with all teams from a tournament.
    :param eve: eve is the number of a tournament.
    :return: a dictionary.
    """
    df = matchs(eve)
    Teams = set(df['Team1'].unique()).union(df['Team2'].unique())
    return Teams

def stats(eve):
    """
    This function return a dataframe to have a stats from all players who played on a tournament.
    :param eve: eve is the number of a tournament.
    :return: a dataframe.
    """
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

def agents(eve):
    """
    This function return a dataframe with all agents played on a tournament per map and his percentage of players who played on.
    :param eve: eve is the number of a tournament.
    :return: a dataframe.
    """
    url = "https://www.vlr.gg/event/agents/" + eve
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    target_table = soup.find('table', class_='wf-table mod-pr-global')

    # Vérifier si la table a été trouvée
    if target_table:
        # Trouver toutes les balises <td> dans la table
        all_td = target_table.find_all('td')

        # Extraire le texte de chaque cellule
        cell_contents = [td.get_text(strip=True) for td in all_td]
    # Diviser les données en lignes avec 20 colonnes par ligne
    num_columns = 27
    table_data = [cell_contents[i:i + num_columns] for i in range(0, len(cell_contents), num_columns)]

    header_row = soup.find('div', class_='pr-matrix-map')
    colums_headers = header_row.find_all('th') if header_row else []

    title_list = ["Map", "Pick", "ATK", "DEF"]
    for header in colums_headers:
        img_tag = header.find('img')
        if img_tag:
            title_attribute = img_tag.get('title')
            title_list.append(title_attribute)

    # Créer un DataFrame pandas
    df = pd.DataFrame(table_data, columns=title_list)
    df['Map'] = df['Map'].str[1:]

    return df

def matrix(eve):
    """
    This function return multiple dataframes with all agents played on a tournament per map and his percentage of players who played on.
    Do 'matrix(eve)[a]' to see a dataframe. [a] represent an int number.
    :param eve: eve is the number of a tournament.
    :return: a dataframe.
    """
    url = "https://www.vlr.gg/event/agents/" + eve
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    dfs = {}
    dfs_team = {}
    maps = []
    matrixs = soup.find_all('div', class_='pr-matrix-map')  # 6 matrices
    header_row = soup.find('div', class_='pr-matrix-map')
    colums_headers = header_row.find_all('th') if header_row else []

    for a in range(len(matrixs)):
        list = []
        for row in matrixs[a].find_all('tr', class_='pr-matrix-row'):
            if 'mod-dropdown' not in row.get('class', []):
                for cell in row.find_all('td'):
                    value = 1 if 'mod-picked' in cell.get('class', []) else 0
                    list.append(value)

        el = 25
        title_list = ["A", "B"]
        for header in colums_headers:
            img_tag = header.find('img')
            if img_tag:
                title_attribute = img_tag.get('title')
                title_list.append(title_attribute)
        sous_listes = [list[i:i + el] for i in range(0, len(list), el)]
        dfs[a] = pd.DataFrame(sous_listes, columns=title_list)

        th_tags = matrixs[a].find_all('th')
        for th_tag in th_tags:
            text = th_tag.get_text(strip=True)
            maps.append(text[1:])
        while ('' in maps):
            maps.remove('')
        df_maps = pd.DataFrame(maps)

    teams = []
    for x in range(len(matrixs[0].find_all('span', class_="text-of"))):
        teams.append(matrixs[0].find_all('span', class_="text-of")[x].get_text(strip=True))
        df_team = pd.DataFrame(teams)

    def create_dataframes(dfs, df_team, maps):
        result_dfs = []
        for e in range(len(dfs)):
            matrice_e = dfs[e]
            df_e = pd.concat([df_team, matrice_e], axis=1)
            df_e.rename(columns={df_e.columns[0]: maps[e]}, inplace=True)
            df_e = df_e.drop(["A", "B"], axis=1)
            result_dfs.append(df_e)

        return tuple(result_dfs)

    df0, df1, df2, df3, df4, df5, df6 = create_dataframes(dfs, df_team, maps)
    return df0, df1, df2, df3, df4, df5, df6
