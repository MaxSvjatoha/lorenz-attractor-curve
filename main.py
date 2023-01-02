import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

preset = False

if preset:
    # Lorenz paramters and initial conditions, preset:
    sigma, beta, rho = 10, 2.667, 28
    u0, v0, w0 = 0, 1, 1.05
else:
    # Lorenz paramters and initial conditions, random:
    sigma, beta, rho = np.random.uniform(0, 20), np.random.uniform(0, 5), np.random.uniform(0, 30)
    u0, v0, w0 = np.random.uniform(0, 2), np.random.uniform(0, 2), np.random.uniform(0, 2)
    
print(f"sigma: {sigma}, beta: {beta}, rho: {rho}")
print(f"u0: {u0}, v0: {v0}, w0: {w0}")

# Maximum time point and total number of time points
#tmax, n = 100, 10000
tmax, n = 30, 900

# Time step
dt = tmax / n

# Create arrays to store the solution
t = np.arange(0, tmax, dt)
x = np.empty(n)
y = np.empty(n)
z = np.empty(n)

# Set initial conditions
x[0], y[0], z[0] = u0, v0, w0

# Iterate over the time steps to solve the system
for i in range(1, n):
    x[i] = x[i-1] + dt * sigma * (y[i-1] - x[i-1])
    y[i] = y[i-1] + dt * (x[i-1] * (rho - z[i-1]) - y[i-1])
    z[i] = z[i-1] + dt * (x[i-1] * y[i-1] - beta * z[i-1])

# Create figure and 3D axis
fig = plt.figure()
ax = plt.axes(projection='3d')

# Set axis limits
ax.set_xlim((-30, 30))
ax.set_ylim((-30, 30))
ax.set_zlim((0, 50))

# Set line colors
colors = plt.cm.cool(np.linspace(0, 1, n))

# Create line objects
lines = [ax.plot([], [], [], '-', c=c)[0] for c in colors]

# Set up the animation
def init():
    for line in lines:
        line.set_data([], [])
        line.set_3d_properties([])
    return lines

def animate(i):
    for j, line in enumerate(lines):
        line.set_data(x[:i], y[:i])
        line.set_3d_properties(z[:i])
    return lines

# Create the animation
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=n, interval=20, blit=True)

# Set the file name (use all 6 initial conditions as file name)
file_name = f"lorenz__sigma_{sigma}__beta_{beta}__rho_{rho}__u0_{u0}__v0_{v0}__w0_{w0}.gif"

# Save the animation
anim.save(file_name, writer='Pillow', fps=20)