import requests
import json

QUERY_URL = "http://localhost:8983/solr/news/select"

# Does Alex (author) write news about Russia?
params = {
    'q': 'author:Alex (title:Russia OR body_en:Russia)',
    'indent': 'true',
    'q.op': 'AND',
    'defType': 'edismax',
    'qf': 'title^2',
    'wt': 'json',
    'rows': 10
}

results = requests.get(QUERY_URL, params=params).json()['response']['docs']

# Conspiracy fake news about the FBI
params = {
    'q': '((title:FBI OR body_en:FBI) AND type:conspiracy)^=2' +
            '((title:FBI OR body_en:FBI) AND (title:conspiracy OR body_en:conspiracy))^=1',
    'indent': 'true',
    'q.op': 'OR',
    'wt': 'json',
    'rows': 10
}

results = requests.get(QUERY_URL, params=params).json()['response']['docs']

# What highly spammy news have there been about war?
params = {
    'q': 'title:war body_en:war',
    'indent': 'true',
    'q.op': 'OR',
    'defType': 'edismax',
    'qf': 'title^2',
    'fq': 'spam_score:[0.8 TO *]',
    'wt': 'json',
    'rows': 1000
}

results = requests.get(QUERY_URL, params=params).json()['response']['docs']
print(len(results))

# Fake news related to the presidential elections in the United States
# NEEDS TO BE FINISHED
params = {
    'q': 'country:US AND (title:"elections" OR body_en:"elections")' + 
            '(title:"elections" OR body_en:"elections")',
    'indent': 'true',
    'q.op': 'OR',
    'wt': 'json',
    'rows': 10
}

results = requests.get(QUERY_URL, params=params).json()['response']['docs']

# Fake news in Colombia about the US
params = {
    'q': 'country:CO ' + 
            '((title:"United States" OR body_en:"United States") OR' + 
            '((title:"USA" OR body_en:"USA") OR' +
            '((title:"US" OR body_en:"US")^=0.5))',
    'indent': 'true',
    'q.op': 'AND',
    'wt': 'json',
    'rows': 10
}

results = requests.get(QUERY_URL, params=params).json()['response']['docs']