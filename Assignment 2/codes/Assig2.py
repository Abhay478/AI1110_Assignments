
import math
import numpy as np
from numpy import linalg as la
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as mpl
from fractions import Fraction

"""
Question 15 (b):

Find the length of the perpendicular from origin to the plane r.(3i - 4j - 12k) + 39 = 0.

Solution in .pdf and .latex files
Verification: 
We will find a vector normal to the plane that starts at the origin and ends at some point on the plane. 
The length of this vector is required, and must be 3 units to verify solution.

Any vector that is normal to the plane will be of the form A + cN, where A is some vector, N is (3i - 4j - 12k) and c is a parameter.
Any vector passing through the origin will be of the form tB, where t is a parameter and B is a vector.

Therefore, the required vector will be of the form cN, where N is (3i - 4j - 12k) and k is a parameter.

Since this vector starts at the origin and ends at some point on the plane, it is a point vector for that point, and hence is a 
solution of the vector form of the plane equation. 
"""
#finding the length of vector, mathematical verifictation
d = -39
N = np.array([3, -4, -12])
c = math.fabs(d)/(N @ N)

intersection_point = c * N
nrm = la.norm(intersection_point)
print(nrm)


#plotting graph
xx, yy = np.meshgrid(range(-10, 10), range(-10, 10))
z = (-N[0] * xx - N[1] * yy - d) * 1. /N[2]

plt3d = plt.figure().gca(projection='3d')
plt3d.plot_surface(xx, yy, z)

plt3d.plot(0, 0, 0, marker = 'o', markerfacecolor='red', markeredgecolor='red')

plt3d.quiver(0, 0, 0, intersection_point[0], intersection_point[1], intersection_point[2], arrow_length_ratio=0.5, edgecolors='red')
plt3d.plot(intersection_point[0], intersection_point[1], intersection_point[2], marker = 'o', markerfacecolor='red', markeredgecolor='red')

plt3d.text(0, 0, 0, "(0, 0, 0)")
plt3d.text(intersection_point[0], intersection_point[1], intersection_point[2],
           "({0:.3g}, {1:.3g}, {2:.3g})".format(intersection_point[0], intersection_point[1], intersection_point[2], '.2f'))

plt.show()