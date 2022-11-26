# -*- coding: utf-8 -*-
"""
exp 4.1 create induvidual resonance curves for each frequency used

Created on Fri Feb 11 14:18:37 2022

@author: Daniel Smith
"""
import numpy as np 
import matplotlib.pyplot as plt 

data_70_kHz = np.genfromtxt('4.1_70kHz_resonance_curve_data.csv', delimiter=',', skip_header=1)
data_80_kHz = np.genfromtxt('4.1_80kHz_resonance_curve_data.csv', delimiter=',', skip_header=1)
data_90_kHz = np.genfromtxt('4.1_90kHz_resonance_curve_data.csv', delimiter=',', skip_header=1)
data_100_kHz = np.genfromtxt('4.1_100kHz_resonance_curve_data.csv', delimiter=',', skip_header=1)
data_110_kHz = np.genfromtxt('4.1_110kHz_resonance_curve_data.csv', delimiter=',', skip_header=1)
data_120_kHz = np.genfromtxt('4.1_120kHz_resonance_curve_data.csv', delimiter=',', skip_header=1)
data_130_kHz = np.genfromtxt('4.1_130kHz_resonance_curve_data.csv', delimiter=',', skip_header=1)

#70 kHz
voltage_70 = data_70_kHz[:, 0]
voltage_70_err = data_70_kHz[:, 1]
capacitance_70 = data_70_kHz[:, 2]
capacitance_70_err = data_70_kHz[:, 3]

#80 kHz
voltage_80 = data_80_kHz[:, 0]
voltage_80_err = data_80_kHz[:, 1]
capacitance_80 = data_80_kHz[:, 2]
capacitance_80_err = data_80_kHz[:, 3]

#90kHz
voltage_90 = data_90_kHz[:, 0]
voltage_90_err = data_90_kHz[:, 1]
capacitance_90 = data_90_kHz[:, 2]
capacitance_90_err = data_90_kHz[:, 3]

#100kHz
voltage_100 = data_100_kHz[:, 0]
voltage_100_err = data_100_kHz[:, 1]
capacitance_100 = data_100_kHz[:, 2]
capacitance_100_err = data_100_kHz[:, 3]

#110kHz
voltage_110 = data_110_kHz[:, 0]
voltage_110_err = data_110_kHz[:, 1]
capacitance_110 = data_110_kHz[:, 2]
capacitance_110_err = data_110_kHz[:, 3]

#120kHz
voltage_120 = data_120_kHz[:, 0]
voltage_120_err = data_120_kHz[:, 1]
capacitance_120 = data_120_kHz[:, 2]
capacitance_120_err = data_120_kHz[:, 3]

#130kHz
voltage_130 = data_130_kHz[:, 0]
voltage_130_err = data_130_kHz[:, 1]
capacitance_130 = data_130_kHz[:, 2]
capacitance_130_err = data_130_kHz[:, 3]

fig = plt.figure()
ax_70 = fig.add_subplot(221)
# ax_70.set_xlabel('Capcitance, pF')
# ax_70.set_ylabel('Voltage, mV')
#ax_70.set_title('70 kHz')
ax_70.errorbar(capacitance_70, voltage_70, label='70kHz', fmt='x', color='black')
plt.legend(fontsize='6')

ax_80 = fig.add_subplot(222)
# ax_80.set_xlabel('Capcitance, pF')
# ax_80.set_ylabel('Voltage, mV')
#ax_80.set_title('80 kHz')
ax_80.errorbar(capacitance_80, voltage_80, label='80kHz', fmt='x', color='black')
plt.legend(fontsize='6')

ax_90 = fig.add_subplot(223)
ax_90.set_xlabel('Capcitance, pF')
ax_90.set_ylabel('Voltage, mV')
#ax_90.set_title('90 kHz')
ax_90.errorbar(capacitance_90, voltage_90, label='90kHz', fmt='x', color='black')
plt.legend(fontsize='6')

ax_100 = fig.add_subplot(224)
# ax_100.set_xlabel('Capcitance, pF')
# ax_100.set_ylabel('Voltage, mV')
#ax_100.set_title('80 kHz')
ax_100.errorbar(capacitance_100, voltage_100, label='100kHz', fmt='x', color='black')
plt.legend(fontsize='6')

plt.savefig('4.1_resonance_curves_70-100.png', dpi = 600)
plt.show()



fig_2 = plt.figure()

ax_110 = fig_2.add_subplot(221)
ax_110.errorbar(capacitance_110, voltage_110, label='110kHz', fmt='x', color='black')
plt.legend(fontsize='6')

ax_120 = fig_2.add_subplot(222)
ax_120.errorbar(capacitance_120, voltage_120, label='120kHz', fmt='x', color='black')
plt.legend(fontsize='6')

ax_130 = fig_2.add_subplot(223)
ax_130.set_xlabel('Capcitance, pF')
ax_130.set_ylabel('Voltage, mV')
ax_130.errorbar(capacitance_130, voltage_130, label='130kHz', fmt='x', color='black')
plt.legend(fontsize='6')


plt.savefig('4.1_resonance_curves_110-130.png', dpi = 600)
plt.show()