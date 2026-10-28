import matplotlib.pyplot as plt
import numpy as np


def plot_signals(x, h, y, sr):
    """
    Plot the audio signals: input, impulse response and output.

    Arguments:
    x  : array -> input signal
    h  : array -> impulse response
    y  : array -> output signal
    sr : int   -> sampling rate
    """
    # Build the time axes (in seconds)
    t_x = np.arange(len(x)) / sr
    t_h = np.arange(len(h)) / sr
    t_y = np.arange(len(y)) / sr

    # Create the figure
    plt.figure(figsize=(12, 6))

    # Input signal
    plt.subplot(3, 1, 1)
    plt.plot(t_x, x)
    plt.title("Input signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")

    # Impulse response
    plt.subplot(3, 1, 2)
    plt.plot(t_h, h)
    plt.title("Impulse response")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")

    # Output signal
    plt.subplot(3, 1, 3)
    plt.plot(t_y, y)
    plt.title("Output signal after reverb")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")

    # Display the plots
    plt.tight_layout()
    plt.show()