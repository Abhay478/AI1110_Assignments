#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import mpmath as mp
import scipy 
import matplotlib.pyplot as plt
import math as m

maxlim = 6
maxrange=30
x = np.linspace(-maxlim,maxlim,30)#points on the x axis
# t = np.linspace(-maxlim,maxlim,300)
# res = np.array((np.exp((t ** 2)/2))/m.sqrt(2 * m.pi))
simlen = int(1e6) #number of samples
err = [] #declaring probability list
pdf = [] #declaring pdf list
h = 2*maxlim/(maxrange-1)

randvar = np.loadtxt('gau.dat',dtype='double')

for i in range(0,maxrange):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

	
for i in range(0,maxrange-1):
	test = (err[i+1]-err[i])/(x[i+1]-x[i])
	pdf.append(test) #storing the pdf values in a list

def gauss_pdf(x):
	return 1/mp.sqrt(2*np.pi)*np.exp(-x**2/2.0)
	
vec_gauss_pdf = scipy.vectorize(gauss_pdf)

plt.plot(x[0:(maxrange-1)].T,pdf,'o', label="Simulated")
plt.plot(x, vec_gauss_pdf(x), label="analysis")#plotting the PDF
plt.grid() #creating the grid
plt.title("Gaussian PDF")
plt.xlabel('$x_i$')
plt.ylabel('$p_X(x_i)$')
plt.legend()

#if using termux
plt.savefig('../images/pdf_gau.png')
plt.savefig('../images/pdf_gau.pdf')


