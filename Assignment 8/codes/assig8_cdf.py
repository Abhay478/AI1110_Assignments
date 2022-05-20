

import matplotlib.pyplot as plt
from scipy import special as sp

n = 10
k = 3

X = list(range(n + 1))
Y = [sp.comb(m, k) / sp.comb(n, k) for m in X] 

plt.stem(X, Y)
plt.xticks(X)
plt.xlabel('Value of m')
plt.ylabel('Probability that the largest number drawn is less than m')


plt.show()
