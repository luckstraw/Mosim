import time

def simulate_event(event_name, delay):
    print(f"{event_name} at {time.strftime('%I:%M:%S %p')}")
    time.sleep(delay)

simulate_event("Customer Arrival", 1)
simulate_event("Order Taken", 2)
simulate_event("Food Preparation Complete", 5)
simulate_event("Customer Departure", 1)


print("\n\n\n")