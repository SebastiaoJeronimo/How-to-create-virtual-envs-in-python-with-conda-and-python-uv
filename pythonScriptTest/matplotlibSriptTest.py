"""
matplotlib_test.py
A simple script to verify matplotlib plotting works.
"""

import numpy as np
import matplotlib.pyplot as plt

# Generate data
x = np.linspace(0, 2 * np.pi, 200)
y_sin = np.sin(x)
y_cos = np.cos(x)

# Line plot
plt.figure(figsize=(8, 5))
plt.plot(x, y_sin, label='sin(x)')
plt.plot(x, y_cos, label='cos(x)')
plt.title('Sine and Cosine Functions')
plt.xlabel('x values')
plt.ylabel('y values')
plt.legend()
plt.grid(True)
plt.show()

# Scatter plot
np.random.seed(42)
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
sizes = 1000 * np.random.rand(50)

plt.figure(figsize=(6, 6))
plt.scatter(x, y, c=colors, s=sizes, alpha=0.6, cmap='viridis')
plt.title('Random Scatter Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.colorbar(label='Color Scale')
plt.show()
