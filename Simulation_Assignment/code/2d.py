
import numpy as np
import matplotlib.pyplot as plt
import mpmath as m
import scipy
A = 10

gau = np.loadtxt('../data/gau.dat')
n_1 = gau[:500000]
n_2 = gau[500000:]


plt.grid()

plt.title('Combined Scatter plot')
plt.scatter([A] * 500000  + n_1, n_2, label='s0')
plt.scatter(n_1, [A] * 500000 + n_2, label='s1')
lin = np.linspace(-20, 20, 1000)
plt.xlabel('x')
plt.ylabel('y')

plt.plot(lin, lin, label='y = x')

plt.legend()
plt.savefig('../images/2d.png')
plt.savefig('../images/2d.pdf')

plt.show()