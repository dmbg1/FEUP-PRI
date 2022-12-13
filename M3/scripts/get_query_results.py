import requests
import json
from translate_all import translate_query

QUERY_URL = "http://localhost:8983/solr/news/select"

# Does Alex (author) write news about Russia?
Q1_PARAMS = {
    'q': 'author:Alex AND Russia',
    'indent': 'true',
    'q.op': 'AND',
    'defType': 'edismax',
    'qf': 'title_en^2 title_es^2 title_de^2 title_fr^2 title_ru^2 body_en body_es body_de body_fr body_ru',
    'fl': 'title_en, title_es, title_de, title_fr, title_ru, body_en, body_es, body_de, body_fr, body_ru score',
    'wt': 'json',
    'rows': 20
}
# Conspiracy fake news about the FBI
Q2_PARAMS = {
    'q': 'FBI conspiracy',
    'indent': 'true',
    'q.op': 'AND',
    'defType': 'edismax',
    'qf': 'title_en^2 title_es^2 title_de^2 title_fr^2 title_ru^2 body_en body_es body_de body_fr body_ru',
    'fl': 'title_en, title_es, title_de, title_fr, title_ru, body_en, body_es, body_de, body_fr, body_ru score',
    'wt': 'json',
    'rows': 20
}
# What highly spammy news have there been about war?
Q3_PARAMS = {
    'q': 'war',
    'indent': 'true',
    'q.op': 'OR',
    'defType': 'edismax',
    'qf': 'title_en^2 title_es^2 title_de^2 title_fr^2 title_ru^2 body_en body_es body_de body_fr body_ru',
    'fl': 'title_en, title_es, title_de, title_fr, title_ru, body_en, body_es, body_de, body_fr, body_ru score',
    'fq': 'spam_score:[0.8 TO *]',
    'wt': 'json',
    'rows': 20
}
# Fake news related to the presidential elections in the United States
Q4_PARAMS = {
    'q': '(country:US AND "presidential elections"~5) "american elections"~4',
    'indent': 'true',
    'q.op': 'OR',
    'defType': 'edismax',
    'qf': 'title_en^2 title_es^2 title_de^2 title_fr^2 title_ru^2 body_en body_es body_de body_fr body_ru',
    'fl': 'title_en, title_es, title_de, title_fr, title_ru, body_en, body_es, body_de, body_fr, body_ru score',
    'wt': 'json',
    'rows': 20
}
# Fake news in Colombia about the US
Q5_PARAMS = {
    'q': 'country:CO AND (body_en:US OR title:US)',
    'indent': 'true',
    'q.op': 'AND',
    'wt': 'json',
    'rows': 20
}

def query_solr(query_url, query_params, results_file_path):
    """ query_results = requests.get(query_url, params=query_params)
    
    # Serializing json
    json_object = json.dumps(query_results, indent=4)
    
    # Writing to sample.json
    with open(results_file_path, "w+") as outfile:
        outfile.write(json_object) """
        
    all_results = []
        
    regular_query = query_params['q']
    
    query_params['q'] = translate_query(regular_query, 'en')
    query_results = requests.get(query_url, params=query_params).json()['response']['docs']
    for result in query_results:
        all_results.append(result)
    
    query_es = translate_query(regular_query, 'es')
    query_params['q'] = query_es
    query_results = requests.get(query_url, params=query_params).json()['response']['docs']
    for result in query_results:
        all_results.append(result)
    
    query_fr = translate_query(regular_query, 'fr')
    query_params['q'] = query_fr
    query_results = requests.get(query_url, params=query_params).json()['response']['docs']
    for result in query_results:
        all_results.append(result)
    
    query_de = translate_query(regular_query, 'de')
    query_params['q'] = query_de
    query_results = requests.get(query_url, params=query_params).json()['response']['docs']
    for result in query_results:
        all_results.append(result)
    
    query_ru = translate_query(regular_query, 'ru')
    query_params['q'] = query_ru
    query_results = requests.get(query_url, params=query_params).json()['response']['docs']
    for result in query_results:
        all_results.append(result)
    
    all_results.sort(key=lambda x: int(x['score']), reverse=True)
    
    with open(results_file_path, "w+") as outfile:
        for i in range(20):
            outfile.write(json.dumps(all_results[i], indent=4))
            outfile.write(",\n")


query_solr(QUERY_URL, Q1_PARAMS, "./M3/queries/q1.json")
query_solr(QUERY_URL, Q2_PARAMS, "./M3/queries/q2.json")
query_solr(QUERY_URL, Q3_PARAMS, "./M3/queries/q3.json")
query_solr(QUERY_URL, Q4_PARAMS, "./M3/queries/q4.json")
#query_solr(QUERY_URL, Q5_PARAMS, "./M3/queries/q5.json")
