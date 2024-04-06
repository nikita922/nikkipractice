import threading

# Define a function that will be executed in the thread
def my_thread_function():
    print("Thread is running")

# Create a thread object and pass the function to it
my_thread = threading.Thread(target=my_thread_function)

# Start the thread
my_thread.start()

# You can do other work here in the main thread
print("Main thread continues to run")

# Wait for the thread to finish (if needed)
my_thread.join()

# The program continues to execute here
print("Main thread has finished")
