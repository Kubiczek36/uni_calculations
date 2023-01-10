# %%
import matplotlib.pyplot as plt
import numpy as np
from scipy import constants

def ev2Joule(val):
    return val/constants.e

def ener2temp(val):
    return val/(constants.Boltzmann)
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
1/(np.exp(3) + 1)
# %%

T = 300
E = np.linspace(-3e3, 3e3,500) * constants.Boltzmann

plt.plot(E, 1/(np.exp(E/(constants.Boltzmann * T)) +1))
plt.plot(E, 1/(np.exp(E/(constants.Boltzmann * 0.01)) +1))
# %%
ev2Joule(0.3)/99*constants.Boltzmann
# %%

f = 15
z = 33
zc = f*z/(z - f)

z3_nahore = f * zc / (1 - 2*f/z)
z3_dole = zc / (1 - 2*f/z) - f
z3 = z3_nahore/z3_dole
print(f'z_3 = {z3}')

z2_nahore = f * zc / (1 + 2*f/z)
z2_dole = zc / (1 + 2*f/z) - f
z2 = z2_nahore/z2_dole
print(f'z_2 = {z2}')

print(f'Hloubka ostrosti je {z2 - z3}')


# %% 9.1

field_gradient = 1.83e9 #* constants.mu_0
d_1 = 3e-2
d_2 = 25e-2
E_k = 3e-20

force = constants.physical_constants['Bohr magneton'][0]*field_gradient

print(f'Magnetic force is {force}')

mass = 107.8682*constants.m_u

acceleration = force/mass

print(f'a_z = {acceleration}')

v_x = np.sqrt(2*E_k/mass)
print(f'v_x = {v_x}')

t_1 = d_1/v_x

v_z = acceleration*t_1
print(f'v_z = {v_z}')

alpha = np.rad2deg(np.arctan(v_x/v_z))
print(f'Tha atom is leaving the angle {alpha}')
# %% 9.2 

I = 10 # A
R = 5e-2
z = 10e-2

grad_B = -1.5 * constants.mu_0 * I * R**2 * z / (z**2 + R**2)**2.5
print(f'grad B_z = {grad_B}')

force = constants.physical_constants['Bohr magneton'][0]*field_gradient
print(f'Magnetic force is {force}')



# %% 9.3

U_H = 8.8e-3
U = 230 # both in V

rho_Ge = 1/80 
B = 0.1 # T

L = 0.1 #m
l = 6e-3 #m

R_H = U_H * rho_Ge * L / (U*l*B)

print(f'the Hall const is {R_H}')

conc = - R_H * constants.e
print(f'concentration is {conc}')
# %% 9.4

P_1 = 0.4
P_2 = 0.3

TMR = 2*P_1*P_2/ (1-P_1*P_2)
print(f'magnetoresistance is {TMR}')

R_ap = 1e3

R_p = R_ap/(1+TMR)

print(f'TMR is {TMR}')

# %%
