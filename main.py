import numpy as np
import matplotlib.pyplot as plt

# Lorenz paramters and initial conditions
sigma, beta, rho = 10, 2.667, 28
u0, v0, w0 = 0, 1, 1.05

# Maximum time point and total number of time points
tmax, n = 100, 10000

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

# Create 3D plot
fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot3D(x, y, z, 'gray')

plt.show()