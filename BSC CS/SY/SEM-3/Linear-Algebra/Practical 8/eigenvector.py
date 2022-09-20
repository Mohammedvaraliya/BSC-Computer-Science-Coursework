import numpy as np

a = np.mat("7  3 ; 3  -1")
print(a)

print("Eigen values ", np.linalg.eigvals(a))
ev = np.linalg.eig(a)
print(ev)
