# -*- coding: utf-8 -*-
"""
Prove that velocity is constant on the detector rail

Created on Tue Mar  1 14:02:36 2022

@author: daniel
"""

import numpy as np
import matplotlib.pyplot as plt


def chi_square(y_val, y_fit, err):
    return np.sum(( (y_val - y_fit) / err )**2)


data = np.genfromtxt('4.3_2_setting_data.csv', delimiter=',', skip_header=1)

time = data[:, 0]
distance = data[:, 1]
y_err = data[:, 2]

fit_vals, cov = np.polyfit(time, distance, 1, cov=True)
y_2 = np.polyval(fit_vals, time)

fig = plt.figure()
ax_1 = fig.add_subplot(111)

ax_1.set_xlabel('time, s')
ax_1.set_ylabel('distance, cm')
ax_1.set_title('Speed setting of 2')


plt.errorbar(time, distance, yerr=y_err, fmt='x', label='data')
plt.plot(time, y_2, label='fit')

plt.legend()
plt.savefig('Check Linearity 4.3 2 setting.png', dpi=600)
plt.show()

chi_square_val = chi_square(distance, y_2, y_err)
red_chi_val = chi_square_val / (len(time) - 2)

print('Reduced Chi square: {}'.format(red_chi_val))
