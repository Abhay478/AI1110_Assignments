#Importing numpy, scipy, mpmath and pyplot

import numpy as np
import mpmath as m
import scipy
import matplotlib.pyplot as plt


maxlim = 10
maxrange=50
x = np.linspace(0,maxlim,maxrange)

simlen = int(1e6) #number of samples
err = [] #declaring probability list
pdf = [] #declaring pdf list
h = 2*maxlim/(maxrange-1)

randvar = np.loadtxt('gss.dat',dtype='double')

for i in range(0,maxrange):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

	
for i in range(0,maxrange-1):
	test = (err[i+1]-err[i])/(x[i+1]-x[i])
	pdf.append(test) #storing the pdf values in a list


def gss_pdf(t):
    if (t < 0):
        return 0.0
    return 0.5 * m.exp(-t/2)
	
# vec_tri_pdf = np.vectorize(tri_pdf)
# print(x)

vec_z = scipy.vectorize(gss_pdf)
out = vec_z(x)

plt.plot(x[:(maxrange - 1)].T,pdf,'o', label="Simulated")
plt.plot(x,out, label="analysis")#plotting the PDF
plt.grid() #creating the grid
plt.title("PDF of Exponential (as gaussian-square-sum)")
plt.xlabel('$x_i$')
plt.ylabel('$p_X(x_i)$')
plt.legend()

#if using termux
plt.savefig('../images/pdf_gss.png')
plt.savefig('../images/pdf_gss.pdf')

# plt.show()
