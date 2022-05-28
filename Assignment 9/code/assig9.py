
import numpy as np
from scipy.stats import norm
from scipy import integrate as teg
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)
x = np.linspace(-1, 1, 100)

rv = norm(0, 0.3)
i = rv.pdf(x) + rv.pdf(-x)
ii = 1 + 4 * np.exp(x) * rv.pdf(x)

n = teg.simpson(rv.pdf(x), x)
n1 = teg.simpson(i, x)
n2 = teg.simpson(ii, x)

ax.plot(x, i / n1, label ='f(0, 0.3)')

ax.plot(x, (ii/n2), label = '(1 + 4exp(x) * f(0, 0.3))*0.1618')


plt.legend()
plt.show()





