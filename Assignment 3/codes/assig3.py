import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

read = pd.read_excel('/Users/abhay/Latex/tables/assig3.xlsx')
raw_data = np.array(read)
freq = raw_data[1][1:]

bin = np.array([31, 36, 41, 46, 51, 56, 61, 66, 71, 76])
#alternatively, bin = np.array([5 * (i + 6) + 1 for i in range(9)]). Manual entry vs. Generator, either one will do.

lst = np.concatenate(tuple(np.linspace(bin[i], bin[i + 1] - 1, freq[i]) for i in range(9)))
#alternatives include using an actual loop, or entering 38 elements manually. Above approach clearly preferable.


plt.hist(lst, bins=bin, alpha=0.7, rwidth=0.85, color = 'brown', range=(31, 75))

plt.grid(axis='y', alpha = 0.3)
plt.xlabel("Weights in kg")
plt.ylabel("Number of students")
plt.annotate("([46, 50], 3)", (46, 3.25))
plt.xticks(bin)

plt.show()


