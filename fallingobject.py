
import numpy as np

v = 0
y = 50
g = -9.81
a = g
dt = 0.01
t = np.arange(0, 10, dt)

velocity = []
height = []

for time in t:
  a = g
  v = v + a * dt
  y = y + v * dt
  if y <= 0:
    y = 0
    velocity.append(v)
    height.append(y)
    break
  velocity.append(v)
  height.append(y)

print("Velocities: ", velocity)
print("Heights: ", height)
