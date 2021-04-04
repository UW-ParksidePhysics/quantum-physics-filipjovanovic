# Filip Jovanovic, Quantum Mechanics Homework 3A, Gram Shmidt Orthonormalization, April 5, 2021
import numpy as np


e1 = np.array([1j+1,
               1,
               1j])

e2 = np.array([1j,
              3,
              1])

e3 = np.array([0,
              28,
              0])
print("Initial Vectors:")
print(e1)
print(e2)
print(e3)


u1 = e1

u2 = e2 - (np.vdot(e2, u1)/np.vdot(u1, u1)) * u1

u3 = e3 - (np.vdot(e3, u1)/np.vdot(u1, u1)) * u1 - (np.vdot(e3, u2)/np.vdot(u2, u2)) * u2


e1_prime = u1/(np.sqrt(np.vdot(u1, u1)))
e2_prime = u2/(np.sqrt(np.vdot(u2, u2)))
e3_prime = u3/(np.sqrt(np.vdot(u3, u3)))

print("Orthogonalized Vectors:")
print(u1)
print(u2)
print(u3)

# print("Orthogonalized e_i * e_j i not equal to j:")
# print(np.vdot(u1, u2))
# print(np.vdot(u2, u3))
# print(np.vdot(u1, u3))

print("Orthonormalized Vectors:")
print(e1_prime)
print(e2_prime)
print(e3_prime)

# print("Normalized e_n * e_n:")
# print(np.round(np.vdot(e1_prime, e1_prime)))
# print(np.round(np.vdot(e2_prime, e2_prime)))
# print(np.round(np.vdot(e3_prime, e3_prime)))
