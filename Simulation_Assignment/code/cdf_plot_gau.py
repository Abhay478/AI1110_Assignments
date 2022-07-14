import numpy as np
import matplotlib.pyplot as plt
import mpmath as mp
import scipy

x = np.linspace(-6,6,30)#points on the x axis
t = np.linspace(-6, 6, 300)

def with_q(x):
    return 1 - 0.5 * mp.erfc(x/mp.sqrt(2))

vec = scipy.vectorize(with_q)
res = vec(t)
simlen = int(1e6) #number of samples
err = [] #declaring probability list

randvar = np.loadtxt('../data/gau.dat',dtype='double')

for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

plt.title("CDF of Gaussian.")
plt.plot(x.T,err, "o", label="simulation")#plotting the CDF
plt.plot(t, res, label="analysis")
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')

#if using termux
plt.legend()
plt.savefig('../images/gau.pdf')
plt.savefig('../images/gau.png')

# plt.show()
