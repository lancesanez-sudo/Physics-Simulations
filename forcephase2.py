"""
Simulation: Phases Of Forces 2
This simulation is an advanced version of the first Phases Of Force sim, now with friction and a longer integration duration
"""

import numpy as np
import matplotlib.pyplot as plt

v = 0
x = 0
m = 2
Force1 = 10
Force2 = 8
Force3 = 4
Friction = 1
u = 0.1
F_f = Friction * u
dt = 0.01
t = np.arange(0, 10, dt)

ForceChange1 = False
ForceChange2 = False

velocity = []
distance = []

for time in t:

  if time >= 3 and not ForceChange1:
    Force1 = Force2
    ForceChange1 = True
  if time >= 7 and not ForceChange2:
    Force1 = Force3
    ForceChange2 = True

  a = (Force1 - F_f) / m
  v = v + a * dt
  x = x + v * dt

  velocity.append(v)
  distance.append(x)

print("Velocity: ", velocity)
print("Distance: ", distance)

plt.plot(t, velocity)
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Changing Forces Simulator: Velocity")
plt.show()

plt.plot(t, distance)
plt.xlabel("Time (s)")
plt.ylabel("Distance (m)")
plt.title("Changing Forces Simulator: Distance")
plt.show()
