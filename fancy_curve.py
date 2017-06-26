import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np

# Parameters
k = 3
t = np.linspace(0, 2*np.pi, 200)
f = k*np.cos(t)

# Calculate stuff
x = 5*np.cos(f)*np.sin(t)
y = 5*np.sin(f)*np.sin(t)
z = 5*np.cos(t)

# Plot
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_xlim(-5,5)
ax.set_ylim(-5,5)
ax.set_zlim(-5,5)
ax.plot(x, y, z, antialiased=True)

# Add details to plot (labels, title, etc.)
rc("text", usetex=True)
plt.title("$f(t) = k\cos(t)$, $x = 5\cos(f(t))\sin(t)$, $y = 5\sin(f(t))\sin(t)$, $z = 5\cos(t)$")

plt.show()