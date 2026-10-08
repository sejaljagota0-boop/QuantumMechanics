#runge kutta
import numpy as np
import matplotlib.pyplot as plt

x0 = 0
y0 = 0
z0 = 0

h = 0.1

n = 10

x = np.zeros(n + 1)
y = np.zeros(n + 1)
z = np.zeros(n + 1)

x[0] = x0
y[0] = y0
z[0] = z0


for i in range(n):

    k1 = h * z[i]
    l1 = h * (10 - 2*z[i] - 5*y[i])

    k2 = h * (z[i] + l1/2)
    l2 = h * (10 - 2*(z[i] + l1/2)
              - 5*(y[i] + k1/2))

    k3 = h * (z[i] + l2/2)
    l3 = h * (10 - 2*(z[i] + l2/2)
              - 5*(y[i] + k2/2))

    k4 = h * (z[i] + l3)
    l4 = h * (10 - 2*(z[i] + l3)
              - 5*(y[i] + k3))

    y[i+1] = y[i] + (k1 + 2*k2 + 2*k3 + k4)/6
    z[i+1] = z[i] + (l1 + 2*l2 + 2*l3 + l4)/6

    x[i+1] = x[i] + h

print("x       y        dy/dx")

for i in range(n + 1):
    print(f"{x[i]:.1f}   {y[i]:.6f}   {z[i]:.6f}")

plt.plot(x, y, 'o-')
plt.xlabel("x")
plt.ylabel("y")
plt.title("RK4 Solution")
plt.grid()
plt.show()