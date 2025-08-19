import numpy as np
import matplotlib.pyplot as plt

def get_trajectory(v0, angle_deg, g=9.81, steps=100):
    angle_rad = np.deg2rad(angle_deg)
    
    t_flight = 2 * v0 * np.sin(angle_rad) / g
    t = np.linspace(0, t_flight, steps)
    
    x = v0 * np.cos(angle_rad) * t
    y = v0 * np.sin(angle_rad) * t - 0.5 * g * t**2
    
    return x, y


def plot_trajectory(v0, angle_deg, g=9.81):
    x, y = get_trajectory(v0, angle_deg, g)
    
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label=f"{v0} m/s @ {angle_deg}°")
    plt.title("Projectile Motion Simulator")
    plt.xlabel("Distance (m)")
    plt.ylabel("Height (m)")
    plt.legend()
    plt.grid(True)
    plt.savefig("img.png")


if __name__ == "__main__":
    print("Projectile Motion Simulator")
    v0 = float(input("Enter initial velocity (m/s): "))
    angle = float(input("Enter launch angle (degrees): "))
    
    plot_trajectory(v0, angle)

