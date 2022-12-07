import json
import pandas as pd
from sklearn.metrics import PrecisionRecallDisplay
import matplotlib.pyplot as plt
import numpy as np


def metrics(query_num):
    # Relevant Total
    all_relevant = list(map(lambda el: el.strip(), open("./M3/queries/q" + str(query_num) + "_rels.txt").readlines()))
    #print(relevant)
    
    # Open result files
    with open("./M3/queries/schema/q" + str(query_num) + ".json") as json_file:
        results_normal = json.load(json_file)
        
    
    all_results = [results_normal]
    
    _, ax = plt.subplots(figsize=(5, 5))
    
    for index in range(len(all_results)):
        results = all_results[index]
        metrics = {}
        metric = lambda f: metrics.setdefault(f.__name__, f)
        # Relevants for this index
        relevant = [doc['id'] for doc in results
                if doc['id'] in all_relevant]

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
            with open('./M3/results/results_normal_q' + str(query_num) + '.tex','w') as tf:
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
        print(precision_values)
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
            disp.plot(ax=ax, name="Schema & Modifiers", color="lime")
                
    
    ax.set_title("Precision-Recall Curve")

    plt.ylim((0, 1.1))
    
    plt.savefig('./M3/results/precision_recall_q' + str(query_num) + '.pdf')


metrics(1)
metrics(2)
metrics(3)
metrics(4)