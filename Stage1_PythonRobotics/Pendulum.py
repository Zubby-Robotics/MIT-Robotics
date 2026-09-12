import numpy as np
import matplotlib.pyplot as plt

# Initializing parameters
m = 1
g = 9.80665
L = 4
theta0 = 60
omega0 = -7

# Time settings
dt = 0.001
T = 10
N = int(T/dt)

# Arrays
theta = np.zeros(N)
omega = np.zeros(N)
t = np.linspace(0, T, N)

theta[0] = theta0
omega[0] = omega0

# Setting up the differential equations
def dthetadt(omega):
    return omega

def domegadt(theta):
    return -g/L*sin(theta)

# RK4 Loop
for i in range(N-1):
    k1theta = dthetadt(omega[i])
    k1omega = domegadt(theta[i], omega[i])

    k2theta = dthetadt(omega[i] + 0.5*dt*k1omega)
    k2omega = domegadt(theta[i] + 0.5*dt*k1theta)

    k3theta = dthetadt(omega[i] + 0.5*dt*k2omega)
    k3omega = domegadt(theta[i] + 0.5*dt*k2x)

    k4theta = dthetadt(omega[i] + dt*k3omega)
    k4omega = domegadt(theta[i] + dt*k3theta)

    theta[i+1] = theta[i] + (dt/6)*(k1theta + 2*k2theta + 2*k3theta + k4theta)
    omega[i+1] = omega[i] + (dt/6)*(k1omega + 2*k2omega + 2*k3omega + k4omega)

# Plot
plt.plot(t, theta)
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.title("Pendulum")
plt.grid()
plt.show()
