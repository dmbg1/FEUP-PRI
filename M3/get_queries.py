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
    'q': 'author:Alex AND Russia',
    'indent': 'true',
    'q.op': 'AND',
    'defType': 'edismax',
    'qf': 'title^2 body_en',
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
    'q': 'FBI conspiracy',
    'indent': 'true',
    'q.op': 'AND',
    'defType': 'edismax',
    'qf': 'type^4 title^2 body_en',
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
    'q': 'war',
    'indent': 'true',
    'q.op': 'OR',
    'defType': 'edismax',
    'qf': 'title^2 body_en',
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
    'q': '(country:US AND "presidential elections"~5) "american elections"~4',
    'indent': 'true',
    'q.op': 'OR',
    'defType': 'edismax',
    'qf': 'title^2 body_en',
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
    'q': 'author:Alex AND Russia',
    'indent': 'true',
    'q.op': 'AND',
    'defType': 'edismax',
    'qf': 'title body_en',
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
    'q': 'FBI conspiracy',
    'indent': 'true',
    'q.op': 'AND',
    'defType': 'edismax',
    'qf': 'type title body_en',
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
    'q': 'war',
    'indent': 'true',
    'q.op': 'OR',
    'defType': 'edismax',
    'qf': 'title body_en',
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
    'q': '(country:US AND "presidential elections") "american elections"',
    'indent': 'true',
    'q.op': 'OR',
    'defType': 'edismax',
    'qf': 'title body_en',
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

def metrics(query_num):
    # Relevant
    relevant = list(map(lambda el: el.strip(), open("./M2/queries/q" + str(query_num) + "_rels.txt").readlines()))
    #print(relevant)
    
    # Open result files
    with open("./M2/queries/noSchema/q" + str(query_num) + ".json") as json_file:
        results_no_schema = json.load(json_file)
    with open("./M2/queries/noWeights/q" + str(query_num) + ".json") as json_file:
        results_no_weights = json.load(json_file)
    with open("./M2/queries/schema/q" + str(query_num) + ".json") as json_file:
        results_normal = json.load(json_file)
        
    
    all_results = [results_no_schema, results_no_weights, results_normal]
    
    _, ax = plt.subplots(figsize=(5, 5))
    
    for index in range(len(all_results)):
        print(index)
        results = all_results[index]
        metrics = {}
        metric = lambda f: metrics.setdefault(f.__name__, f)

        @metric
        def ap(results, relevant):
            """Average Precision"""
            precision_values = [
                len([
                    doc 
                    for doc in results[:idx]
                    if doc['id'] in relevant
                ]) / idx 
                for idx in range(1, len(results))
            ]
            print(precision_values)
            return sum(precision_values)/len(precision_values)

        @metric
        def p10(results, relevant, n=10):
            """Precision at N"""
            return len([doc for doc in results[:n] if doc['id'] in relevant])/n

        def calculate_metric(key, results, relevant):
            return metrics[key](results, relevant)

        # Define metrics to be calculated
        evaluation_metrics = {
            'ap': 'Average Precision',
            'p10': 'Precision at 10 (P@10)'
        }

        # Calculate all metrics and export results as LaTeX table
        df = pd.DataFrame([['Metric','Value']] +
            [
                [evaluation_metrics[m], calculate_metric(m, results, relevant)]
                for m in evaluation_metrics
            ]
        )
        
        if(index == 0):
            with open('results_no_schema_q' + str(query_num) + '.tex','w') as tf:
                tf.write(df.to_latex())
        elif(index == 1):
            with open('results_no_weights_q' + str(query_num) + '.tex','w') as tf:
                tf.write(df.to_latex())
        elif(index == 2):
            with open('results_normal_q' + str(query_num) + '.tex','w') as tf:
                tf.write(df.to_latex())

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
        
        if(index == 0):
            disp.plot(ax=ax, name="No Schema", color="red")
        elif(index == 1):
            if(query_num == 2 or query_num == 3 or query_num == 1 ):
                disp.plot(ax=ax, name="No Modifiers", color="blue", linestyle="--", dashes=(5, 15))
            else: 
                disp.plot(ax=ax, name="No Modifiers", color="blue", linestyle="--", dashes=(5, 5))
        elif(index == 2):
            if(query_num == 2 or query_num == 3 or query_num == 1):
                disp.plot(ax=ax, name="Schema & Modifiers", color="lime", linestyle="--", dashes=(5, 15))
            else: 
                disp.plot(ax=ax, name="Schema & Modifiers", color="lime", linestyle="--", dashes=(5, 5))
                
    
    ax.set_title("Precision-Recall Curve")
    
    if(query_num == 2 or query_num == 3):
        plt.legend(loc='upper right')
    elif(query_num == 4):
        plt.legend(bbox_to_anchor=(0.45, 0.7))
    
    plt.savefig('precision_recall_q' + str(query_num) + '.pdf')


# metrics(1)
# metrics(2)
# metrics(3)
metrics(4)