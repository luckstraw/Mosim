import random

class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.total_time = 0

    def process_stage(self, stage_name, min_time, max_time):
        stage_time = random.randint(min_time, max_time)
        print(f"Order {self.order_id}: {stage_name} took {stage_time} minutes.")
        self.total_time += stage_time

def simulate_order_processing(num_orders):
    orders = []
    for i in range(1, num_orders + 1):
        order = Order(i)
        order.process_stage("Order Received", 1, 2)
        order.process_stage("Payment Verification", 2, 4)
        order.process_stage("Packaging", 3, 5)
        order.process_stage("Shipping", 4, 6)
        print(f"Order {i} completed in {order.total_time} minutes.\n")
        orders.append(order.total_time)
        
    avg_time = sum(orders) / len(orders)
    print(f"Average processing time: {round(avg_time, 2)} minutes.")

simulate_order_processing(num_orders=5)