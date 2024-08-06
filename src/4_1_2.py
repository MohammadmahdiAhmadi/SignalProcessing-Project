import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Parameters
omega_0 = 2 * np.pi * 1.0  # Choose an appropriate value for omega_0
duration = 1.0  # Duration of the signal
sampling_rate = 1000  # Sampling rate
SNR_dB = 10  # Signal-to-Noise Ratio in decibels
cutoff_frequency = 10  # Cutoff frequency of the low-pass filter

# Time values
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Signal x(t)
x_t = np.cos(omega_0 * t)

# Discretize the signal to obtain x[n] with AWGN
x_n_with_noise = np.cos(omega_0 * t) + np.random.normal(0, 10**(-SNR_dB / 20), len(t))

# Design a Butterworth low-pass filter
b, a = signal.butter(4, cutoff_frequency / (0.5 * sampling_rate), btype='low', analog=False)

# Apply the filter to x[n] with noise to obtain x_hadd[n]
x_hadd_n = signal.filtfilt(b, a, x_n_with_noise)

# Plotting
plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.plot(t, x_t)
plt.title('Original Signal x(t)')
plt.xlabel('t')
plt.ylabel('x(t)')

plt.subplot(3, 1, 2)
plt.stem(t, x_n_with_noise, linefmt='b-', markerfmt='bo', basefmt='b')
plt.title('Signal with AWGN x[n]')
plt.xlabel('n')
plt.ylabel('x[n]')

plt.subplot(3, 1, 3)
plt.stem(t, x_hadd_n, linefmt='g-', markerfmt='go', basefmt='g')
plt.title('Filtered Signal x_hadd[n]')
plt.xlabel('n')
plt.ylabel('x_hadd[n]')

plt.tight_layout()
plt.show()
