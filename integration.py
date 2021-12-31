from scipy.integrate import quad
def integrateFunction(x):
    return x
x = quad(integrateFunction,0,1)
print(x)

def integrateFn(x,a,b):
    return x*a+b
a=3
b=2
y = quad(integrateFn,0,1,args=(a,b))
print(y)
