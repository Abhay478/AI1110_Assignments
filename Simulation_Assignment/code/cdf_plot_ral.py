import numpy as np
import matplotlib.pyplot as plt
import mpmath as mp
import scipy

x = np.linspace(-6,6,30)#points on the x axis
t = np.linspace(-6, 6, 300)

def z(sample):
    return (1 - mp.exp(-(sample ** 2) / 2)) * (sample + abs(sample))/(2 * sample)

vec_z = scipy.vectorize(z)
res = vec_z(t)
simlen = int(1e6) #number of samples
err = [] #declaring probability list

randvar = np.loadtxt('../data/ral.dat',dtype='double')

for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

plt.title("CDF of Raleigh.")
plt.plot(x.T,err, "o", label="simulation")#plotting the CDF
plt.plot(t, res, label="analysis")
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')

#if using termux
plt.legend()
plt.savefig('../images/ral.pdf')
plt.savefig('../images/ral.png')

# plt.show()
