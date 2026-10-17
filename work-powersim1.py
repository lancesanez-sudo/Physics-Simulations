
"""
Simulation: 1-Dimension Power & Work Simulator
Simulates the motion of an object with an initial force, calculating its work and power over time.
"""

import numpy as np
import matplotlib.pyplot as plt

m = 1
F_push = 5
mu_k = 0.1
g = 9.81
d = 0
v = 0
F_N = m * g
F_fric = F_N * mu_k
w = 0
p = 0
F_current = F_push - F_fric
dt = 0.01
t = np.arange(0, 10, dt)

work = []
power = []
position = []
velocity = []

for time in t:
    a = F_current / m
    v += a * dt
    d += v * dt
    w = 0.5 * m * (v ** 2)
    p = F_current * v
    work.append(w)
    power.append(p)
    position.append(d)
    velocity.append(v)

plt.plot(t, work)
plt.xlabel("Time (s)")
plt.ylabel("Work (J)")
plt.title("Work over time")
plt.show()

plt.plot(t, power)
plt.xlabel("Time (s)")
plt.ylabel("Power (Watts)")
plt.title("Power over time")
plt.show()

plt.plot(t, position)
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.title("Position over time")
plt.show()

plt.plot(t, velocity)
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Velocity over time")
plt.show()
