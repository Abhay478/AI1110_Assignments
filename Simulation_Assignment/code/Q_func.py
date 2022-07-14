import numpy as np
import scipy
import matplotlib.pyplot as plt

import mpmath as mp

x = np.linspace(0, 10, 30)#points on the x axis
t = np.linspace(0, 10, 300)

def with_q(x):
    return 0.5 * mp.erfc(x/mp.sqrt(2))

vec = scipy.vectorize(with_q)
res1 = vec(t)

sig = np.loadtxt('plm.dat', dtype='double')
noise = np.loadtxt('gau.dat', dtype='double')

def error(a):
    out = a*sig + noise
    n0 = np.count_nonzero(sig > 0)
    n1 = np.count_nonzero(sig < 0)
    e0 = np.count_nonzero((out < 0) & (sig > 0)) 
    e1 = np.count_nonzero((out > 0) & (sig < 0))
    return 0.5*(e0/n0 + e1/n1)

err_vec = scipy.vectorize(error, otypes=['double'])
res2 = err_vec(x)
plt.grid()
plt.title('Rectangular plot of the Q-function')
plt.plot(t, res1, label='Analysis')
plt.plot(x, res2, '.', label='Simulation')
plt.legend()
plt.savefig('../images/Q.png')
plt.savefig('../images/Q.pdf')

plt.clf()

plt.grid()
plt.title('Semilog plot of the Q-function')
plt.semilogy(t, res1, label='Analysis')
plt.semilogy(x, res2, '.', label='Simulation')
plt.legend()
plt.savefig('../images/Q_log.png')
plt.savefig('../images/Q_log.pdf')

