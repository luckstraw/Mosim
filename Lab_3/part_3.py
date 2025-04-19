import numpy as np
import matplotlib.pyplot as plt

sales_price = 100
unit_sales = np.random.normal(500, 50, 100000)
unit_cost = np.random.normal(60, 10, 100000)
profit = (sales_price - unit_cost) * unit_sales

avg_profit = np.mean(profit)
std_dev = np.std(profit)

# Plot
plt.hist(profit, bins=50, color='skyblue', edgecolor='black')
plt.title('Profit Distribution (Monte Carlo Simulation)')
plt.xlabel('Profit')
plt.ylabel('Frequency')
plt.grid(True)

# Annotate
plt.axvline(avg_profit, color='red', linestyle='dashed', linewidth=2, label=f'Avg Profit = ${avg_profit:,.2f}')
plt.legend()
plt.text(avg_profit, plt.ylim()[1]*0.9, f'Std Dev = ${std_dev:,.2f}', color='black')
plt.tight_layout()
plt.show()
