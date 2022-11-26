# -*- coding: utf-8 -*-
"""
This is better than the gradient method as L seems to increase with frequency

Different method of calculating L, by considering each frequency induvidually
and just soliving for L

Created on Tue Feb 15 12:06:41 2022

@author: Daniel Smith
"""

import numpy as np

peak_C_err = 0.661420 * (10**-12)

def get_peak_vals(data):
    peak_V = np.max(data[:, 0])
    index = np.where(data[:, 0] == peak_V)
    peak_C = data[index, 2]

    return peak_C[0][0]


#70kHz case
data_70kHz = np.genfromtxt('4.1_70kHz_resonance_curve_data.csv', delimiter=',', skip_header=1)
ang_freq_70kHz = 2*np.pi*70000
ang_freq_70kHz_err = 0.0001 * ang_freq_70kHz

peak_C_70 = get_peak_vals(data_70kHz)

L_70 = 1/((ang_freq_70kHz**2)*(peak_C_70))
L_70_err = L_70 * np.sqrt((ang_freq_70kHz_err / ang_freq_70kHz)**2 + (peak_C_err / peak_C_70)**2)
print('L at 70kHz:', L_70)
print('With error:', L_70_err)


#80kHz case
data_80kHz = np.genfromtxt('4.1_80kHz_resonance_curve_data.csv', delimiter=',', skip_header=1)
ang_freq_80kHz = 2*np.pi*80000
ang_freq_80kHz_err = 0.0001 * ang_freq_80kHz

peak_C_80 = get_peak_vals(data_80kHz)

L_80 = 1/((ang_freq_80kHz**2)*(peak_C_80))
L_80_err = L_80 * np.sqrt((ang_freq_80kHz_err / ang_freq_80kHz)**2 + (peak_C_err / peak_C_80)**2)
print('L at 80kHz:', L_80)
print('With error:', L_80_err)


#90kHz case
data_90kHz = np.genfromtxt('4.1_90kHz_resonance_curve_data.csv', delimiter=',', skip_header=1)
ang_freq_90kHz = 2*np.pi*90000
ang_freq_90kHz_err = 0.0001 * ang_freq_90kHz

peak_C_90 = get_peak_vals(data_90kHz)

L_90 = 1/((ang_freq_90kHz**2)*(peak_C_90))
L_90_err = L_90 * np.sqrt((ang_freq_90kHz_err / ang_freq_90kHz)**2 + (peak_C_err / peak_C_90)**2)
print('L at 90kHz:', L_90)
print('With error:', L_90_err)


#100kHz case
data_100kHz = np.genfromtxt('4.1_100kHz_resonance_curve_data.csv', delimiter=',', skip_header=1)
ang_freq_100kHz = 2*np.pi*100000
ang_freq_100kHz_err = 0.0001 * ang_freq_100kHz

peak_C_100 = get_peak_vals(data_100kHz)

L_100 = 1/((ang_freq_100kHz**2)*(peak_C_100))
L_100_err = L_100 * np.sqrt((ang_freq_100kHz_err / ang_freq_100kHz)**2 + (peak_C_err / peak_C_100)**2)
print('L at 100kHz:', L_100)
print('With error:', L_100_err)


#110kHz case
data_110kHz = np.genfromtxt('4.1_110kHz_resonance_curve_data.csv', delimiter=',', skip_header=1)
ang_freq_110kHz = 2*np.pi*110000
ang_freq_110kHz_err = 0.0001 * ang_freq_110kHz

peak_C_110 = get_peak_vals(data_110kHz)

L_110 = 1/((ang_freq_110kHz**2)*(peak_C_110))
L_110_err = L_110 * np.sqrt((ang_freq_110kHz_err / ang_freq_110kHz)**2 + (peak_C_err / peak_C_110)**2)
print('L at 110kHz:', L_110)
print('With error:', L_110_err)


#120kHz case
data_120kHz = np.genfromtxt('4.1_120kHz_resonance_curve_data.csv', delimiter=',', skip_header=1)
ang_freq_120kHz = 2*np.pi*120000
ang_freq_120kHz_err = 0.0001 * ang_freq_120kHz

peak_C_120 = get_peak_vals(data_120kHz)

L_120 = 1/((ang_freq_120kHz**2)*(peak_C_120))
L_120_err = L_120 * np.sqrt((ang_freq_120kHz_err / ang_freq_120kHz)**2 + (peak_C_err / peak_C_120)**2)
print('L at 120kHz:', L_120)
print('With error:', L_120_err)


#130kHz case
data_130kHz = np.genfromtxt('4.1_130kHz_resonance_curve_data.csv', delimiter=',', skip_header=1)
ang_freq_130kHz = 2*np.pi*130000
ang_freq_130kHz_err = 0.0001 * ang_freq_130kHz

peak_C_130 = get_peak_vals(data_130kHz)

L_130 = 1/((ang_freq_130kHz**2)*(peak_C_130))
L_130_err = L_130 * np.sqrt((ang_freq_130kHz_err / ang_freq_130kHz)**2 + (peak_C_err / peak_C_130)**2)
print('L at 130kHz:', L_130)
print('With error:', L_130_err)