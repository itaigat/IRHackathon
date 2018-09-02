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

### Metrics

The metrics we will use are: 

- MAP
- nDCG@20
- Precision@5
- Precision@10

In order to check your results with the metrics above you can use the code below: 


```python
    evaluation = Eval(trec_file, qrels)
```

Where:
- trec_file - Path to
- qrels - 
