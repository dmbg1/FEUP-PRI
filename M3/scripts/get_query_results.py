import requests
import json

QUERY_URL = "http://localhost:8983/solr/news/select"

# Does Alex (author) write news about Russia?
Q1_PARAMS = {
    'q': 'author:Alex AND Russia',
    'indent': 'true',
    'q.op': 'AND',
    'defType': 'edismax',
    'qf': 'title^2 body_en',
    'wt': 'json',
    'rows': 20
}
# Conspiracy fake news about the FBI
Q2_PARAMS = {
    'q': 'FBI conspiracy',
    'indent': 'true',
    'q.op': 'AND',
    'defType': 'edismax',
    'qf': 'type^4 title^2 body_en',
    'wt': 'json',
    'rows': 20
}
# What highly spammy news have there been about war?
Q3_PARAMS = {
    'q': 'war',
    'indent': 'true',
    'q.op': 'OR',
    'defType': 'edismax',
    'qf': 'title^2 body_en',
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
    'qf': 'title^2 body_en',
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
    query_results = requests.get(query_url, params=query_params)
    
    # Serializing json
    json_object = json.dumps(query_results, indent=4)
    
    # Writing to sample.json
    with open(results_file_path, "w+") as outfile:
        outfile.write(json_object)


query_solr(QUERY_URL, Q1_PARAMS, "./M3/queries/schema/q1.json")
query_solr(QUERY_URL, Q2_PARAMS, "./M3/queries/schema/q2.json")
query_solr(QUERY_URL, Q3_PARAMS, "./M3/queries/schema/q3.json")
query_solr(QUERY_URL, Q4_PARAMS, "./M3/queries/schema/q4.json")
# query_solr(QUERY_URL, Q5_PARAMS, "./M3/queries/schema/q5.json")
