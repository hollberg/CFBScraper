"""
get_cfb_schedules.py
Program to get CFB schedules from ESPN.com
"""

import pandas as pd
import scraper_helpers as sh
import sqlite3
import re

url = f'https://www.espn.com/college-football/schedule/_/week/1/year/2021/seasontype/2'

def get_cfbschedules(week_num, year_num, seasontype):
    """
    Get CFB schedules from ESPN.com
    :param week_num: Week of season
    :param year_num: Year of season
    :param seasontype: 2 = regular season, 3 = bowl season. Bowl season week=1
    :return: dataframe of schedule
    """
    url = f'https://www.espn.com/college-football/schedule/_/week/{week_num}/year/{year_num}/seasontype/{seasontype}'

    schedule_columns = [('MATCHUP', None),
                        "('MATCHUP', None).1",
                        ('result', None),
                        ('passing leader', None),
                        ('rushing leader', None),
                        ('receiving leader', None)]


    sched_tables = pd.read_html(url, extract_links='all')

    # Check that table columns match expected columns
    for table in sched_tables:
        if list(table.columns) == schedule_columns:
            if 'df_schedule' not in locals():
                df_schedule = table
            else:
                df_schedule = pd.concat([df_schedule, table], axis=0)


    # Clean column names: remove "/None" from the end of the column names
    df_schedule = sh.clean_tuple_columns(df_schedule)

    # Split columns into two columns; new column named "_links" will contain the links
    df_schedule = sh.split_tuple_columns(df_schedule)

    # Rename columns
    df_schedule = df_schedule.rename(columns={'MATCHUP': 'Away Team',
                                              '(': 'Home Team',
                                              'MATCHUP_links': 'Away Team Links',
                                              '(_links': 'Home Team Links'})

    # Clen up team names (convert to "Alabama" from "@ #1 Alabama")
    pattern = r'^[^a-zA-Z]*'    # Replace everything before the first letter
    df_schedule['Away Team'] = df_schedule['Away Team'].str.replace(pattern, '')
    df_schedule['Home Team'] = df_schedule['Home Team'].str.replace(pattern, '')
    df_schedule['year'] = year_num
    df_schedule['week'] = week_num
    df_schedule['seasontype'] = seasontype

    return df_schedule

# Loop over all years, weeks, and seasontypes to get all schedules
for year_num in range(2010, 2022):
    for week_num in range(1, 18):
        for seasontype in range(2, 3):
            try:
                df_schedule = get_cfbschedules(week_num, year_num, seasontype)
                # Append new schedule to existing schedule
                try:
                    df_schedule_all = pd.concat([df_schedule_all, df_schedule], axis=0)
                except:
                    df_schedule_all = df_schedule
            except:
                print(f'No data for week {week_num}, year {year_num}, seasontype {seasontype}')


df_schedule_all.to_excel(r'../data/schedule.xlsx', index=False)

