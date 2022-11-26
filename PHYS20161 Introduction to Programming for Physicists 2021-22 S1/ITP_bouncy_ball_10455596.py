# -*- coding: utf-8 -*-
"""
PHYS20161 1st assignment: Bouncy Ball

This program investigates situation when a ball is droped from a specified
initial height and after each bounce the ball returns to a height that is
its previous maximum times a constant which is from 0 to 1. The user is asked
to input the initial height, a minimum height of interest and the bounce
constant. The program validates all inputs and calculates how many times the
ball will bounce above the specified minimum height and the time these bounces
will take. Optionally, the user can choose to plot a graph for height vs time
for this process.

Patrikas Vanagas ID 10455596 22/10/2021
"""
# SI units

import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import g as GRAVITATIONAL_CONSTANT


def get_initial_height():
    '''
    Asks the user to input the initial height of the ball in meters, validates
    the input and returns it (float).

    Raises
    ------
    ValueError
        Is raised whenever the user inputs a number which is less or equal to
        zero.

    Returns
    -------
    initial_height : float
        Initial height of the ball.

    '''
    print("\nPlease input the initial height of the ball in meters.")
    while True:
        try:
            initial_height = float(input("Initial height = "))
            if initial_height <= 0:
                raise ValueError
            break
        except ValueError:
            print("Your input must be numerical and greater than zero.")
            continue
    return initial_height


def get_minimum_height(initial_height):
    '''
    Asks the user to input the minimum height of interest for the calculation
    in meters, validates the input and returns it (float).

    Parameters
    ----------
    initial_height : float
        Previously specified initial height of the ball.

    Raises
    ------
    ValueError
        Is raised whenever the user inputs a number which is less or equal to
        zero or larger than the previously specified initial height.

    Returns
    -------
    minimum_height : float
        Minimum height of interest for the calculation.

    '''
    print("\nPlease input the minimum height of interest in meters.")
    while True:
        try:
            minimum_height = float(input("Minimum height = "))
            if minimum_height <= 0 or minimum_height >= initial_height:
                raise ValueError
            break
        except ValueError:
            print(
                "Your input must be numerical, greater than zero, but less \
than the initial height of the ball."
            )
            continue
    return minimum_height


def get_bounce_coefficient():
    '''
    Asks the user to input the bounce coefficient which describes to what
    fraction of the previous maximum the ball will return to after the bounce,
    validates the input and returns it (float).

    Raises
    ------
    ValueError
        Is raised whenever the user inputs a number which is less or equal to
        zero or larger or equal to one.

    Returns
    -------
    bounce_coefficient : float
        Bounce coefficient which describes to what fraction of the previous
        maximum the ball will return to after the bounce.

    '''
    print("\nPlease input the bounce coefficient η between 0 and 1:")
    while True:
        try:
            bounce_coefficient = float(input("Bounce coefficient = "))
            if not 0 < bounce_coefficient < 1:
                raise ValueError
            break
        except ValueError:
            print("Your input must be numerical and between 0 and 1.")
            continue
    return bounce_coefficient


def calculate_bounce_count(initial_height, minimum_height, bounce_coefficient):
    '''
    Calculates how many times the ball will bounce above the specified minimum
    height by looking at the maximum height after each bounce with given
    conditions and returns it (int).

    Parameters
    ----------
    initial_height : float
        Initial height of the ball.
    minimum_height : float
        Minimum height of interest.
    bounce_coefficient : float
        Bounce coefficient which describes to what fraction of the previous
        maximum the ball will return to after the bounce.

    Returns
    -------
    bounce_count : int
        The number of times the ball will bounce above the specified minimum
        height.

    '''
    bounce_count = -1 # set to -1 to account for the initial drop
    while initial_height > minimum_height:
        initial_height = initial_height * bounce_coefficient
        bounce_count += 1
    return bounce_count


def calculate_time_taken(initial_height, bounce_coefficient, bounce_count):
    '''
    Calculates how long the specified number of bounces will take with the
    given conditions by separately considering the initial drop and each
    bounce using SUVAT equations and returns it (float). For the i-th bounce,
    the maximum speed gets multiplied by the bounce coefficient to the power
    half i.

    Parameters
    ----------
    initial_height : float
        Initial height of the ball.
    bounce_coefficient : float
        Bounce coefficient which describes to what fraction of the previous
        maximum the ball will return to after the bounce.
    bounce_count : int
        An integer specifying how many times the ball will bounce.

    Returns
    -------
    time_taken : float
        The time it will take for the ball to complete the specified number of
        bounces.

    '''
    time_taken = np.sqrt(2 * initial_height / GRAVITATIONAL_CONSTANT)
    for i in range(1, bounce_count + 1):
        time_taken += (
            2
            * np.sqrt(2 * bounce_coefficient ** i * initial_height)
            / np.sqrt(GRAVITATIONAL_CONSTANT)
        )
    return time_taken


def print_results(bounce_count, time_taken):
    '''
    Prints the obtained number of bounces and the time taken to complete them
    in a specified format.

    Parameters
    ----------
    bounce_count : int
        An integer specifying how many times the ball will bounce.
    time_taken : float
        The time it will take for the ball to complete a specified number of
        bounces.

    Returns
    -------
    None.

    '''
    if bounce_count == 0:
        print(
            "\nThe ball will not bounce above the specified height. The time \
taken for the initial drop is {0:.2f} seconds.".format(time_taken))
    else:
        print(
            "\nThe number of bounces above the specified height is {0}. \
The total time taken is {1:.2f} seconds.".format(bounce_count, time_taken))


def execute_or_not():
    '''
    Ask the user to confirm whether they want to execute the following action,
    validates the input and returns a corresponding bool.

    Raises
    ------
    ValueError
        Is raised whenever the user inputs anything else but specified strings,
        either 'y' or 'n'.

    Returns
    -------
    bool
        True for 'y' and False for 'n'.

    '''
    while True:
        try:
            continuation_input = input("Yes or no ['y'/'n']? ")
            if continuation_input not in ["y", "n"]:
                raise ValueError
            break
        except ValueError:
            print("\nYour input must be either 'y' for yes or 'n' for no.")
            continue
    return bool(continuation_input == "y")


def print_total_distance(initial_height, bounce_coefficient):
    '''
    Calculates and prints the total distance travelled by the ball by treating
    the process as a diminishing geometric series.

    Parameters
    ----------
    initial_height : float
        Initial height of the ball.
    bounce_coefficient : float
        Bounce coefficient which describes to what fraction of the previous
        maximum the ball will return to after the bounce.

    Returns
    -------
    None.

    '''
    total_distance = initial_height + (
        2 * initial_height * bounce_coefficient
    ) / (1 - bounce_coefficient)
    print(
        "\nThe total distance travelled by the ball is {0:.2f} meters.".format(
            total_distance
        )
    )


def bounce_graph(
        initial_height,
        minimum_height,
        bounce_coefficient,
        bounce_count,
):
    '''
    Plots the graph of the bouncing ball including the first bounce that will
    not reach the specified minimum height by separately considering the
    initial drop and each of the bounces using SUVAT equations. For the i-th
    bounce, the maximum speed gets multiplied by the bounce coefficient to the
    power half i.

    Parameters
    ----------
    initial_height : float
        Initial height of the ball.
    minimum_height : float
        Minimum height of interest.
    bounce_coefficient : float
        Bounce coefficient which describes to what fraction of the previous
        maximum the ball will return to after the bounce.
    bounce_count : int
        The number of times the ball will bounce above the specified minimum
        height.
    time_taken : float
        The time it will take for the ball to complete the specified number of
        bounces.

    Returns
    -------
    None.

    '''
    if bounce_count == 0:
        total_datapoints = 1000000
    else:
        # find smallest number greater than 1000000 divisible by the number of
        # bounces, divide by the number of bounces and multiply by the number
        # which is larger than the number of bounces by two. This accounts
        # for the initial drop and the last bounce lower than minimum height.
        total_datapoints = int(
            (1000000 + bounce_count - (1000000 + bounce_count) % bounce_count)
            / bounce_count
            * (bounce_count + 2)
        )
    cycle_time = np.sqrt(2 * initial_height / GRAVITATIONAL_CONSTANT)
    total_time = cycle_time
    cycle_abscissas = np.linspace(
        0, cycle_time, int(total_datapoints / (bounce_count + 2))
    )
    ordinates = (
        initial_height - GRAVITATIONAL_CONSTANT * cycle_abscissas ** 2 / 2
    )
    for i in range(1, bounce_count + 2):
        cycle_time = (
            2
            * np.sqrt(2 * bounce_coefficient ** i * initial_height)
            / np.sqrt(GRAVITATIONAL_CONSTANT)
        )
        cycle_abscissas = np.linspace(
            0, cycle_time, int(total_datapoints / (bounce_count + 2))
        )
        cycle_ordinates = (
            np.sqrt(
                2
                * GRAVITATIONAL_CONSTANT
                * initial_height
                * bounce_coefficient ** i
            )
            * cycle_abscissas
            - GRAVITATIONAL_CONSTANT * cycle_abscissas ** 2 / 2
        )
        ordinates = np.append(ordinates, cycle_ordinates)
        total_time += cycle_time
    abscissas = np.linspace(0, total_time, total_datapoints)
    plt.plot(abscissas, ordinates)
    plt.axhline(y=minimum_height, xmin=0, xmax=1, color="g")
    plt.title(
        "Height vs time for initial height "
        + str(initial_height)
        + " m, minimum height "
        + str(minimum_height)
        + " m and bounce coefficient "
        + str(bounce_coefficient)
    )
    plt.xlabel("Time, seconds")
    plt.ylabel("Height, meters")
    plt.show()


print("Hello! We will calculate how many times a ball bounces above the \
specified height and how long this will take.\n")
time.sleep(3)
while True:
    starting_height = get_initial_height()
    smallest_height = get_minimum_height(starting_height)
    bounce_efficiency = get_bounce_coefficient()
    NUMBER_OF_BOUNCES = calculate_bounce_count(
        starting_height, smallest_height, bounce_efficiency
    )
    full_time = calculate_time_taken(
        starting_height, bounce_efficiency, NUMBER_OF_BOUNCES
    )
    print_results(NUMBER_OF_BOUNCES, full_time)
    print("\nEnter 'y' to find out the total distance travelled by the ball or\
'n' to skip.")
    if execute_or_not():
        print_total_distance(starting_height, bounce_efficiency)
    print("\nEnter 'y' to plot the graph of the bounces or 'n' to skip.")
    if execute_or_not():
        bounce_graph(
            starting_height,
            smallest_height,
            bounce_efficiency,
            NUMBER_OF_BOUNCES,
        )
    print(("\nEnter 'y' to make another calculation or 'n' to exit."))
    if not execute_or_not():
        print("\nGoodbye!")
        time.sleep(2)
        break
