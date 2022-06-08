from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import norm
from scipy import integrate as teg
import matplotlib.pyplot as plt
import math

fig, ax = plt.subplots(1, 1)
x = np.linspace(-5, 5, 100)
rv = norm(0, 1)
def Gauss(x):
    return 1/math.sqrt(2 * math.pi) * math.pow(math.e, -(x ** 2)/2)

i = teg.quad(Gauss, -np.inf, 1.22)
#rv.cdf()
ax.plot(x, rv.cdf(x))
plt.xlabel('z')
plt.ylabel('CDF of Gaussian')
plt.grid()
plt.scatter([1.22], [i[0]])
plt.annotate("({0}, {1:.3f})".format(1.22, i[0]), (1.22, i[0]))
plt.show()
