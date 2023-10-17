#!/usr/bin/env python3
"""testing api"""

from config import db
from api.v1.views import app
import requests
import json


@app.route('/fetch_and_store_data')
def fetch_and_store_data():
    # Define the API endpoint
    api_url = 'https://api.github.com/users'

    # Make an API GET request
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = json.loads(response.text)

        # Insert data into the database
        for user in data:
            github_user = GitHubUser(login=user['login'], url=user['url'])
            db.session.add(github_user)

        # Commit the changes to the database
        db.session.commit()

        return 'Data fetched and stored successfully!'
    else:
        return f"API request failed with status code: {response.status_code}"
