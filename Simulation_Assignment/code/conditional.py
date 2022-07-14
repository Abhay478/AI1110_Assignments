import numpy as np
import matplotlib.pyplot as plt
import mpmath as m
import scipy

gamma = np.loadtxt('../data/con.dat', dtype='double')
# A = np.concatenate((gamma))

X = np.loadtxt('../data/plm.dat', dtype='int')
# N = np.loadtxt('../data/gau.dat', dtype='double')

res = np.concatenate((gamma))
# print(len(res))

def check(x, y):
    # if x == -1:
    #     return True
    return x * y > 0

vec = scipy.vectorize(check)

out = vec(X, res)
# print(len(np.nonzero(out)[0]))

out = np.split(out, 100)
print(len(out))

count = []
for row in out:
    count.append(1 - np.count_nonzero(row)/len(row))

lin = np.linspace(0, 10, 100)  
plt.plot(lin, count, 'o', label='simulation')
plt.grid()
plt.title('Estimation error')
def theo(x):
    return 0.5 * (1 - m.sqrt(x/(x + 2)))
vec_t = scipy.vectorize(theo)
plt.plot(lin, vec_t(lin), label='analysis')
plt.xlabel('Gamma')
plt.ylabel('Y')
plt.legend()

plt.savefig('../images/con.png')
plt.savefig('../images/con.pdf')
# plt.show()

plt.show()
plt.clf()

plt.title('Logarithmic plot')
plt.loglog(lin, count, 'o', label='simulation')
plt.loglog(lin, vec_t(lin), label='analysis')
plt.legend()
plt.savefig('../images/con_log.png')
plt.savefig('../images/con_log.pdf')