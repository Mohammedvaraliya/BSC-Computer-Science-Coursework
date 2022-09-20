import numpy as np
a = np.mat("3  -2 ; 1  0")
print(a)
print("Eigen values ", np.linalg.eigvals(a))
ev = np.linalg.eig(a)
print(ev)
