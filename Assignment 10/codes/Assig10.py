
import matplotlib.pyplot as plt
n = 5
X = list(range(-n, n + 1))
Y = [0] * n + [1] + [0] * n


plt.xticks(X)


plt.stem(X, Y, linefmt='k--', markerfmt='ko', basefmt='k-')

plt.xlabel('RV')
plt.ylabel('Delta Function')




plt.show()