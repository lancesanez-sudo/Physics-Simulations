
"""
Simulation: 2-Dimension Power & Work Simulator
Simulates the motion of a projectile object with an initial force, calculating its work and power over time.
"""

import numpy as np
import matplotlib.pyplot as plt
import math

m = 5
g = 9.81
initial_speed = 25
theta = math.radians(45)
v_x = initial_speed * math.cos(theta)
v_y = initial_speed * math.sin(theta)
x = 0
y = 0
drag_coefficient = 0.01
dt = 0.01
t_final = 10
t = np.arange(0, t_final + dt, dt)
work = 0

work_list = [0]
power_list = []
horizontal_displacement = [x]
vertical_displacement = [y]
horizontal_velocity = [v_x]
vertical_velocity = [v_y]

speed = math.sqrt(v_x**2 + v_y**2)
F_dragx = -drag_coefficient * speed * v_x
F_dragy = -drag_coefficient * speed * v_y

power = F_dragx * v_x + (F_dragy - m * g) * v_y
power_list.append(power)

time_list = [0]

for time in t:
    v_x_old = v_x
    v_y_old = v_y
    speed = math.sqrt(v_x**2 + v_y**2)
    F_dragx = -drag_coefficient * speed * v_x
    F_dragy = -drag_coefficient * speed * v_y
    F_netx = F_dragx
    F_nety = F_dragy - (m * g)
    a_x = F_netx / m
    a_y = F_nety / m
    v_x = v_x + a_x * dt
    v_y = v_y + a_y * dt
    v_x_avg = (v_x_old + v_x) / 2
    v_y_avg = (v_y_old + v_y) / 2
    dx = v_x_avg * dt
    dy = v_y_avg * dt
    step = dt
    landed = False

    if y + dy < 0:
        fraction = y / (-dy)
        step = dt * fraction
        v_x = v_x_old + a_x * step
        v_y = v_y_old + a_y * step
        v_x_avg = (v_x_old + v_x) / 2
        v_y_avg = (v_y_old + v_y) / 2
        dx = v_x_avg * step
        dy = -y
        landed = True

    work_increment = (F_netx * dx) + (F_nety * dy)
    work = work + work_increment
    power = (F_netx * v_x_avg) + (F_nety * v_y_avg)
    x = x + dx
    y = y + dy

    work_list.append(work)
    power_list.append(power)
    horizontal_displacement.append(x)
    vertical_displacement.append(y)
    horizontal_velocity.append(v_x)
    vertical_velocity.append(v_y)
    time_list.append(time - dt + step)

    if landed:
        break

# Work over time
plt.plot(time_list, work_list)
plt.xlabel("Time (s)")
plt.ylabel("Work (J)")
plt.title("Net Work over Time")
plt.grid()
plt.show()

# Power over time
plt.plot(time_list, power_list)
plt.xlabel("Time (s)")
plt.ylabel("Power (W)")
plt.title("Net Power over Time")
plt.grid()
plt.show()

# Projectile trajectory
plt.plot(horizontal_displacement, vertical_displacement)
plt.xlabel("Horizontal Displacement (m)")
plt.ylabel("Vertical Displacement (m)")
plt.title("Object Trajectory")
plt.grid()
plt.show()

# Horizontal velocity
plt.plot(time_list, horizontal_velocity)
plt.xlabel("Time (s)")
plt.ylabel("Horizontal Velocity (m/s)")
plt.title("Horizontal Velocity over Time")
plt.grid()
plt.show()

# Vertical velocity
plt.plot(time_list, vertical_velocity)
plt.xlabel("Time (s)")
plt.ylabel("Vertical Velocity (m/s)")
plt.title("Vertical Velocity over Time")
plt.grid()
plt.show()
