'''
This file aims for computing only the model values of 
Kalman filter.
'''

import numpy as np
from noise_adder import gauss_nos_zoh_adder
import config as cfg
import matplotlib.pyplot as plt

DATA_FILE = "Hexa4+_tp02-alt-acc.csv"
Tp = 0.02
noise_presets = {
    "alt_sig": cfg.alt_sig,
    "acc_sig": cfg.acc_sig
}

F = np.array([[ 1, Tp],
              [ 0, 1]])

G = np.array([[ Tp ** 2 / 2],
              [ Tp         ]])

x = np.array([[ 0 ],
              [ 0 ]])

t, h_rel, h_nos, a_rel, a_nos = gauss_nos_zoh_adder(DATA_FILE, noise_presets, Tp)

h_model= []

''' with ZOH implemented in noise_adder.py'''
for step in range(0, len(h_rel)):

    #model calculations
    x = F @ x + G * (a_nos[step])
    h_model.append(x[0][0])
  
plt.plot(h_model, 'b')
plt.plot(h_rel, 'r')
plt.grid()
plt.show()
