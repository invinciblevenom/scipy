import numpy as np
from scipy import optimize
def f(x):
    return x**2 + 5*np.sin(x)
minimaValue = optimize.minimize(f,x0=2,method='bfgs',options={'disp':True})
minimaValueWithoutOpt = optimize.minimize(f,x0=2,method='bfgs')
minimaValueWithoutOpt
