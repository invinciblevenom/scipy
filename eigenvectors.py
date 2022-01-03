import numpy as np
from scipy import linalg

test_rating_data = np.array([[5,8],[7,9]])
eigenValues, eigenVector = linalg.eig(test_rating_data)
first_eigen, second_eigen = eigenValues
print(first_eigen, second_eigen)
print(eigenVector[:,0])
print(eigenVector[:,1])
