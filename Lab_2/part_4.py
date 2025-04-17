from collections import deque
import time

queue = deque(["Passenger 1", "Passenger 2", "Passenger 3", "Passenger 4", "Passenger 5"])

while queue:
    passenger = queue.popleft()
    print(f"{passenger} is being served...")
    time.sleep(1)  # Simulating 3 minutes as 1 second
    print(f"{passenger} finished check-in.\n")

print("\n\n\n")