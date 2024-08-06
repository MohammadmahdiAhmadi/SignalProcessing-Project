import numpy as np
import matplotlib.pyplot as plt
from pi.signal import convolve

def square_pulse(n, width):
    return np.where((n >= 0) & (n < width), 1, 0)

# Create the time axis 'n'
n = np.arange(-10, 11)

# Define the square pulse functions x[n] and h[n]
x_n = square_pulse(n, 5)  # Square pulse of width 5
h_n = square_pulse(n, 3)  # Square pulse of width 3

# Convolve x[n] and h[n] to obtain y[n]
y_n = convolve(x_n, h_n, mode='full')

# Plot x[n]
plt.subplot(3, 1, 1)
plt.stem(n, x_n, linefmt='b-', markerfmt='bo', basefmt='b')
plt.title('x[n] - Square Pulse')

# Plot h[n]
plt.subplot(3, 1, 2)
plt.stem(n, h_n, linefmt='g-', markerfmt='go', basefmt='g')
plt.title('h[n] - Square Pulse')

# Plot y[n] resulting from convolution
plt.subplot(3, 1, 3)
convolution_n = np.arange(min(n) * 2, max(n) * 2 + 1)  # Convolution result axis
plt.stem(convolution_n, y_n, linefmt='r-', markerfmt='ro', basefmt='r')
plt.title('y[n] - Convolution Result')

plt.tight_layout()
plt.show()
