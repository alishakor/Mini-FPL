from flask import render_template
from routes import fixtures_bp
from datetime import datetime

import requests

api_url = "https://fantasy.premierleague.com/api/bootstrap-static/"


@fixtures_bp.route('/fixtures', methods=['GET', 'POST'], strict_slashes=False)
def index():
    endpoints = [
        "bootstrap-static",
        "fixtures",
        "element-summary/{element_id}",
        "event/{event_id}/live"
    ]

    players_url = f"https://fantasy.premierleague.com/api/{endpoints[1]}?future=1"
    res = requests.get(players_url)
    out = res.json()

    my_set = set()  # Define a set to store unique dates

    for i in range(0, len(out)):
        data = out[i].get('kickoff_time')
        time = (data.split('T'))[0].split('-')
        year, month, day = (time[0], time[1], time[2])
        year = int(year)
        month = int(month)
        day = int(day)
        date_obj = datetime(year, month, day)

        # Format the date including the day of the week
        date_in_words = date_obj.strftime("%A %d %B %Y")

        my_set.add(date_in_words)  # Add the formatted date to the set

    # Convert the set to a list
    date_list = list(my_set)

    # Sort the list chronologically
    sorted_dates = sorted(date_list, key=lambda x: datetime.strptime(x, "%A %d %B %Y"))
    return render_template('fixtures.html', sorted_dates=sorted_dates)



def get_fixtures_data():
    """ Retrieve the fixtures data for the season
    """
    # url = "https://fantasy.premierleague.com/api/fixtures/"
    # response = ''
    # while response == '':
    #     try:
    #         response = requests.get(url)
    #     except:
    #         time.sleep(5)
    # if response.status_code != 200:
    #     raise Exception("Response was code " + str(response.status_code))
    # data = json.loads(response.text)
    # return data

