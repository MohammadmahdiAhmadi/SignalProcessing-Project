import numpy as np
import matplotlib.pyplot as plt

def square_pulse(t, L):
    return np.where((t >= 0) & (t < L), 1, 0)

# Define the convolution function
def convolution_result(t, L1, L2):
    return np.convolve(square_pulse(t, L1), square_pulse(t, L2), mode='same')

# Time values
t = np.linspace(-4, 6, 1000)

# Widths of the square pulses
L1 = 2
L2 = 3

# Calculate the convolution result
result = convolution_result(t, L1, L2)

# Plot the convolution result
plt.plot(t, result)
plt.title('Convolution Result')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.grid(True)
plt.show()
