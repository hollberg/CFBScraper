import pandas as pd


df_schedule = pd.read_html(fr'https://www.espn.com/college-football/team/'
                        fr'schedule/_/id/239/season/2010',
                         header=1,
                         extract_links='all')[0]


# Build "Home/Away/Neutral" column
def get_home_away_neutral(x):

    if x.startswith('vs'):
        return 'Home'
    elif x.startswith('@'):
        return 'Away'
    else:
        return 'Neutral'

# Clean column names: remove "/None" from the end of the column names
df_schedule.columns = [col[0] for col in df_schedule.columns]

# Split columns into two columns; new column named "_links" will contain the links
for col in df_schedule.columns:
    col_name = f'{col}_links'

    df_schedule[col_name] = df_schedule[col].apply(lambda x: x[1] if isinstance(x, tuple) else None)
    df_schedule[col] = df_schedule[col].apply(lambda x: x[0] if isinstance(x, tuple) else x)

# Drop superfluous columns
df_schedule.drop(columns=['U', 'DATE_links', 'W-L (CONF)_links', 'U_links' ], axis=1, inplace=True)

print(df_schedule.head(5))



df_schedule['Home/Away/Neutral'] = df_schedule['OPPONENT'].apply(get_home_away_neutral)

moo = 'boo'