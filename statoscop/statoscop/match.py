import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import re

def match_stats(eve, num):
    url = "https://www.vlr.gg/" + eve
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    all_maps = soup.find_all("div", {"class": "vm-stats-game"})

    maps = all_maps[num]

    for e in maps.find_all("table", class_='wf-table-inset mod-overview'):
        team_1 = maps.find_all("table", class_='wf-table-inset mod-overview')[0]
        team_2 = maps.find_all("table", class_='wf-table-inset mod-overview')[1]

    if num == 1:
        stats_t1 = []
        header_row = []
        t_n = []
        p_n = []
        champions = []
        num_columns = 12

        for el in team_1.find_all('span', class_='mod-both'):
            stats_t1.append(el.get_text(strip=True))
        table_data = [stats_t1[i:i + num_columns] for i in range(0, len(stats_t1), num_columns)]

        for title in team_1.find_all('th'):
            header_row.append(title.get('title'))
        header_row = list(filter(None, header_row))
        header_row.remove('Agent')
        for el in team_1.find_all('div', class_='ge-text-light'):
            t_n.append(el.get_text(strip=True))
        for el in team_1.find_all('div', class_='text-of'):
            p_n.append(el.get_text(strip=True))
        for el in team_1.find_all('span', class_='mod-agent'):
            champions.append(el.find('img').get('title'))

        df_data = pd.DataFrame(table_data, columns=header_row)
        df_champions = pd.DataFrame(champions[0::2], columns=['Agents'])
        df_t_n = pd.DataFrame(t_n, columns=['Team'])
        df_p_n = pd.DataFrame(p_n, columns=['Player'])
        df = pd.concat([df_t_n, df_p_n, df_champions, df_data], axis=1)
        df = df.dropna()
        stats_t2 = []
        header_row = []
        t_n = []
        p_n = []
        champions = []
        num_columns = 12

        for el in team_2.find_all('span', class_='mod-both'):
            stats_t2.append(el.get_text(strip=True))
        table_data = [stats_t2[i:i + num_columns] for i in range(0, len(stats_t2), num_columns)]

        for title in team_2.find_all('th'):
            header_row.append(title.get('title'))
        header_row = list(filter(None, header_row))
        header_row.remove('Agent')
        for el in team_2.find_all('div', class_='ge-text-light'):
            t_n.append(el.get_text(strip=True))
        for el in team_2.find_all('div', class_='text-of'):
            p_n.append(el.get_text(strip=True))
        for el in team_2.find_all('span', class_='mod-agent'):
            champions.append(el.find('img').get('title'))

        df_data = pd.DataFrame(table_data, columns=header_row)
        df_champions = pd.DataFrame(champions[0::2], columns=['Agents'])
        df_t_n = pd.DataFrame(t_n, columns=['Team'])
        df_p_n = pd.DataFrame(p_n, columns=['Player'])
        df2 = pd.concat([df_t_n, df_p_n, df_champions, df_data], axis=1)
        df2 = df2.dropna()
        df = pd.concat([df, df2], axis=0, ignore_index=True)
        return df
    else:
        stats_t1 = []
        header_row = []
        t_n = []
        p_n = []
        champions = []
        num_columns = 12

        for el in team_1.find_all('span', class_='mod-both'):
            stats_t1.append(el.get_text(strip=True))
        table_data = [stats_t1[i:i + num_columns] for i in range(0, len(stats_t1), num_columns)]

        for title in team_1.find_all('th'):
            header_row.append(title.get('title'))
        header_row = list(filter(None, header_row))
        header_row.remove('Agent')
        for el in team_1.find_all('div', class_='ge-text-light'):
            t_n.append(el.get_text(strip=True))
        for el in team_1.find_all('div', class_='text-of'):
            p_n.append(el.get_text(strip=True))
        for el in team_1.find_all('span', class_='mod-agent'):
            champions.append(el.find('img').get('title'))

        df_data = pd.DataFrame(table_data, columns=header_row)
        df_champions = pd.DataFrame(champions, columns=['Agents'])
        df_t_n = pd.DataFrame(t_n, columns=['Team'])
        df_p_n = pd.DataFrame(p_n, columns=['Player'])
        df = pd.concat([df_t_n, df_p_n, df_champions, df_data], axis=1)
        df = df.dropna()

        stats_t2 = []
        header_row = []
        t_n = []
        p_n = []
        champions = []
        num_columns = 12

        for el in team_2.find_all('span', class_='mod-both'):
            stats_t2.append(el.get_text(strip=True))
        table_data = [stats_t2[i:i + num_columns] for i in range(0, len(stats_t2), num_columns)]

        for title in team_2.find_all('th'):
            header_row.append(title.get('title'))
        header_row = list(filter(None, header_row))
        header_row.remove('Agent')
        for el in team_2.find_all('div', class_='ge-text-light'):
            t_n.append(el.get_text(strip=True))
        for el in team_2.find_all('div', class_='text-of'):
            p_n.append(el.get_text(strip=True))
        for el in team_2.find_all('span', class_='mod-agent'):
            champions.append(el.find('img').get('title'))

        df_data = pd.DataFrame(table_data, columns=header_row)
        df_champions = pd.DataFrame(champions, columns=['Agents'])
        df_t_n = pd.DataFrame(t_n, columns=['Team'])
        df_p_n = pd.DataFrame(p_n, columns=['Player'])
        df2 = pd.concat([df_t_n, df_p_n, df_champions, df_data], axis=1)
        df2 = df2.dropna()
        df = pd.concat([df, df2], axis=0, ignore_index=True)
        return df

def match_perf_vs(eve, num):
    url = "https://www.vlr.gg/" + eve + "?tab=performance"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    all_maps = soup.find_all("div", {"class": "vm-stats-game"})
    perf = all_maps[num].find_all("table", {"class": "wf-table-inset mod-matrix mod-normal"})[0]
    perf_indi = []
    player_header = []
    team_header = []
    comp = []
    num_columns = 15
    for els in perf.find_all('div', {'class': 'team'}):
        player_header.append(els.find('div').contents[0].strip())
        team_header.append(els.find('div', class_='team-tag').contents[0].strip())
    for el in perf.find_all("div", {"class": "stats-sq"}):
        perf_indi.append(el.get_text(strip=True))
    for i in range(len(player_header)):
        comp.append(team_header[i] + ' ' + player_header[i])

    table_data = [perf_indi[i:i + num_columns] for i in range(0, len(perf_indi), num_columns)]
    df = pd.DataFrame(data=table_data)
    non_header = [1, 2, 4, 5, 7, 8, 10, 11, 13, 14]
    for a in range(len(non_header)):
        df.rename(columns={df.columns[non_header[a]]: ""}, inplace=True)
    df.rename(columns={df.columns[0]: comp[0],
                       df.columns[3]: comp[1],
                       df.columns[6]: comp[2],
                       df.columns[9]: comp[3],
                       df.columns[12]: comp[4]}, inplace=True)
    index = pd.DataFrame(comp[5:], columns=['Player'])
    df = pd.concat([index, df], axis=1)
    df.set_index(['Player'])
    return df

def match_perf_indiv(eve,num):
    url = "https://www.vlr.gg/" + eve + "?tab=performance"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    all_maps = soup.find_all("div", {"class": "vm-stats-game"})
    perf = all_maps[num].find_all("table", {"class": "wf-table-inset mod-adv-stats"})[0]
    perf_indi = []
    header = []
    player = []
    team = []
    comp = []
    num_columns = 13
    for els in perf.find_all('th'):
        header.append(els.get_text(strip=True))
    for els in perf.find_all('div', {'class': 'team'}):
        player.append(els.find('div').contents[0].strip())
        team.append(els.find('div', class_='team-tag').contents[0].strip())
    for i in range(len(player)):
        comp.append(team[i] + ' ' + player[i])
    df_comp = pd.DataFrame(comp, columns=['Player'])
    for el in perf.find_all("div", {"class": "stats-sq"}):
        perf_indi.append(el.contents[0].strip())
    table_data = [perf_indi[i:i + num_columns] for i in range(0, len(perf_indi), num_columns)]

    df = pd.DataFrame(data=table_data, columns=header[1:])
    df = pd.concat([df_comp, df], axis=1)
    df = df.drop(columns=df.columns[1])
    df.set_index('Player')
    return df

def eco_event(eve, num)