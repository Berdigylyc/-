import matplotlib.pyplot as plt
import numpy as np

# Given x and y values
x_values = [0, 20, 40, 60, 80, 100]
y_values = [0, 460*460, 720*720, 833*833, 920*920, 1029*1029]

# Calculate the square root of each x value to get y values
y_values = y_values

# Plot the data points
plt.scatter(x_values, y_values,)
plt.plot(x_values, y_values, )

slope, intercept = np.polyfit(x_values, y_values, 1)

# Print the slope
print(f"Slope of the line: {1/slope}")

plt.xlabel('Height (mm)')
plt.ylabel('Square of velocity ((m/s)^2)')
plt.title('Dependence velocity of wave and height, g = 9.5 m/s^2')
plt.legend()
plt.grid(True)
plt.show()
