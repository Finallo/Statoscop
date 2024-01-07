import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import re


def ongoing(reg):
    """
    This function return a dataframe of all tournament ongoing from a region.
    :param reg: (str). You can have reg from region().
    :return: a dataframe.
    """
    url = "https://www.vlr.gg/events/" + reg
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    def ongo(balise):
        return balise.name == 'a' and balise.find('span', class_='event-item-desc-item-status mod-ongoing') is not None

    ongoings = pd.DataFrame(columns=['Match', 'Name', 'Date'])

    # Utiliser la fonction personnalisée pour récupérer les balises <a>
    balises_a = soup.find_all(ongo)

    # Afficher les balises <a> trouvées
    for balise_a in balises_a:
        texts = balise_a.find("div", class_="event-item-title")
        text = texts.get_text(strip=True)
        date = balise_a.find("div", class_="event-item-desc-item mod-dates").get_text(strip=True).replace('Dates', '')
        if "—" in date:
            periode1, periode2 = date.split("—")
            if len(periode2) <= 2:
                mois1, jour1 = [x.strip() for x in periode1.split()]
                jour2 = periode2
                date = f"{jour1} {mois1} - {jour2} {mois1}"
            elif periode2 == "TBD":
                mois1, jour1 = [x.strip() for x in periode1.split()]
                mois2 = periode2
                date = f"{jour1} {mois1} - {mois2}"
            elif len(periode2) > 2:
                mois1, jour1 = [x.strip() for x in periode1.split()]
                mois2, jour2 = [x.strip() for x in periode2.split()]
                date = f"{jour1} {mois1} - {jour2} {mois2}"
        else:
            mois1, jour1 = [x.strip() for x in periode1.split()]
            date = f"{jour1} {mois1}"
        url = balise_a.get('href')
        match = re.search(r"/event/(\d+)", url)
        match = match.group(1)
        ongoings = ongoings._append({'Match': match, 'Name': text, 'Date': date}, ignore_index=True)

    return ongoings


def upcoming(reg):
    """
    This function return a dataframe of all tournament upcoming from a region.
    :param reg: (str). You can have reg from region().
    :return: a dataframe.
    """
    url = "https://www.vlr.gg/events/" + reg
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    def upco(balise):
        return balise.name == 'a' and balise.find('span',
                                                  class_='event-item-desc-item-status mod-upcoming') is not None

    upcomings = pd.DataFrame(columns=['Match', 'Name', 'Date'])

    # Utiliser la fonction personnalisée pour récupérer les balises <a>
    balises_a = soup.find_all(upco)

    # Afficher les balises <a> trouvées
    for balise_a in balises_a:
        texts = balise_a.find("div", class_="event-item-title")
        text = texts.get_text(strip=True)
        date = balise_a.find("div", class_="event-item-desc-item mod-dates").get_text(strip=True).replace('Dates',
                                                                                                          '')
        if "—" in date:
            periode1, periode2 = date.split("—")
            if len(periode2) <= 2:
                mois1, jour1 = [x.strip() for x in periode1.split()]
                jour2 = periode2
                date = f"{jour1} {mois1} - {jour2} {mois1}"
            elif periode2 == "TBD":
                mois1, jour1 = [x.strip() for x in periode1.split()]
                mois2 = periode2
                date = f"{jour1} {mois1} - {mois2}"
            elif len(periode2) > 2:
                mois1, jour1 = [x.strip() for x in periode1.split()]
                mois2, jour2 = [x.strip() for x in periode2.split()]
                date = f"{jour1} {mois1} - {jour2} {mois2}"
        else:
            mois1, jour1 = [x.strip() for x in periode1.split()]
            date = f"{jour1} {mois1}"
        url = balise_a.get('href')
        match = re.search(r"/event/(\d+)", url)
        match = match.group(1)
        upcomings = upcomings._append({'Match': match, 'Name': text, 'Date': date}, ignore_index=True)

    return upcomings


def completed(reg):
    """
    This function return a dataframe of all tournament completed from a region.
    :param reg: (str). You can have reg from region().
    :return: a dataframe.
    """
    url = "https://www.vlr.gg/events/" + reg
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    def comp(balise):
        return balise.name == 'a' and balise.find('span',
                                                  class_='event-item-desc-item-status mod-completed') is not None

    completeds = pd.DataFrame(columns=['Match', 'Name', 'Date'])

    # Utiliser la fonction personnalisée pour récupérer les balises <a>
    balises_a = soup.find_all(comp)

    # Afficher les balises <a> trouvées
    for balise_a in balises_a:
        texts = balise_a.find("div", class_="event-item-title")
        text = texts.get_text(strip=True)
        date = balise_a.find("div", class_="event-item-desc-item mod-dates").get_text(strip=True).replace('Dates',
                                                                                                          '')
        if "—" in date:
            periode1, periode2 = date.split("—")
            if len(periode2) <= 2:
                mois1, jour1 = [x.strip() for x in periode1.split()]
                jour2 = periode2
                date = f"{jour1} {mois1} - {jour2} {mois1}"
            elif periode2 == "TBD":
                mois1, jour1 = [x.strip() for x in periode1.split()]
                mois2 = periode2
                date = f"{jour1} {mois1} - {mois2}"
            elif len(periode2) > 2:
                mois1, jour1 = [x.strip() for x in periode1.split()]
                mois2, jour2 = [x.strip() for x in periode2.split()]
                date = f"{jour1} {mois1} - {jour2} {mois2}"
        else:
            mois1, jour1 = [x.strip() for x in periode1.split()]
            date = f"{jour1} {mois1}"
        url = balise_a.get('href')
        match = re.search(r"/event/(\d+)", url)
        match = match.group(1)
        completeds = completeds._append({'Match': match, 'Name': text, 'Date': date}, ignore_index=True)

    return completeds
