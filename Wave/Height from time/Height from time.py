import matplotlib.pyplot as plt
import numpy as np

# Load y values from a text file
with open('/home/rejepdurdyyev/120mmtime.txt', 'r') as file:
    y_values = [float(line.strip()) for line in file]

# Calculate the number of divisions for x (time) values
n = len(y_values)
time_division = 15 / 367

# Generate x values (time) based on the y values
x_values = np.arange(0, n * time_division, time_division)

# Plot the line graph with y against x (time)
plt.plot(x_values, y_values, marker='o')
plt.xlabel('Time (s)')
plt.ylabel('Height (mm)')
plt.title('Dependence height and time')
plt.grid(True)
plt.show()