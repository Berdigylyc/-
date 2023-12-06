import matplotlib.pyplot as plt
import numpy as np

# Given x and y values
x_values = [20, 40, 60, 80, 100]
y_values = [0.46, 0.72, 0.833, 0.92, 1.029]

# Calculate the square root of each x value to get y values
x_values = np.sqrt(x_values)

# Plot the data points
plt.scatter(x_values, y_values,)
plt.plot(x_values, y_values, )

plt.xlabel('Square root of height (mm^1/2)')
plt.ylabel('Velocity (m/s)')
plt.title('Dependence velocity of wave and height')
plt.legend()
plt.grid(True)
plt.show()