import numpy as np
a = np.array([0,1,2,3,4])
select=[1,2,3,4]
x = a[select]
print(a)
print(a.size)
print(type(a))
print(a.dtype)
c = np.array([20, 1, 2, 3, 4])
# c[0] = 100
# c[1] = 20
select = [0,2,3]
d = c[select]
print(d)
a = np.linspace(-2,2 , num=5)
print(a)
