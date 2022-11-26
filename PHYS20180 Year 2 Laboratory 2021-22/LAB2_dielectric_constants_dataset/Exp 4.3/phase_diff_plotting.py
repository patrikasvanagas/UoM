# -*- coding: utf-8 -*-
"""
exp 4.3 plotting phases

Created on Tue Feb 22 12:19:07 2022

@author: danie
"""
import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('phase_diff_data.csv', delimiter=',', skip_header=1)

x = data[:, 0]
y = data[:, 1]
y_err = data[:, 2]

fig = plt.figure()
ax_1 = fig.add_subplot(111)

ax_1.set_xlabel('Capacitance, F')
ax_1.set_ylabel('Phase Diff, Deg')

ax_1.errorbar(x, y, yerr=y_err)
ax_1.axvline(x=854.5676 * 10**-12, dashes=[2,2], color='r')