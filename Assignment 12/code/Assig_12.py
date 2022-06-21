

import numpy as np
from scipy.stats import norm, chi2, halfnorm
import matplotlib.pyplot as plt

x = norm(0, 1)
y = chi2(1)
z = halfnorm()


l = np.linspace(-10, 10, 1000)

plt.plot(l, x.pdf(l), label="Gaussian")
plt.plot(l, y.pdf(l), label = "Chi-Square")
plt.plot(l, z.pdf(l), label = "Half-normal")

plt.grid(axis="both")
plt.xlabel("x")
plt.ylabel("RV(x)")
plt.legend()
plt.show()