# Filip Jovanovic, Quantum Mechanics Homework 3A, Gram Schmidt Orthonormalization, April 19, 2021
import numpy as np

M = np.array([[1.0 + 1j, 1j, 0],
              [1.0, 3.0, 28.0],
              [1j, 1.0, 8.0]])


def gram_schmidt(A):
    """Orthogonalize a set of vectors stored as the columns of matrix A."""
    # Get the number of vectors.
    n = A.shape[1]
    for j in range(n):
        # To orthogonalize the vector in column j with respect to the
        # previous vectors, subtract from it its projection onto
        # each of the previous vectors.
        for k in range(j):
            A[:, j] -= (np.vdot(A[:, j], A[:, k])/np.vdot(A[:, j], A[:, j])) * A[:, k]
        A[:, j] = A[:, j] / np.linalg.norm(A[:, j])
    return A


print(gram_schmidt(M))



