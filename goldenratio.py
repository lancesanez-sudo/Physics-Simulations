
"""
Simulation: The Golden Ratio
Graphs the golden ratio by using the growth rule to graph the spiral after each quarter turn.
"""

import matplotlib.pyplot as plt
import numpy as np

phi = (1 + np.sqrt(5))/2
a = 1 # initial radius or quarter circle

# Theta values across 4 full rotations (8*pi radians)
theta = np.linspace(0, 8 * np.pi, 2000)

# Polar equation: grows by a factor of phi every quarter-turn (pi/2)
r = a * (phi ** (2 * theta / np.pi))

# Convert polar (r, theta) to Cartesian (x, y)
x = r * np.cos(theta)
y = r * np.sin(theta)

plt.plot(x, y)
plt.gca().set_aspect("equal")  # Essential so the spiral isn't stretched
plt.title("Spiral of The Golden Ratio ($r = \\phi^{2\\theta/\\pi}$)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()
