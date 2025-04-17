import numpy as np

np.random.seed(0)

n_customers = 20
arrival_times = np.cumsum(np.random.exponential(scale=5, size=n_customers))
service_time = 3

start_service, end_service, waiting_times = [], [], []
server_idle_time = 0

for i, arrival in enumerate(arrival_times):
    start = arrival if i == 0 else max(arrival, end_service[i - 1])
    
    server_idle_time += max(0, arrival - (end_service[i - 1] if i > 0 else 0))
    
    end = start + service_time
    start_service.append(start)
    end_service.append(end)
    waiting_times.append(start - arrival)

avg_wait = np.mean(waiting_times)
max_wait = np.max(waiting_times)

print("\nCustomer Data:")
print(f"Arrival Times: {arrival_times.round(2)}")
print(f"Start of Service: {np.round(start_service, 2)}")
print(f"End of Service: {np.round(end_service, 2)}")
print(f"Waiting Times: {np.round(waiting_times, 2)}")

print("\nStatistics:")
print(f"Average Waiting Time: {avg_wait:.2f} minutes")
print(f"Maximum Waiting Time: {max_wait:.2f} minutes")
print(f"Total Server Idle Time: {server_idle_time:.2f} minutes")
