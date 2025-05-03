import matplotlib.pyplot as plt
from virus_model import VirusModel

# Initialize the model
model = VirusModel(population=100, initial_infected=5, infection_radius=1.5,
                   infection_chance=0.4, recovery_time=20)

# Run the simulation
while model.running:
    model.step()

# Collect and plot data
data = model.datacollector.get_model_vars_dataframe()

plt.figure(figsize=(8, 5))  # Set a better figure size
plt.plot(data["Time"], data["Infected"], label="Infected", marker="o", linestyle="-")
plt.plot(data["Time"], data["Protected"], label="Protected", marker="s", linestyle="--")

plt.xlabel("Time")
plt.ylabel("Count")
plt.title("Computer Virus Spread Over Time")
plt.legend()
plt.grid(True)
plt.show()
