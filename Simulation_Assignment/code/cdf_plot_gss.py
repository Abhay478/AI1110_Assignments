import numpy as np
import matplotlib.pyplot as plt
import mpmath as m
import scipy


def expit(x):
    if x < 0:
        return 0.0
    return 1 - m.sqrt(m.exp(-x))

vec = scipy.vectorize(expit)
x = np.linspace(-6,6,30)#points on the x axis
t = np.linspace(-6, 6, 300)
res = vec(t)
simlen = int(1e6)
err = [] #declaring probability list
randvar = np.loadtxt('../data/gss.dat',dtype='double')

for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

plt.title("CDF of Exponential (as gaussian-squared-sum).")


plt.plot(x.T,err, "o", label="simulation")#plotting the CDF
plt.plot(t, res, label="analysis")
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')

plt.legend()
plt.savefig('../images/gss.pdf')
plt.savefig('../images/gss.png')


