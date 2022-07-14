import numpy as np
import matplotlib.pyplot as plt
import mpmath as mp
import scipy

# def triang(x):
#     if x < 0 or x > 2:
#         return 0
#     return 1 - abs(x - 1)

def triang(x):
    if x < 0:
        return 0.0
    if x > 2:
        return 1.0
    if x < 1:
        return (x ** 2)/2
    if x >= 1:
        return 2*x - (x ** 2)/2 - 1

x = np.linspace(-6,6,30)#points on the x axis
t = np.linspace(-6, 6, 300)
vec = scipy.vectorize(triang)
res = vec(t)
simlen = int(1e6)
err = [] #declaring probability list
randvar = np.loadtxt('../data/tri.dat',dtype='double')

for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

plt.title("CDF of Triangular.")


plt.plot(x.T,err, "o", label="simulation")#plotting the CDF
plt.plot(t, res, label="analysis")
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')

plt.legend()
plt.savefig('../images/tri.pdf')
plt.savefig('../images/tri.png')


