import requests
from datetime import datetime
IDS = []
endpoints = [
    "bootstrap-static",
    "fixtures",
    "element-summary/{element_id}",
    "event/{event_id}/live"
]

fixtures_url = f"https://fantasy.premierleague.com/api/{endpoints[1]}?future=1"
url = f"https://fantasy.premierleague.com/api/{endpoints[0]}"
res = requests.get(fixtures_url)
url_res = requests.get(url)
out = res.json()
output = url_res.json()
event = output.get('events')
for i in range(0, len(event)):
    data = event[i].get('id')
    IDS.append(data)
my_set = set()  # Define a set to store unique dates
event_li = []
for i in range(0, len(out)):
    data = out[i].get('kickoff_time')
    event_id = out[i].get('event')
    event_li.append(event_id)
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

# for date in sorted_dates:
    # print(date)

# for i in IDS:
#     print(i)

for a in event_li:
    print(a)