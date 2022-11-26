# -*- coding: utf-8 -*-
"""
Gaussian Fit to each resonance curve to find full width half max

Created on Tue Feb 15 17:11:30 2022

@author: Daniel Smith
"""

import numpy as np
import matplotlib.pyplot as plt

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

def gaussian(x, std_dev, mean, c):
    # gaussian
    return np.exp(-(x - mean)**2 / (2 * std_dev**2)) / (2 * np.pi * std_dev**2) + c



data = np.genfromtxt('4.1_0kHz_resonance_curve_data.csv', delimiter=',', skip_header=1)

x = data[:, 2]
y = data[:, 0]
e = data[:, 1]

fit = np.polyfit(x, y, 7)
x_2 = np.linspace(np.min(x), np.max(x))
y_2 = np.polyval(fit, x_2)


max_index = np.argmax(y_2)
half_1 = y_2[:max_index]
half_2 = y_2[max_index:]

half_maximum = np.max(y_2) / 2

first_index = np.where(half_1 == find_nearest(half_1, half_maximum))[0][0]
second_index = len(half_1 ) + np.where(half_2 == find_nearest(half_2, half_maximum))[0][0]


fig = plt.figure()
ax_1 = fig.add_subplot(111)
ax_1.set_xlabel('Capacitance, F')
ax_1.set_ylabel('Voltage, V')
ax_1.errorbar(x,y,e,fmt='.k')
ax_1.plot(x_2, y_2, label='fit function')
plt.axvline(x_2[first_index], color='red', dashes=[2,2])
plt.axvline(x_2[second_index], color='red', dashes=[2,2])
plt.axhline(half_maximum, color='red', dashes=[2,2])
plt.legend()
plt.savefig('4.1_resonance_fit_130kHz.png', dpi=600)
plt.show()


Q = x_2[max_index] / (x_2[second_index] - x_2[first_index])



print('First capacitance at half max:', x_2[first_index])
print('Second capacitance at half max:', x_2[second_index])
print('Half max voltage:', half_maximum)
print('Q-factor:', Q)

#find chi squre
chi_list = np.array([])
for i in range(len(x)):
    temp = (-y[i] + (np.polyval(fit, x[i]))) / y[i]**2
    chi_list = np.append(chi_list, temp)

chi_square = np.sum(chi_list)
red_chi_square = chi_square / (len(x) - 7)  #7 fit params
print('Red Chi square:', red_chi_square)


#aquire vals for exp 4.3 plot
diff_in_half_max_capacitances = x_2[second_index] - x_2[first_index]
diff_err = np.sqrt(2 * (0.661420 * (10**-12))**2)
alpha = (np.max(y_2 / half_maximum))**2

print(diff_in_half_max_capacitances, '+/-', diff_err)
print(alpha)