import pandas as pd
import scraper_helpers as sh


url = f'https://www.espn.com/college-football/schedule/_/week/1/year/2021/seasontype/2'
schedule_columns = [('MATCHUP', None),
                    "('MATCHUP', None).1",
                    ('result', None),
                    ('passing leader', None),
                    ('rushing leader', None),
                    ('receiving leader', None)]


sched_tables = pd.read_html(url, extract_links='all')

moo = 'boo'

# Check that table columns match expected columns
for table in sched_tables:
    if list(table.columns) == schedule_columns:
        if 'df_schedule' not in locals():
            df_schedule = table
        else:
            df_schedule = pd.concat([df_schedule, table], axis=0)




print(df_schedule.head(5))
# print(list(sched_tables[0].columns))

# Clean column names: remove "/None" from the end of the column names
df_schedule = sh.clean_tuple_columns(df_schedule)

print(df_schedule.columns)

# Split columns into two columns; new column named "_links" will contain the links
df_schedule = sh.split_tuple_columns(df_schedule)

print(df_schedule.head(5))

moo = 'boo'

