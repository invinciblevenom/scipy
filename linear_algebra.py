import numpy as np
from scipy import linalg

testQuestionVariable = np.array([[1, 4], [4, 9]])
testQuestionValue = np.array([30, 150])
linalg.solve(testQuestionVariable, testQuestionValue)


