# -*- coding: utf-8 -*-
"""
Exp 4.1 - Dielectric Constants

Plot resonance curves for circuit without load capacitor

Created on Thu Feb 10 22:15:56 2022

@author: Daniel Smith
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

data = np.genfromtxt('4.1_determine_L_data.csv', delimiter=',', skip_header=1)
print(data)

def function(x, coef_1):
    return (1/coef_1) * x

def fit(data):

    result = curve_fit(function, data[:, 0], data[:, 2], sigma=data[:, 3])

    fit_vals = result[0]
    cov = result[1]

    return fit_vals, cov


x = data[:, 0]
y = data[:, 2]
linspace = np.linspace(1E9, 7E9, 100)

L, cov = fit(data)
print('Value of L: ', L)
print('With error: ', cov)

fit_func = (1/L) * linspace

fig = plt.figure()
ax_1 = fig.add_subplot(111)

ax_1.set_xlabel('1/Capacitance')
ax_1.set_ylabel('frequency')

ax_1.plot(x, y)
ax_1.plot(linspace, fit_func)
plt.show()