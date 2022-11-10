import requests
import json

QUERY_URL = "http://localhost:8983/solr/news/select"

# Does Alex (author) write news about Russia?
params = {
    'q': 'author:Alex title:Russia (body_en:Russia OR body_fr:Russie OR body_de:Russland OR body_es:Rusia OR body_ru:Россия)',
    'indent': 'true',
    'q.op': 'AND',
    'wt': 'json',
    'rows': 10
}

results = requests.get(QUERY_URL, params=params).json()['response']['docs']

# Conspiracy fake news about the FBI
params = {
    'q': '(title:FBI OR body_fr:FBI OR body_en:FBI OR body_de:FBI OR body_es:FBI OR body_ru:FBI) AND type:conspiracy ' +
            '((title:FBI OR body_fr:FBI OR body_en:FBI OR body_de:FBI OR body_es:FBI OR body_ru:FBI) AND ' +
            '(body_fr:conspiration OR body_en:conspiracy OR body_de:verschwörung OR body_es:conspiración OR body_ru:конспирология))',
    'indent': 'true',
    'q.op': 'OR',
    'wt': 'json',
    'rows': 10
}

results = requests.get(QUERY_URL, params=params).json()['response']['docs']
for i in results:
    print(i['title'])

# What highly spammy news have there been about war?
params = {
    'q': 'title:war body_fr:guerre OR body_en:war OR body_de:krieg OR body_es:guerra OR body_ru:война',
    'indent': 'true',
    'q.op': 'OR',
    'sort': 'spam_score desc',
    'wt': 'json',
    'rows': 10
}

results = requests.get(QUERY_URL, params=params).json()['response']['docs']

# Fake news related to the presidential elections in the United States
params = {
    'q': 'country:US AND (title:"elections" OR body_fr:"élections" OR body_en:"elections" OR body_de:"wahlen" OR body_es:"elecciones" OR body_ru:"выборы" )' + 
            '',
    'indent': 'true',
    'q.op': 'OR',
    'wt': 'json',
    'rows': 10
}

results = requests.get(QUERY_URL, params=params).json()['response']['docs']

# Fake news in Colombia about the US
params = {
    'q': 'country:CO ' + 
            '((title:"United States" OR body_fr:"États Unis" OR body_en:"United States" OR body_de:"Vereinigte Staaten" OR body_es:"Estados Unidos" OR body_ru:"Соединенные Штаты") OR' + 
            '((title:"USA" OR body_fr:"USA" OR body_en:"USA" OR body_de:"USA" OR body_es:"USA" OR body_ru:"США")) OR' +
            '((title:"US" OR body_fr:"US" OR body_en:"US" OR body_de:"US" OR body_es:"US" OR body_ru:"США")))',
    'indent': 'true',
    'q.op': 'AND',
    'wt': 'json',
    'rows': 10
}

results = requests.get(QUERY_URL, params=params).json()['response']['docs']