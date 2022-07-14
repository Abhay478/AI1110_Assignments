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

randvar = np.loadtxt('ral.dat',dtype='double')

for i in range(0,maxrange):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

	
for i in range(0,maxrange-1):
	test = (err[i+1]-err[i])/(x[i+1]-x[i])
	pdf.append(test) #storing the pdf values in a list


def ral_pdf(t):
    if t < 0:
        return 0.0
    return  t * np.exp(-(t ** 2)/2)
	
vec_ral_pdf = scipy.vectorize(ral_pdf)
# print(x)
out = np.array(vec_ral_pdf(x))

plt.plot(x[:(maxrange - 1)].T,pdf,'o', label="Simulated")
plt.plot(x,out, label="analysis")#plotting the PDF
plt.grid() #creating the grid
plt.title("PDF of Raleigh")
plt.xlabel('$x_i$')
plt.ylabel('$p_X(x_i)$')
plt.legend()

#if using termux
plt.savefig('../images/pdf_ral.png')
plt.savefig('../images/pdf_ral.pdf')

plt.show()
