# %%
import numpy as np
from scipy import constants
# %%
N_v = 100.07

frac1 = constants.hbar/constants.m_e
frac2 = 3*np.pi**2*N_v
e_f = frac1*(frac2)**(2/3)
print(e_f)

v_f = frac1*frac2**(1/3)

# np.sqrt(2*e_f/constants.m_e)
print(v_f)

print(e_f/constants.Boltzmann)
# %%
