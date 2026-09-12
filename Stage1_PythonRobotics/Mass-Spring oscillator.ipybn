import numpy as np
import matplotlib.pyplot as plt

# Physical parameters
m = 1.0       # mass
k = 10.0      # spring constant
x0 = 1.0      # initial position
v0 = 0.0      # initial velocity

# Time settings
dt = 0.001
T = 10
N = int(T/dt)

# Arrays
x = np.zeros(N)
v = np.zeros(N)
t = np.linspace(0, T, N)

x[0] = x0
v[0] = v0

def dxdt(v):
    return v

def dvdt(x):
    return -(k/m)*x

# RK4 loop
for i in range(N-1):
    k1x = dxdt(v[i])
    k1v = dvdt(x[i])

    k2x = dxdt(v[i] + 0.5*dt*k1v)
    k2v = dvdt(x[i] + 0.5*dt*k1x)

    k3x = dxdt(v[i] + 0.5*dt*k2v)
    k3v = dvdt(x[i] + 0.5*dt*k2x)

    k4x = dxdt(v[i] + dt*k3v)
    k4v = dvdt(x[i] + dt*k3x)

    x[i+1] = x[i] + (dt/6)*(k1x + 2*k2x + 2*k3x + k4x)
    v[i+1] = v[i] + (dt/6)*(k1v + 2*k2v + 2*k3v + k4v)

# Plot
plt.plot(t, x)
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.title("Mass-Spring Oscillator")
plt.grid()
plt.show()
