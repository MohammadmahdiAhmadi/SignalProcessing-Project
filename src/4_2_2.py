import numpy as np
from scipy.io import wavfile
from sklearn.metrics import mean_squared_error

# Load the original and distorted signals
fs, original_signal = wavfile.read('Original.wav')
distorted_signal = wavfile.read('Distorted.wav')[1]

# Ensure both signals have the same length
min_length = min(len(original_signal), len(distorted_signal))
original_signal = original_signal[:min_length]
distorted_signal = distorted_signal[:min_length]

# Calculate Mean Squared Error (MSE)
mse = mean_squared_error(original_signal, distorted_signal)

# Print the MSE value
print(f'Mean Squared Error (MSE) between original and distorted signals: {mse}')
