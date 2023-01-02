import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
from matplotlib import animation

# TODO: Add additional functionality

preset = False
save_animation = True

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
x = np.empty((n+1,))
y = np.empty((n+1,))
z = np.empty((n+1,))

# Set initial conditions
x[0], y[0], z[0] = u0, v0, w0

# Iterate over the time steps to solve the system
print("Solving the system...")
for i in tqdm(range(n)):
    x[i+1] = x[i] + dt * sigma * (y[i] - x[i])
    y[i+1] = y[i] + dt * (x[i] * (rho - z[i]) - y[i])
    z[i+1] = z[i] + dt * (x[i] * y[i] - beta * z[i])

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

print("Creating the animation...")

# Create the animation
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=n, interval=20, blit=True)

if save_animation:
    # Set the file name (use all 6 initial conditions as file name)
    file_name = f"lorenz__sigma_{sigma}__beta_{beta}__rho_{rho}__u0_{u0}__v0_{v0}__w0_{w0}.gif"

    print(f"Saving the animation as {file_name}...")

    # set up progress bar
    tqdm.write("Saving animation, please wait...")
    with tqdm(total=n) as pbar:
        # save the animation
        anim.save(file_name, writer="ffmpeg", progress_callback=lambda i, n: pbar.update(1))

    # clear the progress bar
    tqdm.write("\nDone!")
else:
    print("Showing the animation...")
    plt.show()