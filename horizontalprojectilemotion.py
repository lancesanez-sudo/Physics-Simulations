
"""
Simulation: 2D Projectile Motion of a Falling Object Launched Horizontally
This 2D physics simulation calculates the height, distance, and velocities of a falling object launched horizontally with gravity and drag.
"""

import numpy as np
import matplotlib.pyplot as plt

y = 500
x = 0
v_x = 10
v_y = 0
g = 9.81
d = 0.1
m = 5
dt = 0.01
t = np.arange(0, 10, dt)

positions_x = []
positions_y = []
velocity_x = []
velocity_y = []


for time in t:
  F_xd = v_x * -d
  F_yd = v_y * -d
  F_yg = m * -g
  F_xnet = F_xd
  F_ynet = F_yd + F_yg
  a_x = F_xnet / m
  a_y = F_ynet / m
  v_x = v_x + a_x * dt
  v_y = v_y + a_y * dt
  y = y + v_y * dt
  x = x + v_x * dt
  positions_x.append(x)
  positions_y.append(y)
  velocity_x.append(v_x)
  velocity_y.append(v_y)

plt.plot(t, positions_x)
plt.xlabel("Time (s)")
plt.ylabel("Distance (m)")
plt.grid(which = 'both', color = 'gray', linestyle = '-', linewidth = 0.5)
plt.title("Horizontally Launched Projectile Simulation")
plt.xticks(np.arange(0, 11, 1))
plt.yticks(np.arange(0, 100, 10))
plt.show()

plt.plot(t, positions_y)
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.grid(which = 'both', color = 'gray', linestyle = '-', linewidth = 0.5)
plt.title("Horizontally Launched Projectile Simulation")
plt.xticks(np.arange(0, 11, 1))
plt.yticks(np.arange(0, 550, 25))
plt.show()

plt.plot(t, velocity_x)
plt.xlabel("Time (s)")
plt.ylabel("Horizontal Velocity (m/s)")
plt.grid(which = 'both', color = 'gray', linestyle = '-', linewidth = 0.5)
plt.title("Horizontally Launched Projectile Simulation")
plt.xticks(np.arange(0, 11, 1))
plt.show()

plt.plot(t, velocity_y)
plt.xlabel("Time (s)")
plt.ylabel("Vertical Velocity (m/s)")
plt.grid(which = 'both', color = 'gray', linestyle = '-', linewidth = 0.5)
plt.title("Horizontally Launched Projectile Simulation")
plt.xticks(np.arange(0, 11, 1))
plt.show()
