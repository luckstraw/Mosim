# Laboratory Activity # 1: Exploring Basic Concepts in Modeling and Simulation

Introduction to Modeling and Simulation

## Part A - Conceptual Understanding
- **Modeling**: Creating a simplified system representation for analysis. Example: Weather forecasting predicts storms.

- **Simulation**: Using models to replicate real-world scenarios and test outcomes. Example: Flight simulators train pilots.

- **Deterministic Model**: A system with predictable outcomes, no randomness. Example: Projectile motion calculations.

- **Stochastic Model**: A system with randomness, leading to variable outcomes. Example: Stock market predictions.

- **Discrete Simulation**: Models systems where changes occur at specific intervals.

- **Continuous Simulation**: Models systems that evolve continuously over time. 

## Part B - Mini Simulation Task

*Queue System Simulation Results*

### **Customer Data**
| Customer | Arrival Time | Start of Service | End of Service | Waiting Time |
|----------|-------------|------------------|---------------|--------------|
| 1        | 3.98        | 3.98             | 6.98          | 0.00         |
| 2        | 10.26       | 10.26            | 13.26         | 0.00         |
| 3        | 14.88       | 14.88            | 17.88         | 0.00         |
| 4        | 18.81       | 18.81            | 21.81         | 0.00         |
| 5        | 21.57       | 21.81            | 24.81         | 0.24         |
| 6        | 26.76       | 26.76            | 29.76         | 0.00         |
| 7        | 29.63       | 29.76            | 32.76         | 0.12         |
| 8        | 40.75       | 40.75            | 43.75         | 0.00         |
| 9        | 57.33       | 57.33            | 60.33         | 0.00         |
| 10       | 59.74       | 60.33            | 63.33         | 0.58         |
| 11       | 67.59       | 67.59            | 70.59         | 0.00         |
| 12       | 71.35       | 71.35            | 74.35         | 0.00         |
| 13       | 75.55       | 75.55            | 78.55         | 0.00         |
| 14       | 88.54       | 88.54            | 91.54         | 0.00         |
| 15       | 88.91       | 91.54            | 94.54         | 2.63         |
| 16       | 89.37       | 94.54            | 97.54         | 5.18         |
| 17       | 89.47       | 97.54            | 100.54        | 8.07         |
| 18       | 98.41       | 100.54           | 103.54        | 2.14         |
| 19       | 105.93      | 105.93           | 108.93        | 0.00         |
| 20       | 116.14      | 116.14           | 119.14        | 0.00         |

### **Statistics**
- **Average Waiting Time:** `0.95 minutes`
- **Maximum Waiting Time:** `8.07 minutes`
- **Total Server Idle Time:** `59.14 minutes`

## Part C - Reflection Questions

### 1️⃣ How does changing the average arrival time affect the average waiting time?
- **Shorter arrival times → More congestion → Higher waiting times**  
- **Longer arrival times → Less congestion → Lower waiting times**  

### 2️⃣ What happens if the service time becomes random (e.g., drawn from a normal distribution)?
- **Fluctuating service time** can lead to:
  - Longer waiting times if service is slow.
  - Potential idle time if service is fast.

### 3️⃣ How would you classify your simulation?
- **Stochastic** → Uses randomness in customer arrival times.  
- **Discrete** → Events (arrivals & service) occur at specific intervals.  

