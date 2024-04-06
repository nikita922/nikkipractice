import threading

# Shared resource (a counter)
counter = 0

# Define a lock for synchronization
counter_lock = threading.Lock()

# Function to increment the counter safely
def increment_counter():
    global counter
    with counter_lock:
        for _ in range(1000000):
            counter += 1

# Create two threads to increment the counter
thread1 = threading.Thread(target=increment_counter)
thread2 = threading.Thread(target=increment_counter)

# Start both threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

# Print the final counter value
print("Final counter value:", counter)
