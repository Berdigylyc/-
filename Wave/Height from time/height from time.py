import matplotlib.pyplot as plt
import numpy as np

# Define the range for y values
a = 0
b = 120

# Load x values from a text file
with open('/home/rejepdurdyyev/Downloads/voltages/voltages_ADC_for_120mm_kalib.txt', 'r') as file:
    x_values = [float(line.strip()) for line in file]

x_values = [3.003515625 - x for x in x_values][::-1]
# Calculate the number of divisions for y values
n = len(x_values)
y_division = (b - a) / (n)
# Generate y values from a to b with the specified division
y_values = np.arange(a, b , y_division)


with open('80mmtime.txt', 'w') as output_file:
    for y in y_values:
        output_file.write(f"{y}\n")
