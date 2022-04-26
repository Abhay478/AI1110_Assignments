import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

lst = np.array([])
x = []
read = pd.read_excel('/Users/abhay/Latex/tables/assig3.xlsx')
raw_data = np.array(read)
freq = [row[1] for row in raw_data]

#freq.append(row[1] for row in raw_data)
i = 31
bin = [5 * (i + 6) + 1 for i in range(10)]
print(freq)

x = [np.linspace(bin[i], bin[i + 1] - 1, freq[i]) for i in range(9)]
#print(x)
count = 0

while count < len(x):
    lst = np.concatenate((lst, np.array(x[count])))
    count += 1
    
    
        

#print(lst)



n, bins, patches = plt.hist(x=lst, bins=bin, alpha=0.7, rwidth=0.85, color = 'brown', range=(31, 75))

plt.grid(axis='y', alpha = 0.3)
plt.xlabel("Weights in kg")
plt.ylabel("Number of students")
plt.annotate("([46, 50], 3)", (46, 3.25))
plt.xticks(bin)

plt.show()


