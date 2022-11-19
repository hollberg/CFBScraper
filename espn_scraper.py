"""
espn_scraper.py

Functions to scrape data from ESPN.com

By: Mitch Hollberg
Created: 9/3/2022
Last Updated: 9/3/2022
"""

# IMPORTS
import pandas as pd


class Espn():
    def __init__(self):
        url_schedule_template = f'https://www.espn.com/college-football/schedule/_/week/{week_num}/year/{year_num}/seasontype/2'
        url_teams_template = f'https://www.espn.com/college-football/team/_/id/{team_id}'
