"""
Simulation: Phases Of Forces
This simulations calculates the velocity and displacement of an object experiencing different phases of motion within different intervals of time
"""

import numpy as np

F_initial = 18
m = 4
v = 0
x = 0
dt = 0.01
t_array = np.arange(0, 10, dt)

velocity = []
displacement = []

for time in t_array:
  F_initial = F_initial
  if time >= 3 and time < 5:
    F_initial = 0
  elif time >= 5:
    F_initial = -10

  a = F_initial / m
  v = v + a * dt
  x = x + v * dt
  if time >= 7:
    break
  velocity.append(v)
  displacement.append(x)

print("Velocities: ", velocity)
print("Displacement: ", displacement)
