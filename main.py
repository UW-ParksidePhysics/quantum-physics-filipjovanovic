import numpy as np
from wag_the_dog import wag_the_dog


def main():
    potential_width = 1.0
    positions = np.linspace(-2 * potential_width, 2 * potential_width, num=10000)
    #k_squared = (np.pi / potential_width)**2  # k_1 = pi/a ==> k_1^2 = pi^2 / a^2
    k = 1
    wag_range = np.linspace(0.5, 1.5, num=5)
    adjustable_coefficients = k * wag_range
    initial_conditions = (0.01, 0.)  # psi(0), psi'(0)
    wag_the_dog('harmonic oscillator', adjustable_coefficients, potential_width, positions, initial_conditions)


if __name__ == "__main__":
    main()
