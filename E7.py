# %%
import numpy as np
import matplotlib.pyplot as plt

# %%
theta = np.linspace(0, 2*np.pi, 200)
I = (np.cos(2*theta))**2

plt.figure(dpi=250, facecolor='w')
plt.plot(np.rad2deg(theta), I)
plt.xlabel(r'$\theta$ (°)')
plt.ylabel(r'$I/I_0$')
plt.grid()
plt.savefig('e_7_transm.png')
# %%
