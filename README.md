# Statoscop

**Statoscop** is a package Python (and more :eyes:) to have data from Valorant esport first then for all players and for more games (League of Legends, TFT).
<hr />

### Available functions
<ul>
<li><b><u>Region():</u></b> To have all regions available. </li>
<br>
<li><b><u>Tournament:</u></b></li>
	<ul>
	<li><u>Completed(reg):</u> You will have a dataframe with all tournaments completed. 
    </br>Use 'Match' on event function to have details.</li>
	<li><u>Ongoing(reg):</u> You will have a dataframe with all tournaments ongoing. 
    </br>Use 'Match' on event function to have details.</li>
	<li><u>Upcoming(reg):</u> You will have a dataframe with all tournaments upcoming. 
    </br>Use 'Match' on event function to have details.</li>
	</ul>
<br>
<li><b><u>Event:</u></b></li>
    <ul>
    <li><u>Matchs(eve):</u> Matches will allow you to have all the matches of an "eve" event.
    </br>Use 'Match' as a string parameter from Tournament functions to have details.</li>
    <li><u>Team(eve):</u> Team will allow you to have all the teams of an "eve" event.
    </br>Use 'Match' as a string parameter from Tournament functions to have details.</li>
    <li><u>Stats(eve):</u> Matches will allow you to have all the matches of an "eve" event.
    </br>Use 'Match' as a string parameter from Tournament functions to have details.</li>
    <li><u>Agents(eve):</u> Agents will allow you to have a dataframe with all agents played of an "eve" event with his percentage of win/loss.
    </br>Use 'Match' as a string parameter from Tournament functions to have details.</li>
    <li><u>Matrix(eve):</u> Matrix will allow you to have multiple dataframes with all agents played of an "eve" event and which team take it.
    </br>Use 'Match' as a string parameter from Tournament functions to have details.</li>
    </ul>
<br>
<li><b><u>Match:</u></b></li>
    <ul>
    <li><u>Matchs_stats(eve, num):</u> Matchs_stats will allow you to have a dataframe with all stats about a 'eve' match.
    </br>Use 'Numéro de match' from event.matchs(eve) as a string paramater for 'eve' and an int for 'num' to select a match from a BO.</li>
    <li><u>Match_perf_vs(eve, num):</u> Match_perf_vs will allow you to have a dataframe with all winrate between two players for the match.
    </br>Use 'Numéro de match' from event.matchs(eve) as a string paramater for 'eve' and an int for 'num' to select a match from a BO.</li>
    <li><u>Match_perf_indiv(eve, num):</u> Match_perf_indiv will allow you to have a dataframe with all stats about a 'eve' match.
    </br>Use 'Numéro de match' from event.matchs(eve) as a string paramater for 'eve' and an int for 'num' to select a match from a BO.</li>
    <li><u>Eco_event(eve, num):</u> Eco_event will present you a dataframe with all event from a match (pistol won, eco round, semi-buy, etc...).
    </br>Use 'Numéro de match' from event.matchs(eve) as a string paramater for 'eve' and an int for 'num' to select a match from a BO.</li>
    <li><u>Eco_round(eve, num):</u> Eco_round present you a dataframe with all event from a match (pistol won, eco round, semi-buy, etc...) but round per round.
    </br>Use 'Numéro de match' from event.matchs(eve) as a string paramater for 'eve' and an int for 'num' to select a match from a BO.</li>
    </ul>
<li><b><u>Stats:</u></b></li>
<ul>
<li><u>Stats():</u> Stats will give you a huge dataframe with all players registered and all their stats.</li>
</ul>
</ul>
<hr />

### Installation

```pip install Statoscop```