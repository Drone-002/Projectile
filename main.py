import numpy as np
import matplotlib.pyplot as plt
print("Welcome to the Projectile Motion Simulator")
vinit = input("Enter the Initial Velocity")
angle = input("Enter the Projection angle in degrees")
ainrad = np.deg2rad(angle)
g = 9.8


tof = 2*vinit*np.sin(angle)/g
t = np.linspace(0, tof, 200)
px = vinit*np.cos(angle)*t
py = vinit* np.sin(angle)*0.5*g*t**2
hmax = (vinit*np.sin(ainrad))**2/(2*g)
r = (vinit*np.sin(2*ainrad))/g 

print("Time of flight={tof}s")
print("The x position={px}")
print("The y position={py}")
print("Maximum height={hmax}m")
print("Range={r}")


plt.figure(figsize=(10))
plt.plot(px, py, label=f"vinit={vinit}m/s, angle={angle}")
plt.grid(True, linestyle="--", alpha=1)
plt.Title("Projectile Motion")
plt.xlabel("Horizontal Distance")
plt.ylabel("Vertical Distance")
plt.legend()
plt.show()
