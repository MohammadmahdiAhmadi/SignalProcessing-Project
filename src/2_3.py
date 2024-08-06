import numpy as np
import matplotlib.pyplot as plt

def x(t):
    return np.where((t >= 1) & (t <= 3), np.exp(-t), 0)

def h(t):
    return np.piecewise(t, [t < 1, (1 <= t) & (t <= 3), (3 < t) & (t <= 5), t > 5], [0, lambda t: t, 1, 0])

def convolution_result(t, x, h):
    return np.convolve(x, h, mode='full') * (t[1] - t[0])  # Convolution and scaling

# Time values
t = np.linspace(0, 6, 1000)

# Input signals
x_t = x(t)
h_t = h(t)

# Calculate the convolution result
y_t = convolution_result(t, x_t, h_t)

# Plotting
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(t, x_t)
plt.title('Input Signal x(t)')
plt.xlabel('t')
plt.ylabel('x(t)')

plt.subplot(3, 1, 2)
plt.plot(t, h_t)
plt.title('Impulse Response h(t)')
plt.xlabel('t')
plt.ylabel('h(t)')

plt.subplot(3, 1, 3)
convolution_t = np.linspace(2, 8, len(y_t))
plt.plot(convolution_t, y_t)
plt.title('System Response y(t)')
plt.xlabel('t')
plt.ylabel('y(t)')

plt.tight_layout()
plt.show()
