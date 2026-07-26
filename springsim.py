
import numpy as np
import matplotlib.pyplot as plt

y = 0
k = 5000
x = 0.5
m = 1
d = -0.05
g = -9.8
U = 0.5 * k * (x ** 2)
v = (((2 * U) / m) ** 0.5)
dt = 0.01
t = np.arange(0, 10, dt)

height = []
velocity = []

for time in t:
  F_d = d * v
  F_g = m * g
  F_net = F_d + F_g
  a = F_net / m
  v = v + a * dt
  y = y + v * dt
  velocity.append(v)
  height.append(y)

plt.plot(t, velocity)
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Spring Simulator With Gravity And Drag")
plt.xticks(np.arange(0, 11, 1))
plt.yticks(np.arange(-60, 50, 5))
plt.grid(which = 'both', color = 'gray', linestyle = '-', linewidth = 0.5)
plt.show()

plt.plot(t, height)
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.title("Spring Simulator With Gravity And Drag")
plt.xticks(np.arange(0, 11, 1))
plt.yticks(np.arange(-150, 100, 10))
plt.grid(which = 'both', color = 'gray', linestyle = '-', linewidth = 0.5)
plt.show()
