
import numpy as np
import random as r

bag1 = np.array(['red_b1'] * 4 + ['black_b1'] * 4)
bag2 = np.array(['red_b2'] * 2 + ['black_b2'] * 6)

mix = np.concatenate((bag1, bag2))


c1 = 0
c2 = 0
#found several functions to simulate the selction, but none to simulate the nested ifs.
for i in range(10 ** 3):
    sel = r.choice(mix)
    if 'red' in sel:
        c1 += 1
        if 'b1' in sel:
            c2 += 1
            
print('{:.3f}'.format(c2 / c1))