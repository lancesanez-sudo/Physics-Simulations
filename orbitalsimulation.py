
"""
Simulation: Orbital Satellite Rocket
Simulates the motion of an orbital rocket undergoing universal gravitation, drag, two stages, fuel burn, and a gravity turn to deploy a satellite that orbits the Earth.
"""

import numpy as np
import matplotlib.pyplot as plt
import math

vx = 0 # m/s (Initial speed relative to center)
vy = 0 # m/s
Earth_radius = 6_371_000 # m
x = Earth_radius # m (Rocket starts on the equator surface)
y = 0 # m
G = 6.674e-11 # Nm^2/kg^3
m_earth = 5.97219e24  # kg
d_x = 0.001 # Drag coefficient X
d_y = 0.015 # Drag coefficient Y
angle = math.radians(0) # Starts pointing straight out into space along the X-axis
m_satellite = 700 # kg (Real-world medium satellite mass)
m_stage1_structure = 22_200 # kg
m_stage2_structure = 4_000 # kg
m_structural_dry_mass = m_stage1_structure + m_stage2_structure + m_satellite # kg
m_propellant = 522_500 # kg
m_total = m_propellant + m_structural_dry_mass # kg
m_propellant_reserve = m_propellant * 0.02 # kg
F_thrust = 7_600_000 # Newtons
dt = 0.01
t = np.arange(0, 12000, dt)

stage1_dropped = False
stage2_dropped = False

mass = []
displacement_x = []
displacement_y = []
velocity_x = []
velocity_y = []

for time in t:
  r = ((x ** 2) + (y ** 2)) ** 0.5

  current_thrust = 7_600_000

  if time >= 0.01 and m_propellant > m_propellant_reserve:
    m_propellant = m_propellant - (1005 * dt)
    if m_propellant < m_propellant_reserve:
        m_propellant = m_propellant_reserve

  m_total = m_propellant + m_structural_dry_mass

  if time >= 165 and not stage1_dropped:
    m_structural_dry_mass = m_structural_dry_mass - m_stage1_structure
    stage1_dropped = True

  if stage1_dropped:
    current_thrust = 2_900_000

  if time >= 510 and not stage2_dropped:
    m_structural_dry_mass = m_structural_dry_mass - m_stage2_structure
    stage2_dropped = True

  if stage2_dropped or m_propellant <= m_propellant_reserve:
    current_thrust = 0

  if time >= 20:
    angle = angle + 0.000034  # Gentle eastward tilt over the equator curve
    if angle > math.radians(90):
      angle = math.radians(90)

  if (r - Earth_radius) < 100_000:
    F_dx = -d_x * vx * abs(vx)
    F_dy = -d_y * vy * abs(vy)
  else:
    F_dx = 0
    F_dy = 0

  F_gx = (-G * m_earth * m_total * x) / (r ** 3)
  F_gy = (-G * m_earth * m_total * y) / (r ** 3)
  radial_degrees = math.atan2(y, x)
  world_thrust_angle = radial_degrees + angle
  F_thrustx = current_thrust * math.cos(world_thrust_angle)
  F_thrusty = current_thrust * math.sin(world_thrust_angle)
  F_net_x = F_gx + F_thrustx + F_dx
  F_net_y = F_gy + F_thrusty + F_dy
  ax = F_net_x / m_total
  ay = F_net_y / m_total
  vx = vx + (ax * dt)
  vy = vy + (ay * dt)
  x = x + (vx * dt)
  y = y + (vy * dt)

  mass.append(m_total)
  displacement_x.append(x)
  displacement_y.append(y)
  velocity_x.append(vx)
  velocity_y.append(vy)

  if r < Earth_radius - 5:
    print("Rocket Crashed!")
    break

plt.plot(t[:len(mass)], mass)
plt.xlabel("Time (s)")
plt.ylabel("Total Mass (kg)")
plt.title("Rocket Total Mass Profile (Successful Step-Down Staging)")
plt.grid(True)
plt.show()

earth_angle = np.linspace(0, 2 * math.pi, 500)
plt.plot(Earth_radius * np.cos(earth_angle), Earth_radius * np.sin(earth_angle), color='g', linestyle = '--', label = 'Earth Surface')
plt.plot(displacement_x, displacement_y, label = 'Rocket Path')
plt.xlabel("X Position (meters)")
plt.ylabel("Y Position (meters)")
plt.title("2D Physical Trajectory (Equatorial View)")
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.show()

plt.plot(t[:len(mass)], displacement_x)
plt.title("Horizontal Position (X) over Time")
plt.xlabel("Time (s)")
plt.ylabel("X Coordinate (m)")
plt.grid(True)
plt.show()

plt.plot(t[:len(mass)], displacement_y)
plt.title("Vertical Position (Y) over Time")
plt.xlabel("Time (s)")
plt.ylabel("Y Coordinate (m)")
plt.grid(True)
plt.show()

plt.plot(t[:len(mass)], velocity_x)
plt.title("Horizontal Velocity (Vx) over Time")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.grid(True)
plt.show()

plt.plot(t[:len(mass)], velocity_y)
plt.title("Vertical Velocity (Vy) over Time")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.grid(True)
plt.show()

# ============================================================
# FALCON 9 INSPIRED 2D ROCKET SIMULATION
# ============================================================
#
# FEATURES:
# - Two-dimensional vector motion
# - Fuel burn and mass reduction
# - Two-stage rocket
# - Atmospheric drag
# - Gravity turn
# - Universal gravitation
# - Orbital insertion
#
# FLIGHT PROFILE:
# 1. Launch using Stage 1 thrust.
# 2. Burn propellant, reducing total mass over time.
# 3. Begin a gravity turn after some time.
# 4. Separate Stage 1 and switch to Stage 2 thrust.
# 5. Separate Stage 2 and coast after engine cutoff.
# 6. Continue under gravity until orbital conditions are reached.
#
# GRAVITY TURN:
# The rocket begins pointed radially outward from Earth.
# A small pitch angle is added every timestep, gradually
# rotating thrust toward the horizon and building the
# horizontal velocity required for orbit.
#
# ORIENTATION LOGIC:
# "Up" changes as the rocket moves around Earth.
# radial_angle = atan2(y, x) gives the local vertical direction.
# world_thrust_angle = radial_angle + pitch_angle
# This keeps the rocket aligned with Earth's curvature while allowing a controllable gravity turn.
#
# GRAVITY LOGIC:
# 1. ACCELERATION CONSTANCY:
#    - MAGNITUDE is constant ONLY in perfectly circular orbits (GM/r^2).
#    - DIRECTION changes every time-step, so the acceleration VECTOR is dynamic.
# 2. VECTOR-BASED DIRECTION (No Trigonometry/Unit Circles Needed):
#    - Satellite Position Vector: r_vec = (x, y)
#    - Straight-line Distance:    r = sqrt(x^2 + y^2)
#    - Target Direction (Inward): -r_vec = (-x, -y)
#    - Unit Vector (Length = 1):  u_hat = (-x/r, -y/r)
#    - Find Gravity:   a_mag = G * M / r^2
#    - Apply Unit Vec: ax = a_mag * (-x / r)  =>  -G * M * x / r^3
#                      ay = a_mag * (-y / r)  =>  -G * M * y / r^3
# 3. CORE SIMULATION ENGINE LOOP (Per Time-Step dt):
#    - Find Distance:  r = sqrt(x^2 + y^2)
#    - Find Gravity:   a_mag = G * M / r^2
#    - Apply Unit Vec: ax = a_mag * (-x / r)  =>  -G * M * x / r^3
#                      ay = a_mag * (-y / r)  =>  -G * M * y / r^3
#    - Integrate Vel:  vx += ax * dt
#                      vy += ay * dt
#    - Integrate Pos:  x  += vx * dt
#                      y  += vy * dt
#
# This automatically updates gravity's direction without needing angle calculations.
