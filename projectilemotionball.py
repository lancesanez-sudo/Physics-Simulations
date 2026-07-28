
"""
Simulation: 2D Projectile Motion of a Thrown Bouncy Ball
This 2D physics simulation calculates the horizontal and vertical displacements and velocities of a thrown bouncy ball with gravity and drag.
"""

import numpy as np
import matplotlib.pyplot as plt

x, y = 0, 0
vx, vy, = 10, 10
m = 1
g = 9.81
d = 0.05
dt = 0.01
t = np.arange(0, 10, dt)

positions_x = []
positions_y = []
velocity_x = []
velocity_y = []

for time in t:
  Fx_drag = -d * vx
  Fy_drag = -d * vy - m * g
  ax = Fx_drag / m
  ay = Fy_drag / m
  vx = vx + ax * dt
  vy = vy + ay * dt
  x = x + vx * dt
  y = y + vy * dt

  if y < 0:
    y = 0
    vy = -vy * 0.9

  positions_x.append(x)
  positions_y.append(y)
  velocity_x.append(vx)
  velocity_y.append(vy)

plt.plot(t, positions_x)
plt.xlabel("Time (s)")
plt.ylabel("Horizontal Position (m)")
plt.title("Projectile Motion Horizontal Position")
plt.xticks(np.arange(0, 11, 1))
plt.yticks(np.arange(0, 85, 5))
plt.grid(which = 'both', color = 'gray', linestyle = '-', linewidth = 0.5)
plt.show()

plt.plot(t, positions_y)
plt.xlabel("Time (s)")
plt.ylabel("Vertical Position (m)")
plt.title("Projectile Motion Vertical Position")
plt.xticks(np.arange(0, 11, 1))
plt.grid(which = 'both', color = 'gray', linestyle = '-', linewidth = 0.5)
plt.show()

plt.plot(positions_x, positions_y)
plt.xlabel("X position (m)")
plt.ylabel("Y position (m)")
plt.title("2D Projectile Motion with Drag and Bounce")
plt.grid(which = 'both', color = 'gray', linestyle = '-', linewidth = 0.5)
plt.show()

plt.plot(t, velocity_x)
plt.xlabel("Time (s)")
plt.ylabel("Horizontal Velocity (m/s)")
plt.title("Projectile Motion Horizontal Velocity")
plt.xticks(np.arange(0, 11, 1))
plt.grid(which = 'both', color = 'gray', linestyle = '-', linewidth = 0.5)
plt.show()

plt.plot(t, velocity_y)
plt.xlabel("Time (s)")
plt.ylabel("Vertical Velocity (m/s)")
plt.title("Projectile Motion Vertical Velocity")
plt.xticks(np.arange(0, 11, 1))
plt.grid(which = 'both', color = 'gray', linestyle = '-', linewidth = 0.5)
plt.show()
