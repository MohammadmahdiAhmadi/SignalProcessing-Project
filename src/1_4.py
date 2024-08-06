import numpy as np
import matplotlib.pyplot as plt

def plot_complex_sequence(w, r):
    # Generate values for n
    n = np.arange(-10, 11)  # Adjust the range based on your preference

    # Generate the complex sequence x[n]
    x_n = r**n * np.exp(1j * w * n)

    # Plot real part
    plt.subplot(2, 2, 1)
    plt.stem(n, np.real(x_n), linefmt='b-', markerfmt='bo', basefmt='b')
    plt.title('Real Part')

    # Plot imaginary part
    plt.subplot(2, 2, 2)
    plt.stem(n, np.imag(x_n), linefmt='g-', markerfmt='go', basefmt='g')
    plt.title('Imaginary Part')

    # Plot magnitude
    plt.subplot(2, 2, 3)
    plt.stem(n, np.abs(x_n), linefmt='r-', markerfmt='ro', basefmt='r')
    plt.title('Magnitude')

    # Plot phase
    plt.subplot(2, 2, 4)
    plt.stem(n, np.angle(x_n), linefmt='purple', markerfmt='o', basefmt='r')
    plt.title('Phase')

    plt.tight_layout()
    plt.show()

# Get user input for w and r
w_input = float(input("Enter the value of w (small omega): "))
r_input = float(input("Enter the value of r: "))

# Call the function to plot
plot_complex_sequence(w_input, r_input)
