from evaluator.evaluate import Eval
import time

if __name__ == "__main__":
    trec_file = ''

    start_indexing_time = time.time()
    '''
    
    Insert indexing functionality
    
    '''
    end_indexing_time = time.time()

    start_retrieval_time = time.time()
    '''
    
    Insert retrieval functionality
    
    '''
    end_retrieval_time = time.time()

    evaluation = Eval(trec_file)
    evaluation.run_evaluation()

    elapsed_index_time = end_indexing_time - start_indexing_time
    elapsed_retrieval_time = end_retrieval_time - start_retrieval_time
    elapsed_time = elapsed_retrieval_time + elapsed_retrieval_time

    print('Total running time: ', elapsed_time)
    print('Indexing running time: ', elapsed_index_time)
    print('Retrieval running time: ', elapsed_retrieval_time)
