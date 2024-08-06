import numpy as np
import matplotlib.pyplot as plt

def square_wave(t, T, N):
    square_wave_sum = 0
    for n in range(1, N+1, 2):  # Summing odd harmonics only for a square wave
        square_wave_sum += (1/n) * np.sin(2 * np.pi * n * t / T)
    return (4 / np.pi) * square_wave_sum

# Parameters
T = 2 * np.pi  # Period of the square wave
N = 19  # Number of terms in the Fourier series
duration = 4 * T  # Duration of the signal for plotting

# Time values
t = np.linspace(0, duration, 1000)

# Generate square wave
square_wave_signal = np.sign(np.sin(t / T * np.pi))

# Generate Fourier series approximation
fourier_series_signal = square_wave(t, T, N)

# Plot the square wave and its Fourier series approximation
plt.plot(t, square_wave_signal, label='Square Wave', linewidth=2)
plt.plot(t, fourier_series_signal, label=f'Fourier Series (N={N})', linestyle='dashed', linewidth=2)

plt.title('Square Wave and Fourier Series Approximation')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()
