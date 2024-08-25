import psutil
import os
import time


# Function to get the current memory usage in MiB
def memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 * 1024)  # Convert bytes to MiB

# Decorator to profile memory usage of a function
def profile_memory(func):
    def wrapper(*args, **kwargs):
        mem_before = memory_usage()
        print(f"Memory before function: {mem_before:.2f} MiB")
        
        result = func(*args, **kwargs)
        
        mem_after = memory_usage()
        print(f"Memory after function: {mem_after:.2f} MiB")
        print(f"Memory used: {mem_after - mem_before:.2f} MiB")
        
        return result
    return wrapper

# Example function to profile
@profile_memory
def example_function():
    print("Function started.")
    a = [i for i in range(10000)]  # Large list to consume memory
    time.sleep(2)  # Simulate a time-consuming task
    b = sum(a)
    print("Function completed.")
    return b


if __name__ == "__main__":
    example_function()
