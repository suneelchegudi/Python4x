import os
import numpy as np
print(os.getcwd())

# a=np.array([2,3])
#
# b=np.array([4,1])
#
# print(np.dot(a,b))

a=np.array([0,1,0,1,0])

b=np.array([1,0,1,0,1])

print(a*b)

V = {'A', 'B', 'C'}

V.add('C')
print(V)