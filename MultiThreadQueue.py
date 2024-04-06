import queue
import threading
import time
import random

# Create a priority queue
priority_queue = queue.PriorityQueue()
# Create a flag to signal the retrieval thread to stop
stop_retrieval = threading.Event()

# Function to insert items into the priority queue
def insert_into_queue():
    for i in range(5):
        item = random.randint(1, 100)
        priority_queue.put((item, f"Item {item}"))
        time.sleep(1)

# Function to retrieve items from the priority queue
def retrieve_from_queue():
    while not stop_retrieval.is_set():
        try:
            item = priority_queue.get(timeout=1)
            print(f"Retrieved: {item[1]}")
            priority_queue.task_done()
        except queue.Empty:
            continue

# Create multiple threads for inserting and retrieving items
insert_thread = threading.Thread(target=insert_into_queue)
retrieve_thread = threading.Thread(target=retrieve_from_queue)

# Start the threads
insert_thread.start()
retrieve_thread.start()

# Wait for the insert_thread to finish
insert_thread.join()

# Set the stop_retrieval flag to signal the retrieve_thread to stop
stop_retrieval.set()

# Wait for the retrieve_thread to finish
retrieve_thread.join()
