import numpy as np
from wag_the_dog import wag_the_dog


def main():
    potential_width = 1.0
    positions = np.linspace(-3*potential_width, 3 * potential_width, num=10000)

    n = 1   # Initial Energy State
    n_max = 3  # Final Energy State

    while n <= n_max:
        k = (2*n) + 1
        wag_range = np.linspace(0.85, 1.15, num=5)
        adjustable_coefficients = k * wag_range
        initial_conditions = (1., 0.)  # psi(0), psi'(0)
        wag_the_dog('harmonic oscillator', adjustable_coefficients, potential_width, positions, initial_conditions)
        n += 1


if __name__ == "__main__":
    main()
