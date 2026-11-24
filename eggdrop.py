
"""
Simulation: Egg Drop
Simulates the motion of two falling eggs that fall on two different surfaces.
"""

import numpy as np
import matplotlib.pyplot as plt

egg1mass = 0.057 # kg
egg2mass = 0.057 # kg
egg1_x = 5 # meters
egg2_x = 10 # meters
egg1_y = 10 # meters
egg2_y = 10 # meters
egg1_velocity = 0 # m/s
egg2_velocity = 0 # m/s
egg1_crack = 50 # Newtons
egg2_crack = egg1_crack
g = -9.81 # m/s^2

# Spring constants
k1 = 50000
k2 = 500
# Damping ratios
zeta1 = 0.1
zeta2 = 0.9
# Damping coefficients
c1 = 2 * zeta1 * np.sqrt(k1 * egg1mass)
c2 = 2 * zeta2 * np.sqrt(k2 * egg2mass)

# Time settings
dt = 0.0001
t = np.arange(0, 10, dt)

# Lists for storing data
momentum_egg1 = [egg1mass * egg1_velocity]
momentum_egg2 = [egg2mass * egg2_velocity]
horizontal_displacement1 = [egg1_x]
horizontal_displacement2 = [egg2_x]
vertical_displacement1 = [egg1_y]
vertical_displacement2 = [egg2_y]

# Maximum impact forces
peak_force1 = 0
peak_force2 = 0

for time in t:
    if egg1_y <= 0:
        F_surface1 = max(0, -k1 * egg1_y - c1 * egg1_velocity)
    else:
        F_surface1 = 0

    if egg2_y <= 0:
        F_surface2 = max(0, -k2 * egg2_y - c2 * egg2_velocity)
    else:
        F_surface2 = 0

    egg1_acceleration = g + F_surface1 / egg1mass
    egg2_acceleration = g + F_surface2 / egg2mass

    egg1_velocity += egg1_acceleration * dt
    egg2_velocity += egg2_acceleration * dt

    egg1_y += egg1_velocity * dt
    egg2_y += egg2_velocity * dt

    if egg1_y <= 0:
        F_surface1 = max(0, -k1 * egg1_y - c1 * egg1_velocity)
    else:
        F_surface1 = 0

    if egg2_y <= 0:
        F_surface2 = max(0, -k2 * egg2_y - c2 * egg2_velocity)
    else:
        F_surface2 = 0

    peak_force1 = max(peak_force1, F_surface1)
    peak_force2 = max(peak_force2, F_surface2)

    egg1_p = egg1mass * egg1_velocity
    egg2_p = egg2mass * egg2_velocity

    momentum_egg1.append(egg1_p)
    momentum_egg2.append(egg2_p)
    horizontal_displacement1.append(egg1_x)
    horizontal_displacement2.append(egg2_x)
    vertical_displacement1.append(egg1_y)
    vertical_displacement2.append(egg2_y)


# Determine whether eggs break
print("Egg 1 maximum impact force:", round(peak_force1, 2), "N")
print("Egg 2 maximum impact force:", round(peak_force2, 2), "N")
if peak_force1 >= egg1_crack:
    print("The first egg has broken!")
else:
    print("The first egg has safely landed!")

if peak_force2 >= egg2_crack:
    print("The second egg has broken!")
else:
    print("The second egg has safely landed!")


# Graph 1: Egg 1 Momentum
plt.plot(t, momentum_egg1)
plt.xlabel("Time (s)")
plt.ylabel("Momentum (kg * m/s)")
plt.title("Momentum of Egg 1 Over Time")
plt.grid()
plt.show()


# Graph 2: Egg 2 Momentum
plt.plot(t, momentum_egg2)
plt.xlabel("Time (s)")
plt.ylabel("Momentum (kg * m/s)")
plt.title("Momentum of Egg 2 Over Time")
plt.grid()
plt.show()


# Graph 3: Egg 1 Trajectory
plt.plot(horizontal_displacement1, vertical_displacement1)
plt.xlabel("Horizontal Displacement (m)")
plt.ylabel("Vertical Displacement (m)")
plt.title("Trajectory of Egg 1")
plt.grid()
plt.show()


# Graph 4: Egg 2 Trajectory
plt.plot(horizontal_displacement2, vertical_displacement2)
plt.xlabel("Horizontal Displacement (m)")
plt.ylabel("Vertical Displacement (m)")
plt.title("Trajectory of Egg 2")
plt.grid()
plt.show()
