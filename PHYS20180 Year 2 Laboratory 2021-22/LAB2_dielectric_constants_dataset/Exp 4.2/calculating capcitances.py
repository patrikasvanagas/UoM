# -*- coding: utf-8 -*-
"""
Calculating capcitances in parralel in circuit

the value of capacitance quoted in each case with the extra capacitor is the
total capacitance

need to use parallel capcitors to find the capacitance of the load capacitor
itself.

Created on Tue Feb 15 11:20:32 2022

@author: Daniel Smith
"""
import numpy as np

peak_capacitance_70kHz_no_load = 946.6833 * (10**-12)
peak_capacitance_90kHz_no_load = 520.9041 * (10**-12)
peak_capacitance_100kHz_no_load = 380.5766 * (10**-12)
capacitance_err = 0.661420 * (10**-12)  #this is the same as it comes from the fit we made earlier

data_70kHz_air = np.genfromtxt('70kHz_data_air.csv', delimiter=',', skip_header=1)
data_90kHz_air = np.genfromtxt('90kHz_data_air.csv', delimiter=',', skip_header=1)
data_100kHz_air = np.genfromtxt('100kHz_data_air.csv', delimiter=',', skip_header=1)
data_70kHz_paraffin = np.genfromtxt('70kHz_data_paraffin.csv', delimiter=',', skip_header=1)
data_90kHz_paraffin = np.genfromtxt('90kHz_data_paraffin.csv', delimiter=',', skip_header=1)
data_100kHz_paraffin = np.genfromtxt('100kHz_data_paraffin.csv', delimiter=',', skip_header=1)

def get_peak_vals(data):
    peak_V = np.max(data[:, 0])
    index = np.where(data[:, 0] == peak_V)
    peak_C = data[index, 2]

    return peak_C[0][0]


peak_C_70kHz_air = get_peak_vals(data_70kHz_air)
peak_C_90kHz_air = get_peak_vals(data_90kHz_air)
peak_C_100kHz_air = get_peak_vals(data_100kHz_air)
peak_C_70kHz_paraffin = get_peak_vals(data_70kHz_paraffin)
peak_C_90kHz_paraffin = get_peak_vals(data_90kHz_paraffin)
peak_C_100kHz_paraffin = get_peak_vals(data_100kHz_paraffin)

#find value of load capacitor with air dielectric at 70kHz
err = np.sqrt(2 * (capacitance_err**2))

load_capacitor_air_70kHz = (1/peak_C_70kHz_air - 1/peak_capacitance_70kHz_no_load)**-1
print('Load capacitance with air dielectric at 70kHz:',load_capacitor_air_70kHz,'F')
print('With error: +/-', err, 'F')

#find value of load capacitor with air dielectric at 90kHz
load_capacitor_air_90kHz = (1/peak_C_90kHz_air - 1/peak_capacitance_90kHz_no_load)**-1
print('Load capacitance with air dielectric at 90kHz:',load_capacitor_air_90kHz,'F')
print('With error: +/-', err, 'F')

#find value of load capacitor with air dielectric at 100kHz
load_capacitor_air_100kHz = (1/peak_C_100kHz_air - 1/peak_capacitance_100kHz_no_load)**-1
print('Load capacitance with air dielectric at 100kHz:',load_capacitor_air_100kHz,'F')
print('With error: +/-', err, 'F')

#find value of load capacitor with paraffin dielectric at 70kHz
load_capacitor_paraffin_70kHz = (1/peak_C_70kHz_paraffin - 1/peak_capacitance_70kHz_no_load)**-1
print('Load capacitance with paraffin dielectric at 70kHz:',load_capacitor_paraffin_70kHz,'F')
print('With error: +/-', err, 'F')

#find value of load capacitor with paraffin dielectric at 90kHz
load_capacitor_paraffin_90kHz = (1/peak_C_90kHz_paraffin - 1/peak_capacitance_90kHz_no_load)**-1
print('Load capacitance with paraffin dielectric at 90kHz:',load_capacitor_paraffin_90kHz,'F')
print('With error: +/-', err, 'F')

#find value of load capacitor with paraffin dielectric at 100kHz
load_capacitor_paraffin_100kHz = (1/peak_C_100kHz_paraffin - 1/peak_capacitance_100kHz_no_load)**-1
print('Load capacitance with paraffin dielectric at 100kHz:',load_capacitor_paraffin_100kHz,'F')
print('With error: +/-', err, 'F')

#calculating dielectric constant for each frequency, simply the ratio
#of capcitance in air and with dielectric


k_70kHz = load_capacitor_air_70kHz / load_capacitor_paraffin_70kHz
err_k_70 = np.sqrt((err/load_capacitor_paraffin_70kHz)**2 + (err/load_capacitor_air_70kHz)**2) * k_70kHz
k_90kHz = load_capacitor_air_90kHz / load_capacitor_paraffin_90kHz
err_k_90 = np.sqrt((err/load_capacitor_paraffin_90kHz)**2 + (err/load_capacitor_air_90kHz)**2) * k_90kHz
k_100kHz = load_capacitor_air_100kHz / load_capacitor_paraffin_100kHz
err_k_100 = np.sqrt((err/load_capacitor_paraffin_100kHz)**2 + (err/load_capacitor_air_100kHz)**2) * k_100kHz

print('Dielectric constant at 70Khz:', k_70kHz, '+/-', err_k_70)
print('Dielectric constant at 90Khz:', k_90kHz, '+/-', err_k_90)
print('Dielectric constant at 100Khz:', k_100kHz, '+/-', err_k_100)