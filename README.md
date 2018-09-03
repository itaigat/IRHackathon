# IRHackathon

## Code evaluation


### Time

In order to get your time score, replace the comments with your code for each section.

#### Indexing

```python
    start_indexing_time = time.time()
    '''
    
    Insert indexing functionality
    
    '''
    end_indexing_time = time.time()
```

#### Retrieval

```python
    start_retrieval_time = time.time()
    '''
    
    Insert retrieval functionality
    
    '''
    end_retrieval_time = time.time()
```

### Evaluation
In order to use the given evaluation class please go through the following stages:
```bash
   cd <project directory>/evaluator/trec_eval.9.0
   make
   cp trec_eval ../
```

The metrics we will use are: 

- MAP
- nDCG@20
- Precision@5
- Precision@10

In order to check your results with the metrics above you can use the code below: 


```python
    from evaluator.evaluate import Eval
    ...
    ...
    evaluation = Eval(trec_file)
    evaluation.run_evaluation()
```

Where:
- trec_file - Path to scores file
- Results of evaluation will be written in a file named "results_of_retrieval"

### Scores file format:
query-id Q0 document-id 1 score hackathon

For example:
- 750 Q0 GX261-61-14975000 1 0.333 hackathon
- 750 Q0 GX261-70-6119593 1 0.311 hackathon
- ...
- ...

**Important Note** - results file should be sorted by query - id(ascending), score(descending), document-id(descending).


### Relevance judgment file:
The file is located at data/qrels.gov2_train.all 
