import os
import requests

TOKEN = os.getenv("TOKEN")
HEADERS = {'Authorization': f'Bearer {TOKEN}'}
API_URL = "https://api.github.com/repos/boto/boto3/pulls"

print(TOKEN)
def get_pull_json(state):
    params = {'state': state, 'per_page': 100}
    r = requests.get(API_URL, headers=HEADERS, params=params)
    pull_requests = r.json()

    return pull_requests


def get_pull_requests(state):
    
    pull_requests = get_pull_json(state)

    formatted_pull_requests = []
    for key in pull_requests:
        title = key['title']
        number = key['number']
        link = key['html_url']
        formatted_pull_request = {'title': title, 'num': number, 'link': link}
        formatted_pull_requests.append(formatted_pull_request)

    return formatted_pull_requests

