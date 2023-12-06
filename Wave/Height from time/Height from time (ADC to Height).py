import numpy as np
from scipy.optimize import fsolve

# Coefficients of the polynomial
coefficients = [-2.995e-11, 1.151e-08, -1.716e-06, 0.000122, -0.003884, 0.02037, 3]

# Define the polynomial function
def polynomial_function(x):
    return np.polyval(coefficients, x)
initial_guess = 0
# Load y values from a text file
with open('/home/rejepdurdyyev/Desktop/Wave/ADC values/120 mm.txt', 'r') as file:
    y_values_from_file = [float(line.strip()) for line in file]

# Use fsolve to find the corresponding x values
x_values_from_file = [fsolve(lambda x: polynomial_function(x) - y, 20.0)[0] for y in y_values_from_file]

# Save the new x values to a text file
with open('/home/rejepdurdyyev/Desktop/Wave/ADC values/120mm converted_x_values.txt', 'w') as file:
    for x_value in x_values_from_file:
        file.write(f'{x_value}\n')
