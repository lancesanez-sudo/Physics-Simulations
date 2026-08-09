
"""
Simulation: Angry Birds Projectile Motion Video Game
This 2D physics simulation uses spring force (either an ideal or realistic, nonlinear S-curve) to launch a bird at a building.
The user must input values for the distance to pull back the slingshot, the angle of launch, and the mass of the bird to see if they can hit the enemy base.
"""

import numpy as np
import matplotlib.pyplot as plt
import math

y = 5
x = 0
v_x = 0
v_y = 0
d = 0.1
g = 9.81
dt = 0.01
t = np.arange(0, 20, dt)

positions_x = []
positions_y = []
velocity_x = []
velocity_y = []

while True:
  try:
    x_spring = float(input("Enter how far you want to retract the slingshot: "))
    break
  except ValueError:
    print("That is not a valid number. Try again!")

k_ideal = 150 #N/m
A_realistic = 2200.0  # N/m^3
B_realistic = -420.0  # N/m^2
C_realistic = 135.0   # N/m

user_choice = input("Do you want to use a realistic slingshot model? (Yes/No): ").strip().lower()

if user_choice in ["yes", "y"]:
    def F_spring(x_spring):
        return (A_realistic * x_spring**3) + (B_realistic * x_spring**2) + (C_realistic * x_spring)
    model_type = "realistic"
else:
    def F_spring(x_spring):
        return k_ideal * x_spring
    model_type = "ideal"

print(f"Using the {model_type} model type at a draw distance of {x_spring} m")

launch_angle = float(input("At what angle do you want to launch? Angle: "))
launch_radians = math.radians(launch_angle)
Bird_mass = float(input("How much mass do you want your bird to be? Mass (kg): "))

class EnemyBase:
    def __init__(self, x_start=10, x_end=13, y_start=0, y_end=21):
        # DESCRIBE THE RANGE
        self.x_coords = np.arange(x_start, x_end, 1)  # [10, 11, 12]
        self.y_coords = np.arange(y_start, y_end, 1)  # [0, 1, ..., 20]

        # Define explicit bounding limits for the check
        self.x_min, self.x_max = self.x_coords[0], self.x_coords[-1]
        self.y_min, self.y_max = self.y_coords[0], self.y_coords[-1]

    def describe_base(self):
        # Prints a description of the base dimensions and area.
        width = len(self.x_coords)
        height = len(self.y_coords)
        print(f"Enemy Base Range Description:")
        print(f" -> X-axis spans from {self.x_min} to {self.x_max} (Width: {width} units)")
        print(f" -> Y-axis spans from {self.y_min} to {self.y_max} (Height: {height} units)")
        print(f" -> Total grid points covered: {width * height} locations\n")

    def is_inside(self, x_positions, y_positions):
        # BOUNDARY CHECK: Returns True if any (x, y) from the trajectory is inside the base.
        for px, py in zip(x_positions, y_positions):
            if (self.x_min <= px <= self.x_max) and (self.y_min <= py <= self.y_max):
                return True
        return False

base = EnemyBase()
base.describe_base()

x_min, x_max = 10, 12
y_min, y_max = 0, 10

E_spring = 0.5 * k_ideal * (x_spring**2)
v_initial = math.sqrt((2 * E_spring) / Bird_mass)
v_x = v_initial * math.cos(launch_radians)
v_y = v_initial * math.sin(launch_radians)

for time in t:
    F_xd = -d * v_x
    F_yd = -d * v_y
    F_g = -Bird_mass * g
    F_xnet = F_xd
    F_ynet = F_yd + F_g
    a_x = F_xnet / Bird_mass
    a_y = F_ynet / Bird_mass
    v_x = v_x + a_x * dt
    v_y = v_y + a_y * dt
    x = x + v_x * dt
    y = y + v_y * dt
    positions_x.append(x)
    positions_y.append(y)
    velocity_x.append(v_x)
    velocity_y.append(v_y)
    if y < 0:
      y = 0
      break

hit_base = base.is_inside(positions_x, positions_y)
print(f"Did you hit the enemy base? {hit_base}")

if hit_base:
  print("VICTORY!")
else:
  print("DEFEAT")

plt.plot(positions_x, positions_y)
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.grid(which = 'both', color = 'gray', linestyle = '-', linewidth = 0.5)
plt.title("Angry Birds Projectile Simulation")
plt.xticks(np.arange(0, 21, 1))
plt.yticks(np.arange(0, 21, 1))
base_rect = plt.Rectangle((x_min, y_min), x_max - x_min, y_max - y_min, color='crimson', alpha=0.25, label='Enemy Base')
ax = plt.gca()
ax.add_patch(base_rect)
plt.legend()
plt.show()
