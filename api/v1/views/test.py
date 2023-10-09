import requests

response = requests.get("https://fantasy.premierleague.com/api/")
# print(response.status_code)
# print(response.text)
# res = response.json()
# print(res['films'])
print(response)
print(dir(response))


