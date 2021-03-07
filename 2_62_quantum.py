# Problem 2.62 Quantum Physics,
# Filip Jovanovic,
# 3/8/2021

import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as la
import scipy.sparse.linalg as spla

# Initialize Matrix (and some other stuff...)
n = 100
N = np.arange(n)
A = np.zeros((n, n))

# Define Constants
hbar = 1 # Planck's constant
m = 1  # Mass
a = 1  # Well width
V0 = (hbar**2)/(m*a**2)  # Initial Potential
L = V0*(n+1)**2  # Lambda
b = n + 1   # delx/a

# Create the Matrix
for i in N:
    for j in N:
        if i == j:
            A[i, j] = (2 + (500/L)*np.sin((np.pi * (j+1)/b)))
        elif i == j + 1:
            A[i, j] = -1
        elif i == j - 1:
            A[i, j] = -1


# Find the eigenvalues and eigenvectors

vals, vecs = spla.eigs(A, k=3, which='SR', return_eigenvectors=True)
print("Energy #1:", L*vals.real[0])
print("Energy #2:", L*vals.real[1])
print("Energy #3:", L*vals.real[2])


fig, ax = plt.subplots()

plt.axhline(color='black')
ax.set_title('Wave Functions')
ax.set_ylabel(r"$\Psi$")
ax.set_xlabel('x')

# set x, y-axis limits
ax.set_xlim(0, 100)
ax.set_ylim(-0.2, 0.2)

ax.plot((vecs.real[:, 0]), label=r"$\Psi_{1}$", color="green")
ax.plot((vecs.real[:, 1]), label=r"$\Psi_{2}$", color="red")
ax.plot((vecs.real[:, 2]), label=r"$\Psi_{3}$", color="blue")
plt.legend()
plt.show()

