import numpy as np

# Given x and y values
x_values = np.array([0, 20, 40, 60, 80, 100, 120])
y_values = np.array([3, 2.59, 2.07, 1.9, 1.80, 1.72, 1.43])

# Fit a polynomial of degree 5 (you can change the degree as needed)
degree = 6
coefficients = np.polyfit(x_values, y_values, degree)

# Define the polynomial function
poly_function = np.poly1d(coefficients)
# Display the polynomial function
print("Polynomial Function:")
print(poly_function)

# Load y values from a text file
with open('/path/to/your/y_values.txt', 'r') as file:
    y_values_from_file = [float(line.strip()) for line in file]

# Use numpy.roots to find the roots (x values) for the given y values
x_values_from_file = np.roots(np.append(coefficients - y_values_from_file, 0))

# Save the new x values to a text file
with open('/path/to/your/converted_x_values.txt', 'w') as file:
    for x_value in x_values_from_file:
        file.write(f'{x_value}\n')
