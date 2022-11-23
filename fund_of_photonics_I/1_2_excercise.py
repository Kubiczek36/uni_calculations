# %%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

# %% Read data

lam = 1036e-9  # m

z = '5 7.5 10 22.5 25 27.5 30 32.5 50 52.5 55'  # input data in cm
z = np.array(z.split(' ')).astype('float64')/100  # convert to m

# input data in mm
Dx = '1.456 1.306 1.156 0.4726 0.3689 0.2956 0.3086 0.3968 1.444 1.635 1.818'
Dx = np.array(Dx.split(' ')).astype('float64')/1e3
Rx = Dx/2

# waist_x = z[np.argmin(Dx)]

# input data in mm
Dy = '1.306 1.192 1.072 0.5083 0.4196 0.3491 0.3289 0.3766 1.211 1.363 1.520'
Dy = np.array(Dy.split(' ')).astype('float64')/1e3
Ry = Dy/2
# waist_y = z[np.argmin(Dy)]


# %%

def w(z, M2, w0, z0):
    fraction = (M2 * lam * (z - z0))/(np.pi * w0**2)
    return w0*np.sqrt(1 + fraction**2)

# %% 

paramsx = curve_fit(w, z, Rx, bounds=([0, 0, 0], [10, 400e-6, 1]))[0]
paramsy = curve_fit(w, z, Ry, bounds=([0, 0, 0], [10, 400e-6, 1]))[0]


# %% plot data
zplot = np.linspace(z.min()*0.9, z.max()*1.1)

plt.figure(dpi=333)
plt.plot(z, 1e3*Rx, '.', label='$R_x$ (mm)')
plt.plot(zplot, 1e3*w(zplot, paramsx[0], paramsx[1], paramsx[2]), '--', color='tab:blue',
         label='$M= {:.2f}$, $w_0 = {:.3}$ mm, $z_0 = {:.2f}$ m '.format(np.sqrt(paramsx[0]), 1e3*paramsx[1], paramsx[2]), linewidth=0.6)
plt.plot(z, 1e3*Ry, '.', label='$D_y$ (mm)')
plt.plot(zplot, 1e3*w(zplot, paramsy[0], paramsy[1], paramsy[2]), '--', color='tab:orange',
         label='$M= {:.2f}$, $w_0 = {:.3}$ mm, $z_0 = {:.2f}$ m '.format(np.sqrt(paramsy[0]), 1e3*paramsy[1], paramsy[2]), linewidth=0.6)
plt.legend()
plt.grid()
plt.xlabel('z (m)')
plt.savefig('m_squared.png')
# %%
