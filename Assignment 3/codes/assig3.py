import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

lst = []
x = []
read = pd.read_excel('./tables/assig3.xlsx')
raw_data = np.array(read)
freq = []
for row in raw_data:
    freq.append(row[1])
i = 31
for k in freq:
    x = np.linspace(i, i + 4, k)
    
    for j in x:
        lst.append(j)
    i += 5


bin = [5 * (i + 6) + 1 for i in range(10)]

n, bins, patches = plt.hist(x = np.array(lst), bins=bin, alpha=0.7, rwidth=0.85, color = 'brown', range=(31, 75))

plt.grid(axis='y', alpha = 0.3)
plt.xlabel("Weights in kg")
plt.ylabel("Number of students")
plt.annotate("([46, 50], 3)", (46, 3.25))
plt.xticks([5 * (i + 6) + 1 for i in range(10)])

plt.show()
