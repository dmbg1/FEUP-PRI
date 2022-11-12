import requests
import json
import pandas as pd
from sklearn.metrics import PrecisionRecallDisplay
import matplotlib.pyplot as plt
import numpy as np

QUERY_URL = "http://localhost:8983/solr/news/select"
QUERY_URL_NO_SCHEMA = "http://localhost:8983/solr/news_without_schema/select"

# Does Alex (author) write news about Russia?
params = {
    'q': 'author:Alex (title:Russia OR body_en:Russia)',
    'indent': 'true',
    'q.op': 'AND',
    'defType': 'edismax',
    'qf': 'title^2',
    'wt': 'json',
    'rows': 20
}
results = requests.get(QUERY_URL, params=params).json()['response']['docs']

# Serializing json
json_object = json.dumps(results, indent=4)

# Writing to sample.json
with open("./M2/queries/schema/q1.json", "w+") as outfile:
    outfile.write(json_object)

# Conspiracy fake news about the FBI
params = {
    'q': '(title:FBI OR body_en:FBI) (type:conspiracy OR (title:conspiracy OR body_en:conspiracy))',
    'indent': 'true',
    'q.op': 'AND',
    'defType': 'edismax',
    'qf': 'type^2',
    'wt': 'json',
    'rows': 20
}

results = requests.get(QUERY_URL, params=params).json()['response']['docs']

# Serializing json
json_object = json.dumps(results, indent=4)

# Writing to sample.json
with open("./M2/queries/schema/q2.json", "w+") as outfile:
    outfile.write(json_object)

# What highly spammy news have there been about war?
params = {
    'q': 'title:war body_en:war',
    'indent': 'true',
    'q.op': 'OR',
    'defType': 'edismax',
    'qf': 'title^2',
    'fq': 'spam_score:[0.8 TO *]',
    'wt': 'json',
    'rows': 20
}
results = requests.get(QUERY_URL, params=params).json()['response']['docs']

# Serializing json
json_object = json.dumps(results, indent=4)

# Writing to sample.json
with open("./M2/queries/schema/q3.json", "w+") as outfile:
    outfile.write(json_object)

# Fake news related to the presidential elections in the United States
params = {
    'q': '(country:US AND (title:elections OR body_en:elections))^=2' + 
            '((title:elections OR body_en:elections) AND (title:"United States" OR body_en:"United States"))^=1',
    'indent': 'true',
    'q.op': 'OR',
    'wt': 'json',
    'rows': 20
}

results = requests.get(QUERY_URL, params=params).json()['response']['docs']

# Serializing json
json_object = json.dumps(results, indent=4)

# Writing to sample.json
with open("./M2/queries/schema/q4.json", "w+") as outfile:
    outfile.write(json_object)

# Fake news in Colombia about the US
#'(title:"United States" OR body_en:"United States" OR title:"USA" OR body_en:"USA" OR title:"US"^0.5 OR body_en:"US"^0.5)',
params = {
    'q': 'country:CO AND (body_en:US OR title:US)',
    'indent': 'true',
    'q.op': 'AND',
    'wt': 'json',
    'rows': 20
}

results = requests.get(QUERY_URL, params=params).json()['response']['docs']

# Serializing json
json_object = json.dumps(results, indent=4)

# Writing to sample.json
with open("./M2/queries/schema/q5.json", "w+") as outfile:
    outfile.write(json_object)

'''
NO SCHEMA - NO WEIGHTS
SCHEMA - NO WEIGHTS
'''

# Does Alex (author) write news about Russia?
params = {
    'q': 'author:Alex (title:Russia OR body_en:Russia)',
    'indent': 'true',
    'q.op': 'AND',
    'wt': 'json',
    'rows': 20
}
results_no_schema = requests.get(QUERY_URL_NO_SCHEMA, params=params).json()['response']['docs']
results = requests.get(QUERY_URL, params=params).json()['response']['docs']

# Serializing json
json_object_no_schema = json.dumps(results_no_schema, indent=4)
json_object = json.dumps(results, indent=4)

# Writing to sample.json
with open("./M2/queries/noSchema/q1.json", "w+") as outfile:
    outfile.write(json_object_no_schema)
with open("./M2/queries/noWeights/q1.json", "w+") as outfile:
    outfile.write(json_object)
    
    
# Conspiracy fake news about the FBI
params = {
    'q': '(title:FBI OR body_en:FBI) (type:conspiracy OR (title:conspiracy OR body_en:conspiracy))',
    'indent': 'true',
    'q.op': 'AND',
    'wt': 'json',
    'rows': 20
}
results_no_schema = requests.get(QUERY_URL_NO_SCHEMA, params=params).json()['response']['docs']
results = requests.get(QUERY_URL, params=params).json()['response']['docs']

# Serializing json
json_object_no_schema = json.dumps(results_no_schema, indent=4)
json_object = json.dumps(results, indent=4)

# Writing to sample.json
with open("./M2/queries/noSchema/q2.json", "w+") as outfile:
    outfile.write(json_object_no_schema)
with open("./M2/queries/noWeights/q2.json", "w+") as outfile:
    outfile.write(json_object)
    

# What highly spammy news have there been about war?
params = {
    'q': 'title:war body_en:war',
    'indent': 'true',
    'q.op': 'OR',
    'fq': 'spam_score:[0.8 TO *]',
    'wt': 'json',
    'rows': 20
}
results_no_schema = requests.get(QUERY_URL_NO_SCHEMA, params=params).json()['response']['docs']
results = requests.get(QUERY_URL, params=params).json()['response']['docs']

# Serializing json
json_object_no_schema = json.dumps(results_no_schema, indent=4)
json_object = json.dumps(results, indent=4)

# Writing to sample.json
with open("./M2/queries/noSchema/q3.json", "w+") as outfile:
    outfile.write(json_object_no_schema)
with open("./M2/queries/noWeights/q3.json", "w+") as outfile:
    outfile.write(json_object)

# Fake news related to the presidential elections in the United States
params = {
    'q': 'country:US AND (title:elections OR body_en:elections)' + 
            '(title:elections OR body_en:elections) AND (title:"United States" OR body_en:"United States")',
    'indent': 'true',
    'q.op': 'OR',
    'wt': 'json',
    'rows': 20
}

results_no_schema = requests.get(QUERY_URL_NO_SCHEMA, params=params).json()['response']['docs']
results = requests.get(QUERY_URL, params=params).json()['response']['docs']

# Serializing json
json_object_no_schema = json.dumps(results_no_schema, indent=4)
json_object = json.dumps(results, indent=4)

# Writing to sample.json
with open("./M2/queries/noSchema/q4.json", "w+") as outfile:
    outfile.write(json_object_no_schema)
with open("./M2/queries/noWeights/q4.json", "w+") as outfile:
    outfile.write(json_object)


# Fake news in Colombia about the US
#'(title:"United States" OR body_en:"United States" OR title:"USA" OR body_en:"USA" OR title:"US"^0.5 OR body_en:"US"^0.5)',
params = {
    'q': 'country:CO AND (body_en:US OR title:US)',
    'indent': 'true',
    'q.op': 'AND',
    'wt': 'json',
    'rows': 20
}

results_no_schema = requests.get(QUERY_URL_NO_SCHEMA, params=params).json()['response']['docs']
results = requests.get(QUERY_URL, params=params).json()['response']['docs']

# Serializing json
json_object_no_schema = json.dumps(results_no_schema, indent=4)
json_object = json.dumps(results, indent=4)

# Writing to sample.json
with open("./M2/queries/noSchema/q5.json", "w+") as outfile:
    outfile.write(json_object_no_schema)
with open("./M2/queries/noWeights/q5.json", "w+") as outfile:
    outfile.write(json_object)


'''

PRECISION RECALL

'''

relevant = []

def precision_recall(results, relevant, query_num):
    # PRECISION-RECALL CURVE
    # Calculate precision and recall values as we move down the ranked list
    precision_values = [
        len([
            doc 
            for doc in results[:idx]
            if doc['id'] in relevant
        ]) / idx 
        for idx, _ in enumerate(results, start=1)
    ]

    recall_values = [
        len([
            doc for doc in results[:idx]
            if doc['id'] in relevant
        ]) / len(relevant)
        for idx, _ in enumerate(results, start=1)
    ]

    precision_recall_match = {k: v for k,v in zip(recall_values, precision_values)}

    # Extend recall_values to include traditional steps for a better curve (0.1, 0.2 ...)
    recall_values.extend([step for step in np.arange(0.1, 1.1, 0.1) if step not in recall_values])
    recall_values = sorted(set(recall_values))

    # Extend matching dict to include these new intermediate steps
    for idx, step in enumerate(recall_values):
        if step not in precision_recall_match:
            if recall_values[idx-1] in precision_recall_match:
                precision_recall_match[step] = precision_recall_match[recall_values[idx-1]]
            else:
                precision_recall_match[step] = precision_recall_match[recall_values[idx+1]]

    disp = PrecisionRecallDisplay([precision_recall_match.get(r) for r in recall_values], recall_values)
    disp.plot()
    plt.savefig('precision_recall' + query_num + '.pdf')
