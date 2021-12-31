import scipy.integrate as integrate
def f(x, y):
    return x + y
a = integrate.dblquad(f, 0, 1, lambda x: 0, lambda x: 2)
print(a)
