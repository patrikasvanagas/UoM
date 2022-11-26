# -*- coding: utf-8 -*-
"""
4.3 collating data for main plot

use at least 7 values of alpha, i.e 8 differnet V_2 values 
try for V_2 is 0.9 v1 (alpha 1)
        V_2 is a 0.8 v1 (alpha 2)
        V_2 is a 0.7 v1 (alpha 3)
        V_2 is a 0.6 v1 (alpha 4)
        V_2 is a 0.5 v1 (alpha 5)
        V_2 is a 0.4 v1 (alpha 6)
        V_2 is a 0.3 v1 (alpha 7)

Created on Tue Feb 22 11:49:32 2022

@author: Daniel Smith 
"""
import numpy as np
import matplotlib.pyplot as plt


def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]


data = np.genfromtxt('100kHz_data_paraffin.csv', delimiter=',', skip_header=1)

voltage = data[:, 0]
voltage_err = data[:, 1]
capacitance = data[:, 2]
capacitance_err = 0.661420 * (10**-12)

fit = np.polyfit(capacitance, voltage, 7)

x = np.linspace(np.min(capacitance), np.max(capacitance), 1000)
y_2 = np.polyval(fit, x)


max_index = np.argmax(y_2)
half_1 = y_2[:max_index]
half_2 = y_2[max_index:]

print(np.max(y_2))
#for alpha 1
alpha_1 = np.max(y_2) * 0.9

first_index_1 = np.where(half_1 == find_nearest(half_1, alpha_1))[0][0]
second_index_1 = len(half_1 ) + np.where(half_2 == find_nearest(half_2, alpha_1))[0][0]

print('For 0.9 max difference in C vals is: {0:1.8e}'.format(x[second_index_1] - x[first_index_1]))



#for alpha 2
alpha_2 = np.max(y_2) * 0.8

first_index_2 = np.where(half_1 == find_nearest(half_1, alpha_2))[0][0]
second_index_2 = len(half_1 ) + np.where(half_2 == find_nearest(half_2, alpha_2))[0][0]

print('For 0.8 max difference in C vals is: {0:1.8e}'.format( x[second_index_2] - x[first_index_2]))



#for alpha 3 
alpha_3 = np.max(y_2) * 0.7

first_index_3 = np.where(half_1 == find_nearest(half_1, alpha_3))[0][0]
second_index_3 = len(half_1 ) + np.where(half_2 == find_nearest(half_2, alpha_3))[0][0]

print('For 0.7 max difference in C vals is: {0:1.8e}'.format( x[second_index_3] - x[first_index_3]))



#for alpha 4 
alpha_4 = np.max(y_2) * 0.5

first_index_4 = np.where(half_1 == find_nearest(half_1, alpha_4))[0][0]
second_index_4 = len(half_1 ) + np.where(half_2 == find_nearest(half_2, alpha_4))[0][0]

print('For 0.5 max difference in C vals is: {0:1.8e}'.format( x[second_index_4] - x[first_index_4]))



#for alpha 5 
alpha_5 = np.max(y_2) * 0.4

first_index_5 = np.where(half_1 == find_nearest(half_1, alpha_5))[0][0]
second_index_5 = len(half_1 ) + np.where(half_2 == find_nearest(half_2, alpha_5))[0][0]

print('For 0.4 max difference in C vals is: {0:1.8e}'.format( x[second_index_5] - x[first_index_5]))



#for alpha 6 
alpha_6 = np.max(y_2) * 0.3

first_index_6 = np.where(half_1 == find_nearest(half_1, alpha_6))[0][0]
second_index_6 = len(half_1 ) + np.where(half_2 == find_nearest(half_2, alpha_6))[0][0]

print('For 0.3 max difference in C vals is: {0:1.8e}'.format( x[second_index_6] - x[first_index_6]))



#for alpha 7 
alpha_7 = np.max(y_2) * 0.6

first_index_7 = np.where(half_1 == find_nearest(half_1, alpha_7))[0][0]
second_index_7 = len(half_1 ) + np.where(half_2 == find_nearest(half_2, alpha_7))[0][0]

print('For 0.6 max difference in C vals is: {0:1.8e}'.format( x[second_index_7] - x[first_index_7]))


fig = plt.figure()
ax_1 = fig.add_subplot(111)

plt.errorbar(capacitance, voltage, yerr=voltage_err, fmt='rx')
plt.plot(x, y_2)

plt.show()