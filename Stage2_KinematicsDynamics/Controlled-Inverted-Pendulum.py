import numpy as np
import matplotlib.pyplot as plt

# Initializing parameters
M, m = 4, 6
L, g = 5, 9.80665
params = (M, m, L, g)

# Time settings
dt = 0.0001
T = 10
N = int(T/dt)

# Arrays
y = np.zeros((N, 4))
t = np.linspace(0, T, N)

y[0, 0] = 4 
y[0, 1] = 0.5   
y[0, 2] = -2 
y[0, 3] = -0.3

# Setting up the differential equations
def f(y, u, params):
    M, m, L, g = params
    x, v, theta, omega = y

    dx = v
    dv = u/(M +m)
    dtheta = omega
    domega = g/L*theta-u/(L*(M +m))

    return np.array([dx, dv, dtheta, domega])

# RK4 Loop
def rk4_step(y, u, dt, params):
    Kp = 20
    Kd = 5
    Ki = 0.1
    theta = y[i,2]
    dtheta = y[i,3]
    I += theta * dt
    u = -Kp*theta - Kd*dtheta - Ki*I

    k1 = f(y, u, params)
    k2 = f(y + 0.5*dt*k1, u, params)
    k3 = f(y + 0.5*dt*k2, u, params)
    k4 = f(y + dt*k3, u, params)

    return y + (dt/6.0)*(k1 + 2*k2 + 2*k3 + k4)

for i in range(N-1):
    y[i+1] = rk4_step(y[i], u, dt, params)

# Plot
plt.plot(t, y[:,0])
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.title("Inverted pendulum")
plt.grid()
plt.show()
plt.plot(t, y[:,2])
plt.xlabel("Time (s)")
plt.ylabel("Angle (°)")
plt.title("Inverted pendulum")
plt.grid()
plt.show()
