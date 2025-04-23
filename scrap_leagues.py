from seleniumbase import SB
import time
from urllib.error import HTTPError
import random
import pandas as pd

domain = 'https://fbref.com'

def open_url(sb, url):
    sb.uc_open_with_reconnect(url, 3)
    try:
        verify_success(sb)
    except Exception:
        if sb.is_element_visible('input[value*="Verify"]'):
            sb.uc_click('input[value*="Verify"]')
        else:
            sb.uc_gui_click_captcha()
        
        try:
            verify_success(sb)
        except Exception as e:
            print(e)
    

def verify_success(sb):
    sb.assert_element('img[alt="FBref.com Logo & Link to home page"]', timeout=4)
    sb.sleep(random.randint(1, 5))


def get_league_matches_links(sb, name, season):
    anchors = sb.find_elements('a:contains("Match Report")')
    links = [a.get_attribute('href') for a in anchors]
    return links


def main():
    leagues = [
        {
            'name': 'Premier League',
            'id': '9',
            'seasons': 10,
        },
        {
            'name': 'La Liga',
            'id': '12',
            'seasons': 7,
        },
        {
            'name': 'Serie A',
            'id': '11',
            'seasons': 7,
        },
        {
            'name': 'Ligue 1',
            'id': '13',
            'seasons': 7,
        },
        {
            'name': 'Bundesliga',
            'id': '20',
            'seasons': 7,
        },
        {
            'name': 'Primeira Liga',
            'id': '32',
            'seasons': 7,
        },
        {
            'name': 'Eredivisie',
            'id': '23',
            'seasons': 7,
        },
        {
            'name': 'Super Lig',
            'id': '26',
            'seasons': 7,
        },
        {
            'name': 'Belgian Pro League',
            'id': '37',
            'seasons': 5,
        },
        {
            'name': 'Championship',
            'id': '10',
            'seasons': 8,
        },
        {
            'name': 'Major League Soccer',
            'id': '22',
            'seasons': 8,
            'is_year': True,
        },
        {
            'name': 'Serie A',
            'id': '24',
            'seasons': 8,
            'is_year': True,
        },
        {
            'name': 'Danish Superliga',
            'id': '50',
            'seasons': 6,
        },
        {
            'name': 'Russian Premier League',
            'id': '30',
            'seasons': 7,
        },
        {
            'name': 'J1 League',
            'id': '25',
            'seasons': 9,
            'is_year': True,
        },
        {
            'name': 'Champions League',
            'id': '8',
            'seasons': 9,
        },
        {
            'name': 'Europa League',
            'id': '19',
            'seasons': 9,
        },
        {
            'name': 'FA Cup',
            'id': '514',
            'seasons': 7,
        },
        {
            'name': 'World Cup',
            'id': '1',
            'seasons': 2,
            'step': 4,
            'is_year': True,
        },
    ]
    data_league = pd.read_csv("leagues.csv")

    with SB(uc=True) as sb:
        for league in leagues:
            for s in range(league['seasons']):
                id = league['id']
                name = league['name'].replace(' ','-')
                season = f'{2025-s}' if 'is_year' in league else f'{2025-(s+1)}-{2025-s}'
                url = f'{domain}/en/comps/{id}/{season}/schedule/{season}-{name}-Scores-and-Fixtures'
                dict_season = {}

                open_url(sb, url)
                links = get_league_matches_links(sb, name, season)
                dict_season['league'] = league['name']
                dict_season['season'] = season
                dict_season['link'] = links

                league_season = pd.DataFrame.from_dict(dict_season)
                data_league = pd.concat([data_league, league_season])
                data_league.to_csv('leagues.csv', index=False)


if __name__ == '__main__':
    try:
        main()
    except HTTPError as e:
        print(e)
        time.sleep(5)
