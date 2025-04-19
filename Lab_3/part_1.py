import matplotlib.pyplot as plt
import numpy as np

# Simulate 60 seconds, 1-second intervals
time = np.arange(0, 60, 1)

# Simulate incoming traffic flow (sine wave fluctuating)
traffic_flow = np.sin(0.1 * time) + 1  # Range is roughly from 0 to 2

# Traffic signal: 1 (green) for 20s, 0 (red) for 20s, alternating
signal = [(1 if (t // 20) % 2 == 0 else 0) for t in time]

# Outgoing traffic: Only passes if signal is green
output_flow = [flow * sig for flow, sig in zip(traffic_flow, signal)]

# Plotting
plt.plot(time, traffic_flow, label='Incoming Traffic', linewidth=2)
plt.plot(time, signal, label='Traffic Signal (1=Green, 0=Red)', linestyle='--')
plt.plot(time, output_flow, label='Outgoing Traffic', linewidth=2)
plt.xlabel('Time (s)')
plt.ylabel('Flow Level')
plt.title('Traffic Flow Simulation')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
