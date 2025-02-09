import pandas as pd
import matplotlib.pyplot as plt

# Load benchmark results
data = pd.read_csv("benchmark_results.csv")

# Plot execution time vs. number of clients for each server type
plt.figure(figsize=(10, 6))
for server_type in data['server_type'].unique():
    subset = data[data['server_type'] == server_type]
    plt.plot(subset['clients'], subset['execution_time'], label=server_type)

plt.title("Server Performance Benchmark")
plt.xlabel("Number of Clients")
plt.ylabel("Execution Time (seconds)")
plt.legend(title="Server Type")
plt.grid()
plt.show()
