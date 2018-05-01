import requests

url = 'https://catfact.ninja/facts'

def get_facts(number):

    facts = requests.get(url, {'limit': number}).json()
    return facts['data']  # todo error handling
