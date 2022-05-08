
import matplotlib.pyplot as plt
from scipy.stats import binom

n = 3
p = 0.5

X = list(range(n + 1))
Y = [binom.pmf(i,n,p) for i in X] # better than typing all three elements as function calls

plt.stem(X, Y)
plt.xticks(X)
plt.xlabel('Random Variable X')
plt.ylabel('Probability')

for i in X:
    plt.annotate("({0:.3f})".format(Y[i]), (i, Y[i]))
plt.show()
