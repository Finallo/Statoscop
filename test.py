import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

url = "https://www.vlr.gg/matches/results"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
data = soup.find_all('div')

df1 = pd.DataFrame()

a = pd.DataFrame(columns=["Compétition"])
b = pd.DataFrame(columns=["Phase"])

col = soup.find_all('div', class_='match-item-event-series text-of')
for cols in col:
    texts = cols.find_all(string=True, recursive=False)
    text1 = texts[0].strip()
    a = a._append({'Compétition':text1}, ignore_index=True)
col1 = soup.find_all('div', class_='match-item-event text-of')
for cols in col1:
    texts1 = cols.find_all(string=True, recursive=False)
    text2 = texts1[1].strip()
    b = b._append({'Phase':text2}, ignore_index=True)

df1 = b.join(a, how='inner')

df2 = pd.DataFrame()
c = pd.DataFrame(columns=["Team 2"])
d = pd.DataFrame(columns=["Team 1"])
col = soup.find_all('div', class_='match-item-vs-team-name')
for cols in col:
    texts = cols.find_all(string=True, recursive=True)
    text = texts[2].strip()
    text1 = texts[3].strip()
    d = d._append({'Team 1':text}, ignore_index=True)
    c = c._append({'Team 2':text1}, ignore_index=True)

c = c.replace('', np.nan, regex=True)
c = c.dropna()
c = c.reset_index(drop=True)
d = d.replace('', np.nan, regex=True)
d = d.dropna()
d = d.reset_index(drop=True)

df2 = d.join(c, how='inner')
df1 = df1.join(df2, how='inner')

col = soup.find_all('div', class_='match-item-vs-team-score js-spoiler')
df3 = pd.DataFrame()
e = pd.DataFrame(columns=["Score Team 1"])
f = pd.DataFrame(columns=["Score Team 2"])

for i, cols in enumerate(col):
    texts = cols.find_all(string=True, recursive=False)
    team = texts[0].strip()

    # Ajouter l'élément à 'c'
    if i % 2 == 0:
        e = e._append({'Score Team 1': team}, ignore_index=True)

for i, cols in enumerate(col):
    texts = cols.find_all(string=True, recursive=False)
    team = texts[0].strip()

    # Ajouter l'élément à 'c_impairs'
    if i % 2 != 0:
        f = f._append({'Score Team 2': team}, ignore_index=True)

df3 = e.join(f, how='inner')
df1 = df1.join(df3, how='inner')

g = pd.DataFrame(columns=["Date"])

col = soup.find_all('div', class_='ml-eta mod-completed')
for cols in col:
    texts = cols.find_all(string=True, recursive=False)
    text1 = texts[0].strip()
    if 'd' in text1:
        jour, heures = map(int, text1.replace('d','').replace('h', '').replace('m', '').split())
        duree = timedelta(days=jour, hours=heures, minutes=minutes)
        time = datetime.today() - duree
        timeM = time.minute
        timeMsup = (timeM + 1) % 60
        diff = timedelta(minutes=timeMsup - timeM)
        time = time + diff
        g = g._append({'Date':time.strftime("%d/%m/%Y %Hh%M")}, ignore_index=True)
    else:
        heures, minutes = map(int, text1.replace('d','').replace('h', '').replace('m', '').split())
        duree = timedelta(hours=heures, minutes=minutes)
        time = datetime.today() - duree
        timeM = time.minute
        timeMsup = (timeM + 1) % 60
        diff = timedelta(minutes=timeMsup - timeM)
        time = time + diff
        g = g._append({'Date':time.strftime("%d/%m/%Y %Hh%M")}, ignore_index=True)

df1 = df1.join(g, how='inner')

h = pd.DataFrame(columns=['Href'])
hrefs = soup.find_all("a", class_="wf-module-item")
for href in hrefs:
    texts2 = href.get('href')
    h = h._append({'Href': texts2[1:7]}, ignore_index=True)

df1 = h.join(df1, how='inner')
print(df1)