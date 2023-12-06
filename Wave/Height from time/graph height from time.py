import matplotlib.pyplot as plt
import numpy as np

# Load values from the text file

with open('/home/rejepdurdyyev/Desktop/Height from time/120mm.txt', 'r') as file:
    values = [float(line.strip()) for line in file]

# Calculate the number of values and time step
n = len(values)
time_step = 15 / n

# Generate time values
time_values = np.arange(0, 15, time_step)

# Plot the graph
plt.plot(time_values, values)
plt.xlabel('Time (seconds)')
plt.ylabel('Values')
plt.title('Graph of Values over Time')
plt.grid(True)
plt.show()


