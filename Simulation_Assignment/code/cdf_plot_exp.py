
import numpy as np
import matplotlib.pyplot as plt
import math as m
import scipy


#if using termux
#import subprocess
#import shlex
#end if    

def expit(x):
    if x < 0:
        return 0.0
    return 1 - m.sqrt(m.exp(-x))
vec = scipy.vectorize(expit)
x = np.linspace(-6,6,30)#points on the x axis
t = np.linspace(-6, 6, 300)

res = vec(t)
simlen = int(1e6) 
err = [] 

randvar = np.loadtxt('../data/exp.dat',dtype='double')

for i in range(30):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

plt.title("CDF of Exponential.")
plt.plot(x.T,err, "o", label="simulation")#plotting the CDF
plt.plot(t.T, res, label="analysis")
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')


plt.legend()
plt.savefig('../images/exp.pdf')
plt.savefig('../images/exp.png')


