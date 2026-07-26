
import numpy as np
import matplotlib.pyplot as plt

v = 0
y = 0
g = -9.81
K = 0
P = 0
d = -10 #constant drag
f = 3000000 #Newtons #Assume constant thrust
m = 1000 #kg
dt = 0.01
t = np.arange(0, 100, dt)

stage1_dropped = False
stage2_dropped = False

mass = []
altitude = []
velocity = []
acceleration = []
kinetic_energy = []
gravitational_potential_energy = []

for time in t:

  if time >= 0.01:
    m = m - 0.02
  else:
    m = m
  if time >= 25 and not stage1_dropped:
    m = m - 25
    stage1_dropped = True
  if time >= 50 and not stage2_dropped:
    m = m - 25
    stage2_dropped = True

  F_d = d * v
  F_g = m * g
  F_net = f + F_d + F_g
  a = F_net / m
  v = v + a * dt
  K = 0.5 * m * (v ** 2)
  y = y + v * dt
  P = m * -g * y

  mass.append(m)
  altitude.append(y)
  velocity.append(v)
  acceleration.append(a)
  kinetic_energy.append(K)
  gravitational_potential_energy.append(P)

#print("Mass: ", mass)
#print("Altitude: ", altitude)
#print("Velocity: ", velocity)
#print("Acceleration: ", acceleration)

plt.plot(t, mass)
plt.xlabel("Time (s)")
plt.ylabel("Mass (kg)")
plt.title("Mass over time in a constant thrust rocket that burns fuel with 3 stages")
plt.grid(which = 'both', color = 'gray', linestyle = '-', linewidth = 0.5)
plt.xticks(np.arange(0, 105, 5))
plt.yticks(np.arange(740, 1010, 10))
plt.show()

plt.plot(t, altitude)
plt.xlabel("Time (s)")
plt.ylabel("Altitude (m)")
plt.title("Altitude over time in a constant thrust rocket that burns fuel with 3 stages")
plt.grid(which = 'both', color = 'gray', linestyle = '-', linewidth = 0.5)
plt.xticks(np.arange(0, 105, 5))

plt.show()

plt.plot(t, velocity)
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Velocity over time in a constant thrust rocket that burns fuel with 3 stages")
plt.grid(which = 'both', color = 'gray', linestyle = '-', linewidth = 0.5)
plt.xticks(np.arange(0, 105, 5))
plt.show()

plt.plot(t, acceleration)
plt.xlabel("Time (s)")
plt.ylabel("Acceleration (m/s^2)")
plt.title("Acceleration over time in a constant thrust rocket that burns fuel with 3 stages")
plt.grid(which = 'both', color = 'gray', linestyle = '-', linewidth = 0.5)
plt.xticks(np.arange(0, 105, 5))
plt.show()

plt.plot(t, kinetic_energy)
plt.xlabel("Time (s)")
plt.ylabel("Kinetic Energy (J)")
plt.title("Kinetic energy over time in a constant thrust rocket that burns fuel with 3 stages")
plt.grid(which = 'both', color = 'gray', linestyle = '-', linewidth = 0.5)
plt.xticks(np.arange(0, 105, 5))
plt.show()

plt.plot(t, gravitational_potential_energy)
plt.xlabel("Time (s)")
plt.ylabel("Gravitational Potential Energy (J)")
plt.title("Gravitational potential energy over time in a constant thrust rocket that burns fuel with 3 stages")
plt.grid(which = 'both', color = 'gray', linestyle = '-', linewidth = 0.5)
plt.xticks(np.arange(0, 105, 5))
plt.show()
