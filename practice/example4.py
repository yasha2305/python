import numpy as np
from scipy.linalg import solve
A =np.array([[2,3],[5,4]])
B =np.array([8,13])
solution = solve(A,B)
print(solution)