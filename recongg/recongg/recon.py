import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import re

def region():
    print("Les regions existantes sont : \n All, north-america, europe, brazil, asia-pacific, korea, japan, latin-america, oceania, mena, game-changers, collegiate")