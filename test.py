import pandas as pd
df_premier21 = pd.read_csv('https://www.football-data.co.uk/mmz4281/2122/E0.csv')
print(df_premier21)
df_premier21 = df_premier21.rename(columns={'Date':'date', 'HomeTeam':'home_team', 'AwayTeam':'away_team', 'FTHG': 'home_goals', 'FTAG': 'away_goals'})
print(df_premier21)
simpsons = pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)')

print(simpsons[1].head())
