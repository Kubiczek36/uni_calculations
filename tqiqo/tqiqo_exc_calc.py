# %%
import numpy as np
from scipy import constants
from scipy.integrate import trapezoid
import matplotlib.pyplot as plt

plt.style.use('bmh')

# %%

def gaussian_state(x, x0, sigma, k):
    '''
    x0 - center of gaussian
    sigma - width of gaussian
    k - momentum of gaussian
    '''
    N = 1/np.sqrt(np.sqrt(np.pi)*sigma)
    return N * np.exp(-(x - x0)**2/(2*sigma**2) - 1j*k*x)

x = np.linspace(-10, 10, 1000)
x0 = 4
sigma = 0.7
k = 6

plt.figure(dpi=300)
plt.plot(x, np.abs(gaussian_state(x, x0, sigma, k))**2, label='$\Psi^2$')
plt.plot(x, np.real(gaussian_state(x, x0, sigma, k)), label='Re($\Psi$)')

plt.legend()
plt.xlabel(r'$x$')

# %%
def gaussian_state_momentum(p, sigma, k, x_0=1):
    '''
    p - momentum
    sigma - width of gaussian
    k - momentum of gaussian
    '''
    N = 1/np.sqrt(np.sqrt(np.pi)*sigma) * np.sqrt(2*np.pi) * sigma
    return N * np.exp((sigma**2 * (k + p) - 1j*x_0)*(k + p))

p = np.linspace(-10, 10, 1000)
sigma = 0.1
k = 3

plt.figure(dpi=300)
plt.plot(p, np.abs(gaussian_state_momentum(p, sigma, k))**2, label='$|\Psi (p)|^2$')
ft_pos = np.fft.fftshift(np.fft.fft(gaussian_state(x, x0, sigma, k)))
N = trapezoid(np.abs(ft_pos)**2, x)
ft_pos = ft_pos/np.sqrt(N)
plt.plot(p, np.abs(ft_pos), label='FFT($\Psi (x)$)')
plt.plot(p, np.real(gaussian_state_momentum(p, sigma, k)), label='Re($\Psi(p)$)')
plt.plot(p, np.imag(gaussian_state_momentum(p, sigma, k)), label='Im($\Psi(p)$)')

plt.legend()
plt.xlabel(r'$p/\hbar$')
plt.title(f'$\sigma = {sigma}, k = {k}$')

norm = trapezoid(np.abs(gaussian_state_momentum(p, sigma, k))**2, p)
print(norm)
# %%
