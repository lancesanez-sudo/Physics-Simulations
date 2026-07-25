"""
Simulation: Acceleration Cutoff
This physics simulation calculates the velocity and displacement of an object that cuts off its acceleration at a given time
"""

import numpy as np
import matplotlib.pyplot as plt

v = 0
x = 0
a = 2
dt = 0.01
t = np.arange(0, 10, dt)

velocity = []
displacement = []

for time in t:
  if time >= 5:
    a = 0
  else:
    a = 2
  v = v + a * dt
  x = x + v * dt
  velocity.append(v)
  displacement.append(x)

print("Velocities: ", velocity)
print("Displacements: ", displacement)

plt.plot(t, velocity)
plt.xlabel("Time (s)")
plt.ylabel("Velocity m/s")
plt.title("Acceleration Cutoff Simulator (Velocity)")
plt.show()

plt.plot(t, displacement)
plt.xlabel("Time (s)")
plt.ylabel("Displacement (m)")
plt.title("Acceleration Cutoff Simulator (Displacement)")
plt.show()
