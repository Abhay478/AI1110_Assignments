import numpy as np
import matplotlib.pyplot as plt
import mpmath as m
import scipy

def with_q(x):
    return 0.5 * m.erfc(5 * x) # 10 * x / 2, because of bel-decibel thing.

vec_q = scipy.vectorize(with_q)
A = np.linspace(0, 10, 100)
theo = vec_q(A)


gau = np.loadtxt('../data/gau.dat')
n_1 = gau[:500000]
n_2 = gau[500000:]

n_sub = n_2 - n_1

def count(a):
    return np.count_nonzero(n_sub > a) / 500000

vec_c = scipy.vectorize(count)

rs = vec_c(A)
plt.plot(A, rs, 'o', label='Simulation')
plt.plot(theo, label='Analysis')
plt.grid()
plt.xlim((0, 10))
plt.legend()
plt.title('Rectangular plot')
plt.xlabel('SNR')
plt.ylabel('Pe')
plt.savefig('../images/2d_estim.png')

plt.clf()
plt.semilogy(A, rs, 'o', label='Simulation')
plt.semilogy(theo, label='Analysis')
plt.grid()
plt.xlim((0, 10))
plt.ylim((10 ** -12, 1))
plt.title('Semilog plot')
plt.legend()
plt.xlabel('SNR')
plt.ylabel('Pe')
plt.savefig('../images/2d_log.png')


# plt.show()
    