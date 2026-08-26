
"""
Simulation: Inclined Plane Physics Simulation
This physics simulation calculates the ramp coordinates of an object on an incline that is initially at rest.
"""

import numpy as np
import math
import matplotlib.pyplot as plt

m = 1
d = 100 # Displacement
v = 0
g = 9.81
u_k = 0.1
angle = math.radians(45)
dt = 0.01
t = np.arange(0, 10, dt)

position = []
velocity = []

for time in t:
  F_g = m * g * math.sin(angle)
  F_N = m * g * math.cos(angle)
  F_k = F_N * u_k
  F_net = F_g - F_k
  a = F_net / m
  v = v + a * dt
  d = d + v * dt
  velocity.append(v)
  position.append(d)

plt.plot(t, position)
plt.xlabel("Time (s)")
plt.ylabel("Displacement")
plt.title("Inclined Plane With Ramp Coords Sim")
plt.show()

plt.plot(t, velocity)
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Inclined Plane With Ramp Coords Sim")
plt.show()

# Ramp coordinates vs World coordinates:
#
# Ramp coordinates:
#   - Axes are rotated to align with the ramp (parallel and perpendicular).
#   - Forces split neatly:
#       Parallel = mg * sin(angle) drives motion down the ramp
#       Perpendicular = mg * cos(angle) balanced by the normal force
#   - Only one axis (parallel) has acceleration.
#   - Coding logic: compute displacement along ramp, then break into x and y components.
#
# World coordinates:
#   - Axes are the usual horizontal (x) and vertical (y).
#   - Forces must be resolved into x and y components.
#       F_gy = -mg, F_gx = 0
#       F_Nx = +mg * cos(angle) * sin(theta) F_Ny = +mg * cos^2(angle)) for ramp sloping down-right
#   - Signs depend on ramp orientation: left = negative x, up = positive y.
#   - Coding logic: compute F_net_x and F_net_y directly, then integrate to get a_x, a_y,
#     and update v_x, v_y, x, y step by step.
#
# Summary:
#   - Ramp coords simplify the physics (1D motion).
#   - World coords match the familiar F_net to a to v to x structure but require careful trig
#     and sign conventions.
