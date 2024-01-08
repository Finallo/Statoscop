# Statoscop

**Statoscop** is a package Python (and more :eyes:) to have data from Valorant esport first then for all players and for more games (League of Legends, TFT).
<hr />


### Installation

```pip install Statoscop```

<hr />

### Available functions
<ul>
<li><b><u>Region():</u></b> To have all regions available. </li>
<br>
<li><b><u>Tournament:</u></b></li>
	<ul>
	<li><u>Completed(reg):</u> You will have a dataframe with all tournaments completed. 
    <br>Use 'Match' on event function to have details.</li>
	<li><u>Ongoing(reg):</u> You will have a dataframe with all tournaments ongoing. 
    <br>Use 'Match' on event function to have details.</li>
	<li><u>Upcoming(reg):</u> You will have a dataframe with all tournaments upcoming. 
    <br>Use 'Match' on event function to have details.</li>
	</ul>
<br>
<li><b><u>Event:</u></b></li>
    <ul>
    <li><u>Matchs(eve):</u> Matches will allow you to have all the matches of an "eve" event.
    <br>Use 'Match' as a string parameter from Tournament functions to have details.</li>
    <li><u>Team(eve):</u> Team will allow you to have all the teams of an "eve" event.
    <br>Use 'Match' as a string parameter from Tournament functions to have details.</li>
    <li><u>Stats(eve):</u> Matches will allow you to have all the matches of an "eve" event.
    <br>Use 'Match' as a string parameter from Tournament functions to have details.</li>
    <li><u>Agents(eve):</u> Agents will allow you to have a dataframe with all agents played of an "eve" event with his percentage of win/loss.
    <br>Use 'Match' as a string parameter from Tournament functions to have details.</li>
    <li><u>Matrix(eve):</u> Matrix will allow you to have multiple dataframes with all agents played of an "eve" event and which team take it.
    <br>Use 'Match' as a string parameter from Tournament functions to have details.</li>
    </ul>
<br>
<li><b><u>Match:</u></b></li>
    <ul>
    <li><u>Matchs_stats(eve, num):</u> Matchs_stats will allow you to have a dataframe with all stats about a 'eve' match.
    <br>Use 'Num_match' from event.matchs(eve) as a string paramater for 'eve' and an int for 'num' to select a match from a BO.</li>
    <li><u>Match_perf_vs(eve, num):</u> Match_perf_vs will allow you to have a dataframe with all winrate between two players for the match.
    <br>Use 'Num_match' from event.matchs(eve) as a string paramater for 'eve' and an int for 'num' to select a match from a BO.</li>
    <li><u>Match_perf_indiv(eve, num):</u> Match_perf_indiv will allow you to have a dataframe with all stats about a 'eve' match.
    <br>Use 'Num_match' from event.matchs(eve) as a string paramater for 'eve' and an int for 'num' to select a match from a BO.</li>
    <li><u>Eco_event(eve, num):</u> Eco_event will present you a dataframe with all event from a match (pistol won, eco round, semi-buy, etc...).
    <br>Use 'Num_match' from event.matchs(eve) as a string paramater for 'eve' and an int for 'num' to select a match from a BO.</li>
    <li><u>Eco_round(eve, num):</u> Eco_round present you a dataframe with all event from a match (pistol won, eco round, semi-buy, etc...) but round per round.
    <br>Use 'Num_match' from event.matchs(eve) as a string paramater for 'eve' and an int for 'num' to select a match from a BO.</li>
    </ul>
<li><b><u>Stats:</u></b></li>
<ul>
<li><u>Stats():</u> Stats will give you a huge dataframe with all players registered and all their stats.</li>
</ul>
</ul>
<hr />

### Some examples

```
from statoscop import tournament

tournament.upcoming('europe')
```
The result is:

| # | Match  |                        Name                         |       Date        |
|---|:------:|:---------------------------------------------------:|:-----------------:|
| 0 |  1939  |    Challengers League 2024 Spain Rising: Split 1    |  15 Jan - 21 Apr  |
| 1 |  1945  |  Challengers League 2024 Portugal Tempest: Split 1  |   15 Jan - TBD    |
| 2 |  1932  |     Challengers League 2024 East Surge: Split 1     |  15 Jan - 9 Apr   |
| 3 |  1948  |   Challengers League 2024 DACH Evolution: Split 1   |   20 Jan - TBD    |
| 4 |  1942  |  Challengers League 2024 France: Revolution Spl...  |   20 Jan - TBD    |
| 5 |  1947  |  Challengers League 2024 Italy Rinascimento: Sp...  |   27 Jan - TBD    |
| 6 |  1943  |  Challengers League 2024 Northern Europe: Polar...  |    1 Feb - TBD    |
| 7 |  1893  |   Challengers League 2024 Türkiye Birlik: Split 1   |   10 Feb - TBD    |
| 8 |  1925  |          Champions Tour 2024: EMEA Kickoff          |   20 Feb - TBD    |
| 9 |  1921  |         Champions Tour 2024: Masters Madrid         |  14 Mar - 24 Mar  |

```
from statoscop import event

event.matchs("1920") # 1920 represent the Mandatory Cup (cc Zerator 👀)
```
The result is:

| #  | Num_match |                      Event                       |          Team1           |  Score Team1  |       Team2        |  Score Team2  |
|---|:---------:|:------------------------------------------------:|:------------------------:|:-------------:|:------------------:|:-------------:|
| 21 |  291468   |               Grand Final Playoffs               |       CGN Esports        |       0       |       Acend        |       3       |
| 20 |  291467   |               Semifinals Playoffs                |          Acend           |       2       | UCAM Esports Club  |       1       |
| 19 |  291466   |               Semifinals Playoffs                |       CGN Esports        |       2       |    NASR Esports    |       0       |

```
from statoscop import match

match.match_stats("291466", 1) # CGN Esport vs NASR Esport. Semifinals of Mandatory Cup
```
The result is:

|  #  |Team|Player|Agents|Rating|Average Combat Score|Kills|Deaths|Assists|Kills - Deaths|"Kill, Assist, Trade, Survive %"|Average Damage per Round|Headshot %|First Kills|First Deaths|Kills - Deaths|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|  0  |CGN|DaviH|Sova|1.41|294|22|11|4|+11|80%|187|25%|2|0|+2|
|  1  |CGN|Vince|Astra|1.09|150|11|10|8|+1|75%|107|26%|2|0|+2|
|  2  |CGN|BennY|Phoenix|1.08|223|16|15|4|+1|70%|146|13%|3|2|+1|
|  3  |CGN|aNguiSt|Killjoy|0.81|145|10|13|3|-3|75%|114|32%|2|2|0|
|  4  |CGN|elllement|Jett|0.75|186|14|15|2|-1|70%|130|36%|5|2|+3|
|  5  |NASR|sibeastw0w|Jett|1.16|232|16|14|2|+2|75%|150|30%|4|5|-1|
|  6  |NASR|vakk|Killjoy|0.97|191|14|13|2|+1|60%|115|37%|1|2|-1|
|  7  |NASR|Avez|Sova|0.95|200|12|15|9|-3|65%|165|25%|0|2|-2|
|  8  |NASR|Shalaby|Kayo|0.86|152|9|15|4|-6|65%|112|24%|0|2|-2|
|  9  |NASR|xenon|Omen|0.81|186|13|16|5|-3|65%|106|54%|1|3|-2|

<hr />

If you have any questions, contact me.

<b><u>X</u></b>: <a href="https://www.twitter.com/Finallo_">/Finallo_</a><br>
<b><u>Threads</u></b>: <a href="https://www.threads.net/@Finallo_">/Finallo_</a><br>
<b><u>Discord</u></b>: Finallo<br>
<b><u>Buy me a coffee:</u></b> <a href="https://www.buymeacoffee.com/finallo">Finallo</a>
<br>
<br>
I am looking for a job as a Python developer, Data Analyst, Data Scientist or DBA. <br>Contact me if you are interested or would like more information about me.