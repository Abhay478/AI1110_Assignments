import numpy as np
import scipy

import mpmath as mp
theo_val = 0.5 * mp.erfc(5 / mp.sqrt(2))

plm = np.loadtxt('../data/plm.dat', dtype='int')
noi = np.loadtxt('../data/noi.dat', dtype='double')

def signs(x, y):
    return x * y > 0

vec_z = scipy.vectorize(signs)

out = vec_z(noi, plm)

#fraction of samples that defy estimate. Equal to zero, sample size too small.
print((len(out) - len(np.nonzero(out)[0])) / 10 ** 6)

#theoretical (ridiculously small) value.
print(theo_val)