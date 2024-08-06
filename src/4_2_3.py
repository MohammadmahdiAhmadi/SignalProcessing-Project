import numpy as np
import scipy.signal as signal
import scipy.io.wavfile as wav

# Load the original and distorted signals
fs = 22050  # Sampling frequency
original_fs, original_signal = wav.read('Original.wav')
distorted_fs, distorted_signal = wav.read('Distorted.wav')

# Ensure both signals have the same length
min_len = min(len(original_signal), len(distorted_signal))
original_signal = original_signal[:min_len]
distorted_signal = distorted_signal[:min_len]

# Design a simple filter (you may need to adjust filter parameters based on your specific case)
cutoff_frequency = 4000  # Adjust this based on your requirements
b, a = signal.butter(4, cutoff_frequency / (fs / 2), 'low')

# Apply the filter to the distorted signal
recovered_signal = signal.filtfilt(b, a, distorted_signal)

# Save the recovered signal
wav.write('Recovered.wav', fs, recovered_signal.astype(np.int16))
