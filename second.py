import numpy as np

def rk4_second_order(f, x0, y0, z0, h, steps):
    x = x0
    y = y0
    z = z0
    
    results = [(x, y, z)]
    
    for _ in range(steps):
        k1 = h * z
        l1 = h * f(x, y, z)
        
        k2 = h * (z + 0.5 * l1)
        l2 = h * f(x + 0.5 * h, y + 0.5 * k1, z + 0.5 * l1)
        
        k3 = h * (z + 0.5 * l2)
        l3 = h * f(x + 0.5 * h, y + 0.5 * k2, z + 0.5 * l2)
        
        k4 = h * (z + l3)
        l4 = h * f(x + h, y + k3, z + l3)
        
        y += (k1 + 2 * k2 + 2 * k3 + k4) / 6.0
        z += (l1 + 2 * l2 + 2 * l3 + l4) / 6.0
        x += h
        
        results.append((x, y, z))
        
    return results

d2y_dx2 = lambda x, y, z: -y

x0 = 0.0
y0 = 1.0
z0 = 0.0

h = 0.1
steps = 5

numerical_data = rk4_second_order(d2y_dx2, x0, y0, z0, h, steps)

print(f"{'x':>5} | {'RK4 Approximation (y)':>21} | {'Exact Solution cos(x)':>21}")
print("-" * 55)
for x_val, y_val, _ in numerical_data:
    exact_val = np.cos(x_val)
    print(f"{x_val:>5.1f} | {y_val:>21.5f} | {exact_val:>21.5f}")
