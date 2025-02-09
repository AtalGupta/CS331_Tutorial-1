
## Problem 1: Multi-Functional Socket Server

**Description:**  
The first problem demonstrates a socket server that can perform multiple tasks based on user input. The server accepts a connection from a client and supports the following operations:
- **Change the case of a string:** Toggle uppercase to lowercase and vice versa.
- **Evaluate a mathematical expression:** Compute the result of the given expression.
- **Find the reverse of a given string:** Return the string in reverse order.

**Files:**
- `Problem 1/client.py` - Implements the client operations that send requests to the server.
- `Problem 1/server.py` - Implements the server with support for single-process, multi-process, and multi-threaded modes.

## Problem 2: Benchmarking Server Performance

**Description:**  
The second problem focuses on benchmarking the performance of different server implementations that handle client requests by reversing a string. The server supports three modes:
- **Single Process:** Handles one client at a time.
- **Multi-process:** Spawns a new process for each client.
- **Multi-threaded:** Creates a new thread for each client.

Benchmarking is performed by running multiple concurrent client requests and measuring the execution time. The benchmarking workflow is automated by a shell script and results are visualized using a Python script.

**Files:**
- `Problem 2/client.py` - Implements a simple client that sends a string to the server and prints the reversed result.
- `Problem 2/server.py` - Implements the server with different concurrency models.
- `Problem 2/start.sh` - A shell script to execute the client script concurrently for benchmarking.
- `Problem 2/benchmark.py` - Automates the benchmarking process by looping through server types and different numbers of clients.
- `Problem 2/benchmark_results.csv` - Stores the benchmarking results.
- `Problem 2/visualization.py` - Loads the benchmark results and creates a plot of execution time versus number of clients for each server type.
