from scipy.io import wavfile
from sklearn.metrics import mean_squared_error

# Load the original and recovered signals
fs, original_signal = wavfile.read('Original.wav')
recovered_signal = wavfile.read('Recovered.wav')[1]

# Ensure both signals have the same length
min_length = min(len(original_signal), len(recovered_signal))
original_signal = original_signal[:min_length]
recovered_signal = recovered_signal[:min_length]

# Calculate Mean Squared Error (MSE)
mse = mean_squared_error(original_signal, recovered_signal)

# Print the MSE value
print(f'Mean Squared Error (MSE) between original and recovered signals: {mse}')
