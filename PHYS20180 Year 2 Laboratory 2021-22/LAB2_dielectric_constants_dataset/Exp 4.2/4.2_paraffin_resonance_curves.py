# -*- coding: utf-8 -*-
"""
Resonance curve for the load capacitor with a paraffin dielectric
Exp 4.2

Created on Tue Feb 15 10:43:34 2022

@author: Daniel Smith
"""

import numpy as np
import matplotlib.pyplot as plt

data_70kHz = np.genfromtxt('70kHz_data_paraffin.csv', delimiter=',', skip_header=1)
data_90kHz = np.genfromtxt('90kHz_data_paraffin.csv', delimiter=',', skip_header=1)
data_100kHz = np.genfromtxt('100kHz_data_paraffin.csv', delimiter=',', skip_header=1)

fig = plt.figure()
ax_1 = fig.add_subplot(221)

#ax_1.set_title('70kHz Paraffin curve')
# ax_1.set_xlabel('Capacitance, pF')
# ax_1.set_ylabel('Voltage, mV')
ax_1.errorbar(data_70kHz[:, 2], data_70kHz[:, 0], yerr=data_70kHz[:, 1], fmt='x', label='70kHz')
plt.legend()

ax_2 = fig.add_subplot(222)

#ax_2.set_title('90kHz Paraffin curve')
# ax_2.set_xlabel('Capacitance, pF')
# ax_2.set_ylabel('Voltage, mV')
ax_2.errorbar(data_90kHz[:, 2], data_90kHz[:, 0], yerr=data_90kHz[:, 1], fmt='x', label='90kHz')
plt.legend()

ax_3 = fig.add_subplot(223)

#ax_3.set_title('100kHz Paraffin curve')
ax_3.set_xlabel('Capacitance, pF')
ax_3.set_ylabel('Voltage, mV')
ax_3.errorbar(data_100kHz[:, 2], data_100kHz[:, 0], yerr=data_100kHz[:, 1], fmt='x', label='100kHz')
plt.legend()

plt.savefig('Resonance Curves paraffin.png', dpi=600)
plt.show()

