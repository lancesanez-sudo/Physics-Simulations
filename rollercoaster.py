
import numpy as np
import matplotlib.pyplot as plt

y = 100
m = 25
g = -9.81
d = -0.5
v = 0
w = m * g
u = 0.1
dt = 0.01
t = np.arange(0, 10, dt)

velocity = []
height = []

for time in t:

  w = m * g

  if y <= 0:
    n = -w
    F_f = n * u
    v = -v * 0.9
    y = 0
  else:
    F_f = 0

  F_d = d * v
  F_net = w + F_f + F_d
  a = F_net / m
  v = v + a * dt
  y = y + v * dt

  velocity.append(v)
  height.append(y)

plt.plot(t, velocity)
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Falling Roller Coaster With Incline")
plt.show()

plt.plot(t, height)
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.title("Falling Roller Coaster With Incline")
plt.show()
