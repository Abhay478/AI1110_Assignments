import matplotlib.pyplot as plt
import numpy as np

lst = []
x = []

freq = [9, 5, 14, 3, 1, 2, 2, 1, 1]
i = 31
for k in freq:
    x = np.linspace(i, i + 4, k)
    
    for j in x:
        lst.append(j)
    i += 5

n, bins, patches = plt.hist(x = np.array(lst), bins=9, alpha=0.7, rwidth=0.85, range=(31, 75))
plt.grid(axis='y')
plt.annotate("([46, 50], 3)", (46, 3))
plt.xticks([5 * (i + 6) + 1 for i in range(9)])

plt.show()
