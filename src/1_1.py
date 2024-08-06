import numpy as np
import matplotlib.pyplot as plt

# Define the unit step function
def u(t):
    return np.heaviside(t, 1)

# Define the signal x(t)
def x(t):
    return u(t + 1) + u(t - 2) + u(t - 4)

# Generate time values from -5 to 5 (or any desired range)
t = np.linspace(-8, 8, 1000)

# Evaluate the signal at each time point
y = x(t)

# Plot the signal
plt.plot(t, y, label='x(t) = u(t+1) + u(t-2) + u(t-4)')
plt.title('Continuous-Time Signal')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.legend()
plt.grid(True)
plt.show()
