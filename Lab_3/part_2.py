import random
from collections import deque

def bank_queue_simulation(sim_time=60, arrival_rate=0.2, service_time=5, tellers=2):
    queue = deque()
    current_time = 0
    teller_busy_until = [0] * tellers
    wait_times = []

    while current_time < sim_time:
        # Random customer arrival
        if random.random() < arrival_rate:
            queue.append(current_time)

        # Assign tellers if available
        for i in range(tellers):
            if teller_busy_until[i] <= current_time and queue:
                arrival = queue.popleft()
                wait_times.append(current_time - arrival)
                teller_busy_until[i] = current_time + service_time

        current_time += 1

    # Summary statistics
    avg_wait = sum(wait_times) / len(wait_times) if wait_times else 0
    print(f"Tellers: {tellers}")
    print(f"Average Wait Time: {avg_wait:.2f} minutes")
    print(f"Total Customers Served: {len(wait_times)}")

# Run the simulation
bank_queue_simulation()
