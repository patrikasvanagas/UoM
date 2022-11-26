# -*- coding: utf-8 -*-
"""
PHYS20161 Final assignment: Z Boson

This program calculates the mass, width, lifetime and respective uncertainties
for a particle with two datasets containing energies, resulting cross
sections and the uncertainty on the cross sections. This is achieved by
continously varying over the mass and the width and minimizing the chi-squared
fit of the Breit-Wigner expression. The measurements are assumed to be
recorded in GeV and nb. Supporting graphics for the fit are provided.

Patrikas Vanagas ID 10455596 22/12/2021
"""
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fmin
from scipy.optimize import curve_fit
from scipy.constants import hbar as REDUCED_PLANCK_CONSTANT
from scipy.constants import pi as PI
from scipy.constants import eV as ELECTRON_VOLT
from scipy.constants import c as SPEED_OF_LIGHT

BREIT_WIGNER_FACTOR = (
    ((REDUCED_PLANCK_CONSTANT * SPEED_OF_LIGHT) / (ELECTRON_VOLT * 10 ** 9))
    ** 2
    / (10 ** -28)
    * 1000
)
PARTIAL_WIDTH = 83.91
START_MASS = 90
START_WIDTH = 3


DATASET_1_DIR = "z_boson_data_1.csv"
DATASET_2_DIR = "z_boson_data_2.csv"


def files_exist():
    '''
    Checks whether both files containing data are in the working directory.
    If one is not, the execution of the program is stopped.

    Returns
    -------
    None.

    '''
    if not os.path.isfile(DATASET_1_DIR):
        sys.exit(DATASET_1_DIR + " is not found, please review.\n")
    if not os.path.isfile(DATASET_2_DIR):
        sys.exit(DATASET_2_DIR + " is not found, please review.\n")


def read_and_combine_data():
    """
    Reads the data from the specified data files and combines it into
    a single numpy array. Returns None if operation is unsuccesful.

    Returns
    -------
    Numpy array if successful, None if unsuccesful
        2d numpy array, first column is energy data, second column is cross-
        section data, third column is cross-section uncertainty.

    """
    dataset_1 = np.genfromtxt(DATASET_1_DIR, comments="%", delimiter=",")
    dataset_2 = np.genfromtxt(DATASET_2_DIR, comments="%", delimiter=",")
    try:
        return np.append(dataset_1, dataset_2, axis=0)
    except ValueError:
        print(
            "Datafiles do not conform to specified 3 column format, please "
            + "review.\n"
        )
        return None


def filter_useless_rows(dataset):
    """
    Deletes rows where either the entry is non-numeric, less than zero, or has
    at least one variable equal to zero from the dataset.

    Parameters
    ----------
    dataset : numpy array
        2d numpy array, first column is energy data, second column is cross-
        section data, third column is cross-section uncertainty.

    Returns
    -------
    numpy array
        2d numpy array, first column is energy data, second column is cross-
        section data, third column is cross-section uncertainty without deleted
        entries

    """
    nan_rows = np.where(np.isnan(dataset))[0]
    negative_rows = np.where(dataset < 0)[0]
    zero_rows = np.where(dataset == 0)[0]
    rows_to_delete = np.concatenate(
        (nan_rows, negative_rows, zero_rows), axis=0
    )
    return np.delete(dataset, np.unique(rows_to_delete), axis=0)


def filter_immediate_outliers(dataset):
    """
    Calculates the mean and standard deviation of the cross-section for a
    dataset, and then deletes entries which are more than 7 standard deviations
    away from the mean, preventing anomalous datapoints.

    Parameters
    ----------
    dataset : numpy array
        2d numpy array, first column is energy data, second column is cross-
        section data, third column is cross-section uncertainty.

    Returns
    -------
    dataset : numpy array
        2d numpy array, first column is energy data, second column is cross-
        section data, third column is cross-section uncertainty.

    """
    counter = 0
    while 1:
        counter += 1
        average_ordinate = np.average(dataset[:, 1])
        standard_deviation_limit = np.std(dataset[:, 1]) * 7
        rows_to_delete = np.where(
            abs(dataset[:, 1])
            > abs(average_ordinate + standard_deviation_limit)
        )
        if rows_to_delete[0].size > 0:
            print(
                "Removing datapoints for which ordinates are at least 7"
                + " standard deviations away from the mean cross-section "
                + "(round {0:g}):".format(counter)
            )
            for i in range(len(rows_to_delete[0])):
                print(
                    "\u03C3={0:4.3f} nb is deleted.".format(
                        dataset[rows_to_delete[0]][i][1]
                    )
                )
            print("\n")
            dataset = np.delete(dataset, rows_to_delete, axis=0)
        elif rows_to_delete[0].size == 0:
            break
    return dataset


def breit_wigner_expression(dataset, mass_and_width):
    """
    Calculates the cross section according to the Breit-Wigner expression from
    a given dataset. Arguments to use with scipy.optimize.fmin

    Parameters
    ----------
    dataset : numpy array
        2d numpy array, first column is energy data, second column is cross-
        section data, third column is cross-section uncertainty.
    mass_and_width : numpy array
        1d numpy array, the first term is the particle mass and the second term
        is the particle width

    Returns
    -------
    numpy array
        1d numpy array of calculated cross-sections

    """
    return (
        (12 * PI * dataset[:, 0] ** 2 * PARTIAL_WIDTH ** 2)
        / (
            mass_and_width[0] ** 2
            * (
                (dataset[:, 0] ** 2 - mass_and_width[0] ** 2) ** 2
                + mass_and_width[0] ** 2 * mass_and_width[1] ** 2
            )
        )
        * BREIT_WIGNER_FACTOR
    )


def breit_wigner_expression_for_uncertainty(dataset, *mass_and_width):
    """
    Calculates the cross section according to the Breit-Wigner expression from
    a given dataset. Exactly same as previious functions, just with the order
    the arguments changed for use with scipy.optimize.curve_fit

    Parameters
    ----------
    dataset : numpy array
        2d numpy array, first column is energy data, second column is cross-
        section data, third column is cross-section uncertainty.
    mass_and_width : numpy array
        1d numpy array, the first term is the particle mass and the second term
        is the particle width

    Returns
    -------
    numpy array
        1d numpy array of calculated cross-sections

    """
    return (
        (12 * PI * dataset[:, 0] ** 2 * PARTIAL_WIDTH ** 2)
        / (
            mass_and_width[0] ** 2
            * (
                (dataset[:, 0] ** 2 - mass_and_width[0] ** 2) ** 2
                + mass_and_width[0] ** 2 * mass_and_width[1] ** 2
            )
        )
        * BREIT_WIGNER_FACTOR
    )


def chi2_function(mass_and_width, dataset):
    """
    Calculates the chi squared value using the Breit-Wigner expression for a
    specific particle mass, width and dataset.

    Parameters
    ----------
    mass_and_width : numpy array
        1d numpy array, the first term is the particle mass and the second term
        is the particle width.
    dataset : numpy array
        2d numpy array, first column is energy data, second column is cross-
        section data, third column is cross-section uncertainty.

    Returns
    -------
    float
        The calculated chi-squared value for given inputs.

    """
    return np.sum(
        (
            (breit_wigner_expression(dataset, mass_and_width) - dataset[:, 1])
            / dataset[:, 2]
        )
        ** 2
    )


def fitting_procedure(dataset, mass_and_width_guess):
    """
    Performs the minimised chi_squared fit on the previously defined chi-
    squared function using the downhill simplex approach to find the optimal
    particle mass and width.

    Parameters
    ----------
    dataset : numpy array
        2d numpy array, first column is energy data, second column is cross-
        section data, third column is cross-section uncertainty.
    mass_and_width_guess : numpy array
        1d numpy array, the first term is the initial guess for particle mass
        and the second term is the guess for particle width

    Returns
    -------
    tuple
        first element is a numpy array containing the optimised mass and
        width; the second element is a float value the chi-squared function at
        these optimized parameters

    """
    return fmin(
        chi2_function, mass_and_width_guess, (dataset,), full_output=1, disp=0,
    )[:2]


def find_fitted_parameters_uncertainty(dataset, mass_and_width):
    """
    Calculates the uncertainty on the optimized mass and width of a particle
    for a given dataset with the covariance matrix diagonals using
    scipy.optimize.curve_fit

    Parameters
    ----------
    dataset : numpy array
        2d numpy array, first column is energy data, second column is cross-
        section data, third column is cross-section uncertainty.
    mass_and_width : numpy array
        1d numpy array, the first term is the optimized particle mass and the
        second term is the optimized particle width

    Returns
    -------
    numpy array
        1d numpy array containing the calculated uncertainty for the optimized
        mass and the optimized width

    """
    return np.sqrt(
        np.diag(
            curve_fit(
                breit_wigner_expression_for_uncertainty,
                (dataset),
                dataset[:, 2],
                p0=mass_and_width,
            )[1]
        )
    )


def reduced_chi2_calculation(dataset, minimum):
    """
    Calculates the reduced chi squared according to the minimum value of the
    chi-squared and the length of the dataset

    Parameters
    ----------
    dataset : numpy array
        2d numpy array, first column is energy data, second column is cross-
        section data, third column is cross-section uncertainty.
    minimum : float
        The value of the minimized chi-squared function at the optimized
        parameters

    Returns
    -------
    float
        The reduced chi-squared for a given dataset and minimum chi-squared

    """
    return minimum / (len(dataset) - 2)


def filter_outliers_from_fit(dataset, mass_and_width):
    """
    For given values of the mass and the width of the particle, deletes
    datapoints which are more than 3 standard deviations away from the fitted
    function

    Parameters
    ----------
    dataset : numpy array
        2d numpy array, first column is energy data, second column is cross-
        section data, third column is cross-section uncertainty.
    mass_and_width : numpy array
        1d numpy array, the first term is the particle mass and the second term
        is the particle width used for the fit

    Returns
    -------
    dataset : numpy array
        2d numpy array, first column is energy data, second column is cross-
        section data, third column is cross-section uncertainty without deleted
        entries

    """
    rows_to_delete = np.where(
        abs(dataset[:, 1] - breit_wigner_expression(dataset, mass_and_width))
        > abs(dataset[:, 2]) * 3
    )
    if rows_to_delete[0].size > 0:
        print(
            "Removing datapoints for which ordinates are at least 3"
            + " standard deviations away from the initial fit:"
        )
        for i in range(len(rows_to_delete[0])):
            print(
                "\u03C3={0:4.3f} nb is deleted.".format(
                    dataset[rows_to_delete[0]][i][1]
                )
            )
        print("\n")
        dataset = np.delete(dataset, rows_to_delete, axis=0)
    return dataset


def lifetime_calculation(width, width_error):
    """
    Calculates the lifetime of a particle for a given width and its uncertainty

    Parameters
    ----------
    width : float
        The width of a given particle
    width_error : float
        Error for the given width of a particle

    Returns
    -------
    float
        The calculated lifetime of a particle
    float
        The calculated error on the lifetime of a particle

    """
    return (
        REDUCED_PLANCK_CONSTANT * 10 ** 9 * width,
        REDUCED_PLANCK_CONSTANT * width_error * 10 ** 9,
    )


def results_printing(
    dataset,
    mass_and_width,
    mass_and_width_uncertainties,
    lifetime_and_uncertainty,
    chi2_reduced,
):
    """
    Prints the results obtained from the fitting procedure

    Parameters
    ----------
    dataset : numpy array
        2d numpy array, first column is energy data, second column is cross-
        section data, third column is cross-section uncertainty.
    mass_and_width : numpy array
        1d numpy array, the first term is the particle mass and the second term
        is the particle width
    mass_and_width_uncertainties : numpy array
        1d numpy array, the first term is the error particle mass and the
        second term is the error on particle width
    lifetime_and_uncertainty : tuple
        The first element is the float of the particle lifetime and the second
        is the error on it
    chi2_reduced : float
        The calculated value of the reduced chi-squared from the fit

    Returns
    -------
    None.

    """
    print(
        "Mass of the particle is found to be"
        + " {0:4.2f} ± {1:4.2f} GeV/c^2.".format(
            mass_and_width[0], mass_and_width_uncertainties[0]
        )
    )
    print(
        "Width is found to be {0:4.3f} ± {1:4.3f} GeV.".format(
            mass_and_width[1], mass_and_width_uncertainties[1]
        )
    )
    print(
        "In turn, the lifetime is {0:3.2e} ± {1:1.1e} s.".format(
            lifetime_and_uncertainty[0], lifetime_and_uncertainty[1]
        )
    )
    print(
        "The results were obtained from a reduced "
        + "chi-squared fit of {0:4.3f} with {1:g} datapoints.".format(
            chi2_reduced, len(dataset)
        )
    )

def uncertainties_on_fit_calculation(
    dataset, mass_and_width, mass_and_width_uncertainties
):
    '''
    Calculates the standard deviation on each evaluated datapoint from the
    fit by taking the half of the fit function from the positive bound of the
    parameter uncertainties minus fit function from the negative bound of the
    parameter uncertainties

    Parameters
    ----------
    dataset : numpy array
        2d numpy array, first column is energy data, second column is cross-
        section data, third column is cross-section uncertainty.
    mass_and_width : numpy array
        1d numpy array, the first term is the particle mass and the second term
        is the particle width
    mass_and_width_uncertainties : numpy array
        1d numpy array, the first term is the error particle mass and the
        second term is the error on particle width

    Returns
    -------
    numpy array
        1d numpy array containing uncertainties for each datapoint resulting
        from the fit

    '''
    mass_and_width_plus_uncertainties = (
        mass_and_width + mass_and_width_uncertainties
    )
    mass_and_width_minus_uncertainties = (
        mass_and_width - mass_and_width_uncertainties
    )
    fit_plus_sigma = breit_wigner_expression(
        dataset, mass_and_width_plus_uncertainties
    )
    fit_minus_sigma = breit_wigner_expression(
        dataset, mass_and_width_minus_uncertainties
    )
    return abs(fit_plus_sigma - fit_minus_sigma) / 2

def fit_plot(dataset, mass_and_width, uncertainties_on_fit):
    '''
    Plots and saves a figure comparing the measured data with the obtained fit,
    including uncertainties

    Parameters
    ----------
    dataset : numpy array
        2d numpy array, first column is energy data, second column is cross-
        section data, third column is cross-section uncertainty.
    mass_and_width : numpy array
        1d numpy array, the first term is the particle mass and the second term
        is the particle width
    uncertainties_on_fit : numpy array
        1d numpy array; standard deviation on each evaluated datapoint from
        the fit

    Returns
    -------
    None.

    '''
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.errorbar(
    dataset[:, 0],
    breit_wigner_expression(dataset, mass_and_width),
    uncertainties_on_fit,
    fmt="D",
    alpha = 1,
    label=r"$\sigma$ from $\chi^2$ fit with error"
)
    ax.errorbar(
    dataset[:, 0],
    dataset[:, 1],
    dataset[:, 2],
    fmt="D",
    alpha = 0.8,
    label=r"Measured $\sigma$ with error",
)
    ax.set_title("Breit-Wigner expression fit", fontsize=16, fontname="Arial")
    ax.legend(loc="upper left", fontsize=11)
    ax.set_ylabel(r"Cross section $\sigma$, nb", fontsize=14, fontname="Arial")
    ax.set_xlabel("Energy $E$, GeV", fontsize=14, fontname="Arial")
    ax.annotate((r'Fit: $m_z$ = {0:4.2f} GeV/$c^2$, $\Gamma_z$ = {1:4.3f} GeV'.
                              format(mass_and_width[0], mass_and_width[1])),
                (1, 0), (-300, -50),
                            xycoords='axes fraction', va='top',
                            textcoords='offset points', fontsize='12')
    plt.savefig('Breit_Wigner_expression_fit.png', dpi=400)
    plt.show()

def main():
    '''
    Main code of the program; calls the functions.

    Returns
    -------
    None.

    '''
    files_exist()
    full_dataset = read_and_combine_data()
    if full_dataset is not None:
        full_dataset = filter_useless_rows(full_dataset)
        full_dataset = filter_immediate_outliers(full_dataset)
        z_boson_mass_and_width, minimum_chi2 = fitting_procedure(
            full_dataset, [START_MASS, START_WIDTH]
        )
        z_boson_mass_and_width_errors = find_fitted_parameters_uncertainty(
            full_dataset, z_boson_mass_and_width
        )
        reduced_chi2 = reduced_chi2_calculation(full_dataset, minimum_chi2)
        full_dataset = filter_outliers_from_fit(
            full_dataset, z_boson_mass_and_width
        )
        z_boson_mass_and_width, minimum_chi2 = fitting_procedure(
            full_dataset, z_boson_mass_and_width
        )
        z_boson_mass_and_width_errors = find_fitted_parameters_uncertainty(
            full_dataset, z_boson_mass_and_width
        )
        reduced_chi2 = reduced_chi2_calculation(full_dataset, minimum_chi2)
        z_boson_lifetime_and_uncertainty = lifetime_calculation(
            z_boson_mass_and_width[1], z_boson_mass_and_width_errors[1]
        )
        results_printing(
            full_dataset,
            z_boson_mass_and_width,
            z_boson_mass_and_width_errors,
            z_boson_lifetime_and_uncertainty,
            reduced_chi2,
        )
        fit_errors = uncertainties_on_fit_calculation(
            full_dataset, z_boson_mass_and_width, z_boson_mass_and_width_errors
        )
        fit_plot(full_dataset, z_boson_mass_and_width, fit_errors)


if __name__ == "__main__":
    main()
