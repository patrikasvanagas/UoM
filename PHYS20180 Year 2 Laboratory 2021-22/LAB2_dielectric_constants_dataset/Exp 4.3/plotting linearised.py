# -*- coding: utf-8 -*-
"""
plotting the linearinsed resonance curve from exp 4.2

Created on Tue Feb 22 18:59:36 2022

@author: Daniel Smith
"""

import numpy as np 
import matplotlib.pyplot as plt 

data = np.genfromtxt('values_air_100kHz.csv', delimiter=',', skip_header=1)

alpha = data[:, 0]
capacitance_diff = data[:, 1]
err = data[:, 2]


#remove points which have the same value of capacitance difference
if capacitance_diff[-1] == capacitance_diff[-2]:
    capacitance_diff = np.delete(capacitance_diff, -1)
    alpha = np.delete(alpha, -1)
    err = np.delete(err, -1)


fit, cov = np.polyfit(np.sqrt(alpha - 1), capacitance_diff, 1, w=err, cov=True)
x = np.linspace(0, 2.5, 100)
y_2 = np.polyval(fit, x)

print('Gradient = {0} +/- {2}, y-intercept = {1} +/- {3}'.format(fit[0], fit[1], np.sqrt(cov[0][0]), np.sqrt(cov[1][1])))


fig = plt.figure()
ax_1 = fig.add_subplot(111)
ax_1.set_xlabel(r'$\sqrt{\alpha-1}$')
ax_1.set_ylabel(r'$C_a - C_b$')


plt.errorbar(np.sqrt(alpha - 1), capacitance_diff, yerr=err, fmt='rx')
plt.plot(x, y_2)
plt.savefig('Linearised_plot_100kHz_air.png', dpi=600)
plt.show()