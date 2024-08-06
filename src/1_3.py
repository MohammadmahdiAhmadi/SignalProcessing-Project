import numpy as np
import matplotlib.pyplot as plt

# Define the range for n
n = np.arange(-3, 7)  # 6 >= n >= -3

# Define the discrete-time ramp signal
ramp_signal = n

# Plot the discrete-time ramp signal
plt.stem(n, ramp_signal, linefmt='b-', markerfmt='bo', basefmt='b')
plt.title('Discrete-Time Ramp Signal')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
