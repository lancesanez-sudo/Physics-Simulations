
import numpy as np
import matplotlib.pyplot as plt

y = 0
v = 0
F_throw = 50
m = 0.25
d = 0.25
g = 9.81
dt = 0.01
t = np.arange(0, 5, dt)

velocity = []
height = []
kinetic_energy = []
gravitational_potential_energy = []
work = []
power = []

for time in t:
  F_g = -g * m
  F_d = -d * v
  a = (F_throw + F_g + F_d) / m
  v = v + a * dt
  y = y + v * dt
  K = 1/2 * m * v ** 2
  P = m * g * y
  W = (F_throw + F_g + F_d) * v * dt
  Power = (F_throw + F_g + F_d) * v

  if y <= 0:
    y = 0
    v = -v * 0.8
  if time >= 0.01:
    F_throw = 0

  velocity.append(v)
  height.append(y)
  kinetic_energy.append(K)
  gravitational_potential_energy.append(P)
  work.append(W)
  power.append(Power)

plt.plot(t, velocity)
plt.xlabel("Time (s)")
plt.ylabel("Velocty (m/s)")
plt.title("Thrown Bouncy Ball Physics Sim: Velocity")
plt.show()

plt.plot(t, height)
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.title("Thrown Bouncy Ball Physics Sim: Height")
plt.show()

plt.plot(t, kinetic_energy)
plt.xlabel("Time (s)")
plt.ylabel("Kinetic Energy (J)")
plt.title("Thrown Bouncy Ball Physics Sim: KE")
plt.show()

plt.plot(t, gravitational_potential_energy)
plt.xlabel("Time (s)")
plt.ylabel("Gravitational Potential Energy (J)")
plt.title("Thrown Bouncy Ball Physics Sim: PE")
plt.show()

plt.plot(t, work)
plt.xlabel("Time (s)")
plt.ylabel("Work (J)")
plt.title("Thrown Bouncy Ball Physics Sim: Work")
plt.show()

plt.plot(t, power)
plt.xlabel("Time (s)")
plt.ylabel("Power (Watts)")
plt.title("Thrown Bouncy Ball Physics Sim: Power")
plt.show()
