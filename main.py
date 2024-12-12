import numpy as np
import matplotlib.pyplot as plt

import config as cfg
from KalmanFilter_class import KalmanFilter
from noise_adder import gaussian_noise_adder, gauss_nos_zoh_adder

'''
The Kalman Filter won't work with gaussian_noise_adder
due to the sampling time of simulated data, which is not constant.

In gauss_nos_zoh_adder, the data is interpolated to have a constant sampling time.
'''

# CONFIG
Tp = 0.02
noise_presets = {
    "alt_sig": cfg.alt_sig,
    "acc_sig": cfg.acc_sig
}

t, h_rel, h_nos, a_rel, a_nos = gauss_nos_zoh_adder(cfg.DATA_FILE, noise_presets, Tp) # gaussian_noise_adder(cfg.DATA_FILE, noise_presets)

# init values
F = np.array([[ 1, Tp],
              [ 0, 1]])

G = np.array([[ Tp ** 2 / 2],
              [ Tp         ]])

H = np.array([ 1, 0])

Q = np.array([[ Tp**4/4, Tp**3/2 ],
              [ Tp**3/2, Tp**2   ]]) * 1

R_init = 2000

P_init = np.array([[ 500, 0   ],
                   [ 0,   500 ]])

x_init = np.array([[ 0 ],
                   [ 0 ]])

kalman = KalmanFilter(F, G, H, Q, R_init, P_init, x_init)

# create data array
kalman_alt = []

# first iteration
kalman.predict( 0 )

# iteration loop
for step in range(0, len(h_nos)):
    val = kalman.update( h_nos[step] )
    kalman_alt.append( val )
    kalman.predict( a_nos[step])

# plt.subplot(2, 1, 1)
plt.plot(t, h_nos, '.g', label="altitude measurements")     #noised altitiude
plt.plot(t, kalman_alt, 'b', label="estimated altitude")  #kalman altitiude
plt.plot(t, h_rel, 'r', label="real height (ZOH)")      #measured altitiude

plt.xlabel("Time [s]")
plt.ylabel("Altitude [m]")
plt.legend()
plt.grid()

plt.show()
