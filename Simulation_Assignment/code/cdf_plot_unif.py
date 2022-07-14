#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import scipy

#if using termux
#import subprocess
#import shlex
#end if
def z(x):
    if(x < 0):
        return 0.0
    elif(x > 1):
        return 1.0
    else:
        return float(x)

vec_z = scipy.vectorize(z)

x = np.linspace(-4,4,30)#points on the x axis

t = np.linspace(-4, 4, 300)

res = vec_z(t)
simlen = int(1e6) #number of samples
err = [] #declaring probability list
#randvar = np.random.normal(0,1,simlen)
randvar = np.loadtxt('../data/uni.dat',dtype='double')
#randvar = np.loadtxt('gau.dat',dtype='double')
for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

plt.title("CDF of Uniform")
plt.plot(x.T, err, "o", label="simulation")#plotting the CDF
plt.plot(t, vec_z(t), label="analysis")
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')

#if using termux
plt.legend()
plt.savefig('../images/unif.pdf')
plt.savefig('../images/unif.png')

#plt.show()
