import numpy as np
import matplotlib.pyplot as plt


randvar = np.loadtxt('noi.dat',dtype='double')
# randvar = np.linspace(-4, 4, 80)
x = np.linspace(0, 1, 1000000)
plt.grid()
plt.title("Scatter Plot")
plt.scatter(x, randvar)
# plt.show()
plt.xlabel('n e-6')
plt.ylabel('y(n)')
plt.savefig('../images/scat.png')
plt.savefig('../images/scat.pdf')
