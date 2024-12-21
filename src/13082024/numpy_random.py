import numpy as np
from numpy.random import randn
x = randn()
if x > 1:
    print(x)
    answer = "X is greater than 1"

else:
    print("X is less than 1:", x)