import numpy as np
import matplotlib.pyplot as plt

# Parameters
omega_0 = 2 * np.pi * 1.0  # Choose an appropriate value for omega_0
duration = 1.0  # Duration of the signal
sampling_rate = 1000  # Sampling rate
SNR_dB = 10  # Signal-to-Noise Ratio in decibels

# Time values
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Signal x(t)
x_t = np.cos(omega_0 * t)

# Discretize the signal to obtain x[n]
x_n = np.cos(omega_0 * t)
x_n += np.random.normal(0, 10**(-SNR_dB / 20), len(t))  # Add AWGN

# Plotting
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(t, x_t)
plt.title('Original Signal x(t)')
plt.xlabel('t')
plt.ylabel('x(t)')

plt.subplot(2, 1, 2)
plt.stem(t, x_n, linefmt='b-', markerfmt='bo', basefmt='b')
plt.title('Signal with AWGN x[n]')
plt.xlabel('n')
plt.ylabel('x[n]')

plt.tight_layout()
plt.show()
