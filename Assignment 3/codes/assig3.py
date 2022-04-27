import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


x = []
read = pd.read_excel('/Users/abhay/Latex/tables/assig3.xlsx')
raw_data = np.array(read)
freq = [row[1] for row in raw_data]

bin = [5 * (i + 6) + 1 for i in range(10)]

x = [np.linspace(bin[i], bin[i + 1] - 1, freq[i]) for i in range(9)]

lst = [np.concatenate(tuple(x))]

print(lst)


plt.hist(x=lst[0], bins=bin, alpha=0.7, rwidth=0.85, color = 'brown', range=(31, 75))

plt.grid(axis='y', alpha = 0.3)
plt.xlabel("Weights in kg")
plt.ylabel("Number of students")
plt.annotate("([46, 50], 3)", (46, 3.25))
plt.xticks(bin)

plt.show()


