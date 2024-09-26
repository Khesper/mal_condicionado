import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir los coeficientes de los tres planos
# Planos: 
# 1x + 2y + 3z = 6
# 4x + 5.0001y + 6z = 15.0001
# 7x + 8y + 9z = 24

x_vals = np.linspace(-10, 10, 400)
y_vals = np.linspace(-10, 10, 400)

# Crear mallas de valores x e y
X, Y = np.meshgrid(x_vals, y_vals)

# Definir las ecuaciones de los planos
Z1 = (6 - X - 2*Y) / 2.9990  # Primer plano
Z2 = (15.0001 - 4*X - 5*Y) / 6  # Segundo plano
Z3 = (24 - 6.999*X - 8*Y) / 9  # Tercer plano

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z1, alpha=0.5, rstride=100, cstride=100, color='red')
ax.plot_surface(X, Y, Z2, alpha=0.5, rstride=100, cstride=100, color='blue')
ax.plot_surface(X, Y, Z3, alpha=0.5, rstride=100, cstride=100, color='green')


ax.set_title("Intersección de los planos (Sistema mal condicionado)", fontsize=15)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
