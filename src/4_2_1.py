import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Load the original and distorted signals
fs, original_signal = wavfile.read('Original.wav')
distorted_signal = wavfile.read('Distorted.wav')[1]

# Time values for x-axis
time = np.arange(len(original_signal)) / fs

# Plot the original signal
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(time, original_signal, label='Original Signal')
plt.title('Original Signal')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.legend()

# Plot the distorted signal
plt.subplot(2, 1, 2)
plt.plot(time, distorted_signal, label='Distorted Signal', color='orange')
plt.title('Distorted Signal')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.legend()

# Show the plots
plt.tight_layout()
plt.show()
