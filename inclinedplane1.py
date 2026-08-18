
"""
Simulation: Inclined Plane Physics Simulation
This physics simulation calculates the world coordinates of an object on an incline that is initially at rest.
"""

import numpy as np
import math
import matplotlib.pyplot as plt

m = 1
g = 9.81
angle = math.radians(30)   # ramp angle (down to the right)
dt = 0.01
t = np.arange(0, 5, dt)
x, y = 0, 5
v_x, v_y = 0, 0

positions_x, positions_y = [], []

for time in t:
    # Forces in world coordinates
    F_gx = 0
    F_gy = -m * g
    # Normal force (perpendicular to ramp, pointing up-right)
    F_Nx = m * g * math.cos(angle) * math.sin(angle)   # negative because left
    F_Ny =  m * g * (math.cos(angle)**2)              # positive because up
    F_net_x = F_gx + F_Nx
    F_net_y = F_gy + F_Ny
    a_x = F_net_x/m
    a_y = F_net_y/m
    v_x = v_x + a_x * dt
    v_y = v_y + a_y * dt
    x = x + v_x * dt
    y = y + v_y * dt
    positions_x.append(x)
    positions_y.append(y)
    if y <= 0:
        break

plt.plot(positions_x, positions_y, 'b-')
plt.xlabel("Horizontal (m)")
plt.ylabel("Vertical (m)")
plt.title("Inclined Plane Simulation in World Coordinates")
plt.grid()
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
