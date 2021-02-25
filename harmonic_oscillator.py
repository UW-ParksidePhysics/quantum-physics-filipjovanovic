import numpy as np
import matplotlib.pyplot as plt


def calculate_harmonic_oscillator_eigenfunctions(eigenfunction_positions, eigenfunction_index,
                                                  harmonic_oscillator_width=1.0):
    """
    :param eigenfunction_positions:  x-values in a Numpy array
    :param eigenfunction_index: n
    :param harmonic_oscillator_width: a
    :return: psi_n(x) from x_minimum to x_maximum
    """
    wave_number = eigenfunction_index * np.pi / harmonic_oscillator_width  # k_n = n * pi / a,  dim(k_n) = L^-1
    normalization_factor = np.sqrt(2 / harmonic_oscillator_width)  # A = sqrt(2 / a),  dim(A) = L^(-1/2)

    # psi_n(x) = A sin(k_n * x),  dim(psi_n) = dim(A) = L^(-1/2)
    harmonic_oscillator_eigenfunction_values = normalization_factor * np.sin(wave_number * eigenfunction_positions)

    return harmonic_oscillator_eigenfunction_values


def draw_harmonic_oscillator_potential(function_positions, harmonic_oscillator_width=1.0,
                                        maximum_potential_value=2.0):
    """
    :param function_positions:  x-values in a Numpy array
    :param harmonic_oscillator_width:  a
    :param maximum_potential_value: sets maximum V (and minimum V = -maximum V)
    :return:
    """
    force_constant = 4 / harmonic_oscillator_width
    minimum_position = np.min(function_positions)
    minimum_potential_position = minimum_position - 0.333 * harmonic_oscillator_width
    maximum_position = np.max(function_positions)
    maximum_potential_position = maximum_position + 0.333 * harmonic_oscillator_width

    potential_positions = np.linspace(minimum_potential_position, maximum_potential_position)
    potential_values = (1/2) * force_constant * potential_positions**2
    plt.fill_between(potential_positions, potential_values,
                     facecolor='gray', alpha=0.2)

    plt.xlim([np.min(potential_positions), np.max(potential_positions)])
    plt.ylim([-maximum_potential_value, maximum_potential_value])

    return


def harmonic_oscillator_differential_equation(xi, psi, k):
    """
    Sets up second-order differential equation for solve_ivp as two linear differential equations
    psi' = psi'
    psi'' = (xi**2 - K)*psi
    :param xi:  position value
    :param psi:  list of wave function and wave-function derivative's values
    :param K: adjustable parameter to find solutions
    :return: psi': list of wave function and wave-function derivative's first derivative values
    """
    dpsi = [0, 0]           # initialize the (psi', psi'') vector
    dpsi[0] = psi[1]        # set psi' = psi'
    dpsi[1] = (xi**2 - k) * psi[0]   # set psi'' = (xi**2 - constant) * psi
    return dpsi
