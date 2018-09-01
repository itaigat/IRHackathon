import time

if __name__ == "__main__":
    start_time_indexing = time.process_time()
    #insert indexing functionality
    end_time_indexing = time.process_time()

    start_retrieval_time = time.process_time()
    # insert retrieval functionality
    end_retrieval_time = time.process_time()

    elapsed_time = time.process_time() - start_time_indexing
    