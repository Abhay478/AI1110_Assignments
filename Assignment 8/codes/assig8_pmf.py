
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

n = 100
p = 0.5
k = 25


X = list(range(n + 1))
Y = [math.comb(i, k) / math.comb(n, k) for i in X] 
Z = np.cumsum(Y)

plt.xticks(X)


plt.stem(X, Y, linefmt='k--', markerfmt='ko', basefmt='k-')

plt.xlabel('X')
plt.ylabel('Cumulative Probability')
plt.grid()
plt.tight_layout()

# for i in X:
#     plt.annotate("({0})".format(round(Z[i] * 1000) / 1000), (i, Z[i]))

plt.show()