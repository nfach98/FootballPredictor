import os
import re
import pandas as pd


def set_season(row):
    year = row['date'].split('-')[0]
    month = row['date'].split('-')[1]
    if month >= '08':
        return f'{int(year)}-{int(year) + 1}'
    else:
        return f'{int(year) - 1}-{int(year)}'

def set_region(row):
    dict_region =  {
        'Fußball-Bundesliga': 'Germany',
        'La Liga': 'Spain',
        'Ligue 1': 'France',
        'Premier League': 'England',
        'Serie A': 'Italy',
        'UEFA Champions League': 'Europe',
        'UEFA Europa League': 'Europe',
    }

    return dict_region[row['league']]

csvs = [f for f in os.listdir('.') if os.path.isfile(f)]
csvs = [f for f in csvs if re.match(r'^(items_matches)', f) and f.endswith('.csv')]

df_old = pd.read_csv('matches.csv')
dfs = [pd.read_csv(c) for c in csvs]
df_new = pd.concat(dfs, ignore_index=True)
df_new = df_new.drop(columns=['key'])
df_new = df_new.drop_duplicates()
df_new = pd.concat([df_new, df_old], ignore_index=True)

df_new['region'] = df_new.apply(set_region, axis=1)
df_new['type'] = 'Club'

df_new = df_new[[
    'league',
    'region',
    'type',
    'season',
    'round',
    'date',
    'time',
    'H_team_name',
    'H_goals',
    'A_goals',
    'A_team_name',
    'H_possession',
    'H_passes_completed',
    'H_passes_total',
    'H_shots_on_target',
    'H_shots_total',
    'H_saves',
    'H_yellow_cards',
    'H_red_cards',
    'H_own_goals',
    'H_fouls',
    'H_corners',
    'H_crosses',
    'H_touches',
    'H_tackles',
    'H_interceptions',
    'H_aerials_won',
    'H_clearances',
    'H_offsides',
    'H_goal_kicks',
    'H_throw_ins',
    'H_long_balls',
    'A_possession',
    'A_passes_completed',
    'A_passes_total',
    'A_shots_on_target',
    'A_shots_total',
    'A_saves',
    'A_yellow_cards',
    'A_red_cards',
    'A_own_goals',
    'A_fouls',
    'A_corners',
    'A_crosses',
    'A_touches',
    'A_tackles',
    'A_interceptions',
    'A_aerials_won',
    'A_clearances',
    'A_offsides',
    'A_goal_kicks',
    'A_throw_ins',
    'A_long_balls'
]]

df_new = df_new.sort_values(by=['league', 'season', 'date'])
df_new.to_csv('matches.csv',index=False)
