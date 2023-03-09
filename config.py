"""
config.py

Configuration file for the project

By: Mitch Hollberg
Created: 9/3/2022
Last Updated: 9/3/2022
"""

# url_schedule_template = f'https://www.espn.com/college-football/schedule/_/week/{week_num}/year/{year_num}/seasontype/2'
# url_team_template = f'https://www.espn.com/college-football/team/_/id/{team_id}'
url_teams_template = fr'https://www.espn.com/college-football/teams'
# url_team_logo = fr'https://a.espncdn.com/combiner/i?img=/i/teamlogos/ncaa/500/{team_id}.png&amp;scale=crop&amp;cquality=40&amp;location=origin&amp;w=80&amp;h=80'


class Team(team_id: int):
    def __init__(self, team_id: int):
        self.team_id = team_id
        self.url_team_logo = fr'https://a.espncdn.com/combiner/i?img=/i/teamlogos/ncaa/500/{self.team_id}.'
        f'png&amp;scale=crop&amp;cquality=40&amp;location=origin&amp;w=80&amp;h=80'
        self.url_roster = fr'https://www.espn.com/college-football/team/roster/_/id/{self.team_id}'


    def get_schedule(self.team_id, season:int):
        """Get the schedule for the team for a given season (year)"""

        url_schedule = fr'https://www.espn.com/college-football/team/schedule/_/id/{team_id}/season/{season}'

