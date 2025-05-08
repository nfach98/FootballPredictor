from seleniumbase import SB
import time
from urllib.error import HTTPError
import pandas as pd
import numpy as np
import re

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


def get_match_data(sb, url):
    data = {}
    open_url(sb, url)

    scorebox = sb.find_elements('div.scorebox > div > div > strong > a')
    teams = [a.text for a in scorebox][:2]
    data['H_team_name'] = teams[0]
    data['A_team_name'] = teams[1]
    
    league_divs = sb.find_elements('div#content > div')
    if (len(league_divs) > 0):
        leagues = league_divs[0].text.split('(')
        league = leagues[0].strip()
        try:
            round = leagues[1].replace(')', '')
            data['round'] = round
        except IndexError:
            data['round'] = None
        
        data['league'] = league

    score_divs = sb.find_elements('div.score')
    scores = [re.findall(r'\d+', s.text)[0] for s in score_divs if s.text != '']
    data['H_goals'] = int(scores[0])
    data['A_goals'] = int(scores[1])

    time_div = sb.find_element('span.venuetime')
    m_date = time_div.get_attribute('data-venue-date')
    m_time = time_div.get_attribute('data-venue-time')
    data["date"] = m_date
    data["time"] = m_time

    # try:
    #     att_div = sb.find_element('div.scorebox_meta > div:nth-child(5)')
    #     att = att_div.text.split(' ')[-1].replace(',', '')
    #     data["attendance"] = int(att)
    # except:
    #     data["attendance"] = 0

    h_og_divs = sb.find_elements('div#b > div > div.own_goal')
    a_og_divs = sb.find_elements('div#a > div > div.own_goal')
    data['H_own_goals'] = len(h_og_divs)
    data['A_own_goals'] = len(a_og_divs)

    stats_divs = sb.find_elements('div#team_stats > table > tbody > tr > td > div > div')
    stats = [s.text for s in stats_divs if s.text != '']
    
    data['H_possession'] = int(stats[0].replace("%",""))
    data['A_possession'] = int(stats[0].replace("%",""))
    
    stats_detail = stats[2:]
    stats_detail = np.array([s.split(' — ') for s in stats_detail]).flatten()
    stats_detail = [s.split(' of ') for s in stats_detail if '%' not in s]

    data['H_passes_completed'] = int(stats_detail[0][0])
    data['H_passes_total'] = int(stats_detail[0][1])
    data['A_passes_completed'] = int(stats_detail[1][0])
    data['A_passes_total'] = int(stats_detail[1][1])

    data['H_shots_on_target'] = int(stats_detail[2][0])
    data['H_shots_total'] = int(stats_detail[2][1])
    data['A_shots_on_target'] = int(stats_detail[3][0])
    data['A_shots_total'] = int(stats_detail[3][1])

    try:
        data['H_saves'] = int(stats_detail[4][0])
        data['A_saves'] = int(stats_detail[5][0])
    except:
        data['H_saves'] = 0
        data['A_saves'] = 0

    h_cards_selector = 'div#team_stats > table > tbody > tr:last-child > td:nth-child(1) > div > div > div > span'
    a_cards_selector = 'div#team_stats > table > tbody > tr:last-child > td:nth-child(2) > div > div > div > span'

    h_yellow = sb.find_elements(f'{h_cards_selector}.yellow_card')
    h_red = sb.find_elements(f'{h_cards_selector}.red_card')
    h_yellow_red = sb.find_elements(f'{h_cards_selector}.yellow_red_card')
    data['H_yellow_cards'] = len(h_yellow) + len(h_yellow_red)
    data['H_red_cards'] = len(h_red) + len(h_yellow_red)

    a_yellow = sb.find_elements(f'{a_cards_selector}.yellow_card')
    a_red = sb.find_elements(f'{a_cards_selector}.red_card')
    a_yellow_red = sb.find_elements(f'{a_cards_selector}.yellow_red_card')
    data['A_yellow_cards'] = len(a_yellow) + len(a_yellow_red)
    data['A_red_cards'] = len(a_red) + len(a_yellow_red)

    stats_extra_divs = sb.find_elements('div#team_stats_extra > div > div:not(.th)')
    stats_extra = [s.text for s in stats_extra_divs if s.text != '']
    stats_extra = np.reshape(stats_extra, (-1, 3))

    data['H_fouls'] = int(stats_extra[0][0])
    data['A_fouls'] = int(stats_extra[0][2])

    data['H_corners'] = int(stats_extra[1][0])
    data['A_corners'] = int(stats_extra[1][2])

    data['H_crosses'] = int(stats_extra[2][0])
    data['A_crosses'] = int(stats_extra[2][2])

    data['H_touches'] = int(stats_extra[3][0])
    data['A_touches'] = int(stats_extra[3][2])

    data['H_tackles'] = int(stats_extra[4][0])
    data['A_tackles'] = int(stats_extra[4][2])

    data['H_interceptions'] = int(stats_extra[5][0])
    data['A_interceptions'] = int(stats_extra[5][2])

    data['H_aerials_won'] = int(stats_extra[6][0])
    data['A_aerials_won'] = int(stats_extra[6][2])

    data['H_clearances'] = int(stats_extra[7][0])
    data['A_clearances'] = int(stats_extra[7][2])

    data['H_offsides'] = int(stats_extra[8][0])
    data['A_offsides'] = int(stats_extra[8][2])

    data['H_goal_kicks'] = int(stats_extra[9][0])
    data['A_goal_kicks'] = int(stats_extra[9][2])

    data['H_throw_ins'] = int(stats_extra[10][0])
    data['A_throw_ins'] = int(stats_extra[10][2])

    data['H_long_balls'] = int(stats_extra[11][0])
    data['A_long_balls'] = int(stats_extra[11][2])

    return data


def main():
    links = pd.read_csv('leagues.csv')
    matches = pd.read_csv('matches_new.csv')
    notes = pd.read_csv('notes.csv')
    idx_start = 5816

    with SB(uc=True) as sb:
        for i in range(idx_start, len(links)):
            try:
                row = links.iloc[i]
                match = get_match_data(sb, row['link'])
                match['season'] = row['season']
                df_match = pd.DataFrame([match])

                matches = pd.concat([matches, df_match], ignore_index=True)
                matches.to_csv('matches_new.csv', index=False)
            except Exception as e:
                notes_new = pd.DataFrame([{'index': i, 'notes': str(e)}])
                notes = pd.concat([notes, notes_new], ignore_index=True)
                notes.to_csv('notes.csv', index=False)


if __name__ == '__main__':
    try:
        main()
    except HTTPError as e:
        print(e)
        time.sleep(5)
