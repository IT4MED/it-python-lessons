import matplotlib.pyplot as plt
import numpy as np
from ipywidgets import interact

# Generate heart rate data
time = np.linspace(0, 10, 100)
heart_rate = 60 + 40 * np.sin(2 * np.pi * time / 2.5)

# Create the interactive plot
def update_plot(rate):
    plt.figure(figsize=(10, 6))
    plt.plot(time, heart_rate, label='Heart Rate', color='b')
    plt.axhline(y=rate, color='r', linestyle='--', label='Selected Rate')
    plt.xlabel('Time (s)')
    plt.ylabel('Heart Rate (bpm)')
    plt.title('Heart Rate Variation Over Time')
    plt.legend()
    plt.grid(True)
    plt.show()

# Create the slider widget
interact(update_plot, rate=(40, 100, 1))
