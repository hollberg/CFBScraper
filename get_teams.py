"""
get_teams.py

Functions to get team data from ESPN.com

By: Mitch Hollberg
Created: 9/3/2022
Last Updated: 9/3/2022
"""

# IMPORTS
import pandas as pd
import bs4  # BeautifulSoup
import config as cfg
import requests
import lxml     # html parser
import re

# Use beautiful soup to get the team data
url = cfg.url_teams_template
page = requests.get(url)
soup = bs4.BeautifulSoup(page.content, features='lxml')

teams_dict = {}

for section in soup.find_all('section', class_='TeamLinks flex items-center'):

    team = section.next.next_sibling.contents[0].next.text
    # only keep the digits
    team_id = re.findall('\d+', section.next.next_sibling.contents[0].attrs['href'])[0]
    teams_dict[team] = team_id

print(teams_dict)

df_teams = pd.DataFrame(list(teams_dict.items()), columns=['team', 'team_id'])

df_teams.to_csv('data/teams.csv', index=False)


