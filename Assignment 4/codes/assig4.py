
import itertools
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


S = ('m1', 'm2', 'w1', 'w2')
R = tuple(itertools.combinations(S, 2))

print("The set of all possible compositions of the committee is\n", R, "\n\n\n")

freq = [0, 0, 0]
#I checked in several packages (e.g. collections, itertools) and found no way for counting the number of instances of elements of elements of a tuple without having to use loops.
#If such a function exists, please recommend.
for com in R:
    if 'm1' not in com and 'm2' not in com:
        freq[0] += 1
    if ('m1' in com) ^ ('m2' in com):
        freq[1] += 1
    if 'm1' in com and 'm2' in com:
        freq[2] += 1
        
print("The frequency distribution is given by :", freq)

#The histogram for the same is not very informative, and hence has been omitted from the pdf.
read = pd.read_excel('./tables/assig4_fused.xlsx')
raw_data = np.array(read)
freq = np.array(raw_data[2][1:])

bin = np.array(raw_data[1][1:])


lst = np.concatenate(tuple(np.linspace(bin[i], bin[i + 1] - 1, freq[i]) for i in range(3)))

plt.hist(lst, bins=bin, alpha=0.7, rwidth=0.85, color = 'brown', range=(0, 2))

plt.grid(axis='y', alpha = 0.3)
plt.xlabel("Number of men in committee")
plt.ylabel("Number of possible committees")

plt.show()



