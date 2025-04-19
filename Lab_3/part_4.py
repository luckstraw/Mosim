import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt

np.random.seed(42)
X = np.random.rand(100, 1) * 150
y = 30000 + 1500 * X + np.random.randn(100, 1) * 5000

model = LinearRegression()
model.fit(X, y)
predictions = model.predict(X)

mae = mean_absolute_error(y, predictions)
mse = mean_squared_error(y, predictions)

# Plot
plt.scatter(X, y, color='blue', label='Actual', alpha=0.6)
plt.plot(X, predictions, color='red', label='Predicted', linewidth=2)
plt.title('House Price Prediction')
plt.xlabel('Size (sqm)')
plt.ylabel('Price ($)')
plt.legend()
plt.grid(True)

# Annotate MAE and MSE
plt.text(X.min(), y.max(), f'MAE: ${mae:.2f}\nMSE: ${mse:.2f}', fontsize=10,
         bbox=dict(facecolor='white', edgecolor='gray', boxstyle='round,pad=0.5'))

plt.tight_layout()
plt.show()
