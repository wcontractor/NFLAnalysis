import nflgame
#Get all 2015 game stats
season2015 = nflgame.games(2015)
#Get the player stats for the 2015 games
playerstats2015 = nflgame.combine(season2015)
#Dump the data into a CSV
playerstats2015.csv('player-stats-2015.csv')
